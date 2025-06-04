from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet, NotificationCategoryViewSet, NotificationExclusionViewSet

router = DefaultRouter()
router.register(r'notifications', NotificationViewSet)
router.register(r'notification-categories', NotificationCategoryViewSet)
router.register(r'notification-exclusions', NotificationExclusionViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 