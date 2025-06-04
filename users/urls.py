from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, SignInHistoryViewSet, UserDeleteViewSet,
    UserDeleteReasonViewSet, AccessCodeViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sign-in-history', SignInHistoryViewSet)
router.register(r'user-deletes', UserDeleteViewSet)
router.register(r'user-delete-reasons', UserDeleteReasonViewSet)
router.register(r'access-codes', AccessCodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 