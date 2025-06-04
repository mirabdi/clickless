from django.shortcuts import render
from core.views import CustomViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from authentication.token_auth import AdminTokenAuth
from .models import User, SignInHistory, UserDelete, UserDeleteReason, AccessCode
from .serializers import (
    UserSerializer, SignInHistorySerializer, UserDeleteSerializer,
    UserDeleteReasonSerializer, AccessCodeSerializer
)
from .representors import (
    UserRepresentor, SignInHistoryRepresentor, UserDeleteRepresentor,
    UserDeleteReasonRepresentor, AccessCodeRepresentor
)

# Create your views here.

class UserViewSet(CustomViewSet):
    """
    ViewSet for managing users
    """
    model_manager = User.objects
    queryset = User.objects.all()
    serializer_class = UserSerializer
    representor_class = UserRepresentor
    permission_classes = [AllowAny]  # Allow unauthenticated access for now
    
    # Override search fields for users
    search_fields = ['email', 'nickname']
    
    # Override default limit
    limit = 20

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        """Login endpoint to get JWT token"""
        email = request.data.get('email')
        if not email:
            return self._respond(
                None,
                message="Email is required",
                status_code=400
            )
        
        try:
            user = User.objects.get(email=email)
            token = AdminTokenAuth.generate_token(user)
            return self._respond({
                'token': token,
                'user': self.representor_class(user, context={'detailed': True}).data
            })
        except User.DoesNotExist:
            return self._respond(
                None,
                message="User not found",
                status_code=404
            )

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Test endpoint that requires authentication"""
        return self._respond(
            self.representor_class(request.user, context={'detailed': True}).data,
            message="Successfully authenticated"
        )
    
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



class SignInHistoryViewSet(CustomViewSet):
    """
    ViewSet for managing sign in history
    """
    model_manager = SignInHistory.objects
    queryset = SignInHistory.objects.all()
    serializer_class = SignInHistorySerializer
    representor_class = SignInHistoryRepresentor
    permission_classes = []
    
    search_fields = ['email', 'device_name', 'os']
    limit = 20

class UserDeleteViewSet(CustomViewSet):
    """
    ViewSet for managing user deletions
    """
    model_manager = UserDelete.objects
    queryset = UserDelete.objects.all()
    serializer_class = UserDeleteSerializer
    representor_class = UserDeleteRepresentor
    permission_classes = []
    
    search_fields = ['user_id', 'reason_id']
    limit = 20

class UserDeleteReasonViewSet(CustomViewSet):
    """
    ViewSet for managing user deletion reasons
    """
    model_manager = UserDeleteReason.objects
    queryset = UserDeleteReason.objects.all()
    serializer_class = UserDeleteReasonSerializer
    representor_class = UserDeleteReasonRepresentor
    permission_classes = []
    
    search_fields = ['reason']
    limit = 20

class AccessCodeViewSet(CustomViewSet):
    """
    ViewSet for managing access codes
    """
    model_manager = AccessCode.objects
    queryset = AccessCode.objects.all()
    serializer_class = AccessCodeSerializer
    representor_class = AccessCodeRepresentor
    permission_classes = []
    
    search_fields = ['access_code', 'user_id']
    limit = 20
