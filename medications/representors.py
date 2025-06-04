from rest_framework import serializers
from core.representors import CustomRepresentor
from .models import Drug, DrugDetail, DrugType

class DrugRepresentor(CustomRepresentor):
    class Meta:
        model = Drug
        fields = ['id', 'user_id', 'name', 'type', 'created_at', 'finished_at', 'deleted_at']

class DrugDetailRepresentor(CustomRepresentor):
    class Meta:
        model = DrugDetail
        fields = ['id', 'drug_id', 'time', 'created_at', 'deleted_at']

class DrugTypeRepresentor(CustomRepresentor):
    class Meta:
        model = DrugType
        fields = ['id', 'type', 'created_at', 'deleted_at', 'orders'] 