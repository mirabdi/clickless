from rest_framework import serializers
from core.representors import CustomRepresentor
from .models import Notification, NotificationCategory, NotificationExclusion

class NotificationRepresentor(CustomRepresentor):
    class Meta:
        model = Notification
        fields = ['id', 'content', 'is_read', 'title', 'user', 'type', 'created_at', 'updated_at']

class NotificationCategoryRepresentor(CustomRepresentor):
    class Meta:
        model = NotificationCategory
        fields = ['id', 'name', 'orders', 'enum_name', 'created_at', 'updated_at', 'exclusions']

class NotificationExclusionRepresentor(CustomRepresentor):
    class Meta:
        model = NotificationExclusion
        fields = ['id', 'user', 'category', 'created_at'] 