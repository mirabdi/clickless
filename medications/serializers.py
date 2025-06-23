from rest_framework import serializers
from core.serializers import CustomSerializer
from .models import Drug, DrugDetail, DrugType

class DrugSerializer(CustomSerializer):
    class Meta:
        model = Drug
        fields = ['id', 'user', 'name', 'type', 'created_at', 'finished_at', 'deleted_at']

class DrugDetailSerializer(CustomSerializer):
    class Meta:
        model = DrugDetail
        fields = ['id', 'drug', 'time', 'created_at', 'deleted_at']

class DrugTypeSerializer(CustomSerializer):
    class Meta:
        model = DrugType
        fields = ['id', 'type', 'created_at', 'deleted_at', 'orders'] 