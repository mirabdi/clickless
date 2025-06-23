from rest_framework import serializers
from core.serializers import CustomSerializer
from .models import Notification, NotificationCategory, NotificationExclusion

class NotificationSerializer(CustomSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'content', 'is_read', 'title', 'user', 'type', 'created_at', 'updated_at']

class NotificationCategorySerializer(CustomSerializer):
    class Meta:
        model = NotificationCategory
        fields = ['id', 'name', 'orders', 'enum_name', 'created_at', 'updated_at']

class NotificationExclusionSerializer(CustomSerializer):
    class Meta:
        model = NotificationExclusion
        fields = ['id', 'user', 'category', 'created_at'] 