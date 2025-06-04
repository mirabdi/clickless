from rest_framework import serializers
from django.db.models import QuerySet, Model
from rest_framework.fields import get_attribute

class CustomRepresentor(serializers.Serializer):
    """
    Base representor for handling output representation.
    Handles both single object and list serialization with metadata.
    """
    meta = serializers.SerializerMethodField()

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add meta to fields if not present
        if hasattr(self.Meta, 'fields') and isinstance(self.Meta.fields, (list, tuple)):
            if "meta" not in self.Meta.fields:
                self.Meta.fields = ["meta"] + list(self.Meta.fields)

    def get_fields(self):
        """
        Return all declared fields + model fields specified in Meta.
        """
        fields = super().get_fields()
        
        # Add model fields if specified in Meta
        if hasattr(self, 'Meta') and hasattr(self.Meta, 'model') and hasattr(self.Meta, 'fields'):
            model_fields = {
                field.name: self._create_field(field.name)
                for field in self.Meta.model._meta.fields 
                if field.name in self.Meta.fields
            }
            fields.update(model_fields)
            
        return fields

    def _create_field(self, field_name):
        """Create a serializer field for a model field."""
        model_field = self.Meta.model._meta.get_field(field_name)
        field_class = serializers.ModelSerializer.serializer_field_mapping.get(
            model_field.__class__, serializers.CharField
        )
        return field_class()

    def get_meta(self, obj):
        """Returns metadata for single object."""
        if hasattr(obj, "meta") and callable(getattr(obj, "meta")):
            return obj.meta()
        return {
            'id': getattr(obj, 'id', None),
            'name': str(obj),
            'type': obj.__class__.__name__.lower(),
        }

    def to_representation(self, instance):
        """Handle both single object and list representations."""
        # Handle list case
        if isinstance(instance, (list, QuerySet)):
            return self._list_representation(instance)

        # Handle single object
        if not self.context.get('detailed', False):
            return {'meta': self.get_meta(instance)}

        representation = {}
        for field_name in self.Meta.fields:
            if field_name == 'meta':
                representation['meta'] = self.get_meta(instance)
                continue

            # Handle method fields
            method_name = f'get_{field_name}'
            if hasattr(self, method_name):
                if method_name in ['get_value', 'get_initial']:
                    continue
                representation[field_name] = getattr(self, method_name)(instance)
                continue

            # Get value and serialize
            try:
                representation[field_name] = self._serialize_value(instance, field_name)
            except Exception as e:
                print(f"Error serializing field {field_name}: {str(e)}")
                representation[field_name] = None

        return representation

    def _list_representation(self, queryset):
        """Handle list representation with metadata."""
        model_name = queryset.model.__name__.lower()
        limit = self.context.get('limit', 10)
        offset = self.context.get('offset', 0)
        
        response = {
            'meta': {
                'type': f'{model_name}-list',
                'href': f'{self.Meta.model.get_href()}',
                'size': queryset.count(),
                'limit': limit,
                'offset': offset
            }
        }

        if self.context.get('detailed', False):
            if isinstance(queryset, QuerySet):
                queryset = queryset[offset:offset + limit]
            response['rows'] = [
                self.__class__(item, context=self.context).to_representation(item)
                for item in queryset
            ]

        return response

    def _serialize_value(self, instance, field_name):
        """Serialize different types of values."""
        value = get_attribute(instance, field_name.split('.'))
        if value is None:
            return None

        # Special handling for reverse relation descriptors
        if str(value.__class__).endswith("RelatedManager'>") or isinstance(value, Model):
            return instance.get_field_meta(field_name) 
            
        # Handle callable (but not model classes)
        if callable(value) and not isinstance(value, type):
            return value()
        return value 