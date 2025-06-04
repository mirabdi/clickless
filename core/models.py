from django.db import models
from django.utils.module_loading import import_string
from datetime import datetime as dt
from rest_framework.pagination import LimitOffsetPagination
from django.utils.translation import gettext_lazy as _


class CustomManager(models.Manager):
    """
    A base manager for models with centralized pagination and serialization logic.
    Child managers must set the `serializer_class` attribute.
    """
    serializer_class = None 

    def __init__(self, serializer_class_path=None):
        super().__init__()
        self._serializer_class_path = serializer_class_path

    def contribute_to_class(self, model, name):
        super().contribute_to_class(model, name)
        self.model = model
    
    def get_serializer_class(self):
        """
        Returns the serializer class for the model.
        """
        try:
            path = self._serializer_class_path
            if path is None:
                path = f"{self.model._meta.app_label}.admin.representors.{self.model.__name__}Representor"
            self._serializer_class = import_string(path)
            return self._serializer_class
        except (ImportError, AttributeError) as e:
            raise ValueError(f"Could not find Representor at {path}: {str(e)}")
        
    def serialize(self, queryset, limit=100, offset=0, context={'detailed': False}):
        """
        Centralized method to handle pagination and serialization.

        Args:
            queryset: The queryset to paginate and serialize.
            serializer_class: The serializer class to use.
            context: Additional context for the serializer.
            limit: The number of items per page (default is None).
            offset: The starting index (default is None).
            request: The HTTP request (used for building absolute URIs).

        Returns:
            dict: A dictionary with `meta` and `rows`.
        """
        # if queryset, request or serializer_class is not provided:
        if queryset is None:
            raise ValueError("queryset is required")
        
        detailed = context.get('detailed', True)
        meta = {
            "type": f"{queryset.model.__name__.lower()}-list",
            "href": f"/admin-api/{queryset.model.__name__.lower()}s/",
            "size":  queryset.count(),
            "limit": offset,
            "offset": limit,
        }

        if not detailed:
            return {"meta": meta} 

        paginator = LimitOffsetPagination()
        paginator.default_limit = limit
        paginator.offset = offset
        start = offset
        end = start + limit
        paginated_queryset = queryset[start:end]

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(paginated_queryset, many=True, context=context)
        serialized_data = serializer.data

        return {
            "meta": meta,
            "rows": serialized_data,
        }
        
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
    
    def with_deleted(self):
        return super().get_queryset()
    
    def delete(self, queryset=None):
        """
        Soft delete items in the given queryset or all items if no queryset is provided.
        
        Args:
            queryset (QuerySet, optional): Queryset to soft delete. 
                                           If None, deletes all items.
        
        Returns:
            int: Number of items soft deleted
        """
        if queryset is None:
            raise ValueError("queryset is required")
        
        # Use update to perform a bulk soft delete
        deleted_count = queryset.update(deleted=True)
        return deleted_count
    
    def restore(self, queryset=None):
        """
        Restore items in the given queryset or all items if no queryset is provided.
        
        Args:
            queryset (QuerySet, optional): Queryset to restore. 
                                           If None, restores all items.
        
        Returns:
            int: Number of items restored
        """
        if queryset is None:
            raise ValueError("queryset is required")
        
        # Use update to perform a bulk restore
        restored_count = queryset.update(deleted=False, deleted_at=None)
        return restored_count


class CustomModel(models.Model):
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    _href = None
    objects = CustomManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        abstract = True

    @classmethod
    def get_href(cls):
        """
        Returns the base URL path for the model.
        Can be overridden by child classes by setting _href class attribute.
        Converts camel case class names to hyphenated form.
        """
        if hasattr(cls, '_href') and cls._href:
            return cls._href
        
        # Convert camel case to hyphenated
        name = cls.__name__
        hyphenated_name = ''
        for i, char in enumerate(name):
            if i > 0 and char.isupper():
                hyphenated_name += '-'
            hyphenated_name += char.lower()
        
        # Convert to plural form
        if hyphenated_name.endswith('y'):
            plural = hyphenated_name[:-1] + 'ies'
        else:
            plural = hyphenated_name + 's'
        
        return f"/{cls._meta.app_label}/admin-api/{plural}"

    def meta(self):
        """
        Returns the metadata for the model instance.
        """
        return {
            'id': self.id,
            'name': self.__str__(),
            'type': self._type if hasattr(self, '_type') else self.__class__.__name__.lower(),
            'href': self.get_url(),
        }

    def get_field_meta(self, field_name):
        """
        Returns metadata for a specific field, with special handling for related managers.
        
        Args:
            field_name (str): Name of the field to get metadata for
            
        Returns:
            dict: Metadata for the field including type, size (for related managers), and href
        """
        try:
            field_obj = getattr(self, field_name)
            
            # Handle related managers (many-to-many relationships)
            if isinstance(field_obj, models.Manager):
                return {
                    'meta': {
                        'type': f"{field_obj.model.__name__.lower()}-list",
                        'size': field_obj.count(),
                        'href': f"{self.get_url()}/{field_name}",
                    }
                }
            
            # Handle foreign key relationships
            elif isinstance(field_obj, models.Model):
                return field_obj.meta_dict()
            
                
        except AttributeError:
            return None

    def meta_dict(self, field=None):
        """
        Returns the metadata as a dictionary.
        """
        if field is None:
            return {
                "meta": self.meta(),
            }
        
        return {
            field: self.meta(),
        }
        
    def delete(self):
        """
        Override the default delete method to perform a soft delete.
        
        Args:
            using: The database to use for the delete operation.
            keep_parents: Whether to keep parent model instances.
        """
        self.deleted = True
        self.deleted_at = dt.now()
        self.save(update_fields=['deleted', 'deleted_at'])

    def restore(self):
        """
        Restore the model instance from a soft delete.
        """
        self.deleted = False
        self.deleted_at = None
        self.save(update_fields=['deleted', 'deleted_at'])

    def hard_delete(self):
        """
        Perform a hard delete on the model instance.
        """
        super().delete()

    def get_url(self):
        """
        Returns the URL for the model instance.
        """
        return f"{self.get_href()}/{self.id}"
