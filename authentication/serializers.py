from rest_framework import serializers
from core.serializers import CustomSerializer
from .models import Admin

class AdminSerializer(CustomSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'email', 'is_active', 'created_at', 'updated_at'] 