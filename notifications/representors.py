from rest_framework import serializers
from core.representors import CustomRepresentor
from .models import Notification, NotificationCategory, NotificationExclusion

class NotificationRepresentor(CustomRepresentor):
    class Meta:
        model = Notification
        fields = ['id', 'content', 'is_read', 'title', 'user_id', 'type', 'created_at', 'updated_at']

class NotificationCategoryRepresentor(CustomRepresentor):
    class Meta:
        model = NotificationCategory
        fields = ['id', 'name', 'orders', 'enum_name', 'created_at', 'updated_at']

class NotificationExclusionRepresentor(CustomRepresentor):
    class Meta:
        model = NotificationExclusion
        fields = ['id', 'user_id', 'category_id', 'created_at'] 