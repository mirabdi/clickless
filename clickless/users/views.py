from django.shortcuts import render
from core.views import CustomViewSet
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer, UserRepresentor

# Create your views here.

class UserViewSet(CustomViewSet):
    """
    ViewSet for managing users
    """
    model_manager = User.objects
    queryset = User.objects.all()
    serializer_class = UserSerializer
    representor_class = UserRepresentor
    
    # Override search fields for users
    search_fields = ['username', 'email', 'phone', 'first_name', 'last_name']
    
    # Override default limit
    limit = 20
    
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        instance = self.get_object(pk)
        instance.is_active = True
        instance.save()
        return self._respond(
            self.representor_class(instance, context={'detailed': True}).data,
            message="User activated successfully"
        )
    
    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        instance = self.get_object(pk)
        instance.is_active = False
        instance.save()
        return self._respond(
            self.representor_class(instance, context={'detailed': True}).data,
            message="User deactivated successfully"
        )
