from rest_framework import serializers
from django.db.models import Manager, QuerySet, Model
from rest_framework.fields import get_attribute

class CustomSerializer(serializers.ModelSerializer):
    """
    Base serializer for handling input validation and object creation/updates.
    """
    class Meta:
        abstract = True

    def process_relationships(self, validated_data):
        """Process relationship fields with _id/_ids suffix."""
        relationships = {}
        model_data = {}

        for key, value in validated_data.items():
            if key.endswith('_id'):
                field = key[:-3]
                relationships[field] = value
            elif key.endswith('_ids'):
                field = key[:-4]
                relationships[field] = value
            else:
                model_data[key] = value

        return relationships, model_data

    def create(self, validated_data):
        relationships, model_data = self.process_relationships(validated_data)
        
        instance = self.Meta.model.objects.create(**model_data)
        
        for field, value in relationships.items():
            field_obj = getattr(instance, field)
            if isinstance(field_obj, Manager):
                field_obj.set(value)
            else:
                setattr(instance, field, value)
                instance.save()
                
        return instance

    def update(self, instance, validated_data):
        relationships, model_data = self.process_relationships(validated_data)
        
        for attr, value in model_data.items():
            setattr(instance, attr, value)
            
        for field, value in relationships.items():
            field_obj = getattr(instance, field)
            if isinstance(field_obj, Manager):
                if value is not None:
                    field_obj.set(value)
            else:
                setattr(instance, field, value)
                
        instance.save()
        return instance
