from rest_framework import serializers
from core.representors import CustomRepresentor
from .models import Admin

class AdminRepresentor(CustomRepresentor):
    class Meta:
        model = Admin
        fields = ['id', 'email', 'is_active', 'created_at', 'updated_at'] 