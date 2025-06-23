from django.shortcuts import render
from rest_framework import viewsets
from core.views import CustomViewSet
from rest_framework.decorators import action
from .models import Notification, NotificationCategory, NotificationExclusion
from .serializers import NotificationSerializer, NotificationCategorySerializer, NotificationExclusionSerializer
from .representors import NotificationRepresentor, NotificationCategoryRepresentor, NotificationExclusionRepresentor

# Create your views here.

class NotificationViewSet(CustomViewSet):
    model_manager = Notification.objects
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    representor_class = NotificationRepresentor
    search_fields = ['title', 'content']

class NotificationCategoryViewSet(CustomViewSet):
    model_manager = NotificationCategory.objects
    queryset = NotificationCategory.objects.all()
    serializer_class = NotificationCategorySerializer
    representor_class = NotificationCategoryRepresentor
    search_fields = ['name', 'enum_name']

    @action(detail=True, methods=['get'])
    def exclusions(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'exclusions')

class NotificationExclusionViewSet(CustomViewSet):
    model_manager = NotificationExclusion.objects
    queryset = NotificationExclusion.objects.all()
    serializer_class = NotificationExclusionSerializer
    representor_class = NotificationExclusionRepresentor
