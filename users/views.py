from django.shortcuts import render
from core.views import CustomViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from authentication.token_auth import AdminTokenAuth
from .models import User, SignInHistory, UserDelete, UserDeleteReason, AccessCode, CustomerInquiry
from .serializers import (
    UserSerializer, SignInHistorySerializer, UserDeleteSerializer,
    UserDeleteReasonSerializer, AccessCodeSerializer, CustomerInquirySerializer
)
from .representors import (
    UserRepresentor, SignInHistoryRepresentor, UserDeleteRepresentor,
    UserDeleteReasonRepresentor, AccessCodeRepresentor, CustomerInquiryRepresentor
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

    @action(detail=True, methods=['get'], url_path='habit_answers')
    def habit_answers(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'habit_answers')
    
    @action(detail=True, methods=['get'], url_path='answers')
    def survey_answers(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'answers')
    
    @action(detail=True, methods=['get'], url_path='pain_answers')
    def survey_pain_answers(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'pain_answers')
    
    @action(detail=True, methods=['get'], url_path='diary_entries')
    def diary_entries(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'diary_entries')

    @action(detail=True, methods=['get'], url_path='pain_records')
    def pain_records(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'pain_records')

    @action(detail=True, methods=['get'], url_path='drugs')
    def drugs(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'drugs')

    @action(detail=True, methods=['get'], url_path='notifications')
    def notifications(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'notifications')

    @action(detail=True, methods=['get'], url_path='notification_exclusions')
    def notification_exclusions(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'notification_exclusions')

    @action(detail=True, methods=['get'], url_path='exercise_histories')
    def exercise_histories(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'exercise_histories')

    @action(detail=True, methods=['get'], url_path='exercise_times')
    def exercise_times(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'exercise_times')

    @action(detail=True, methods=['get'], url_path='article_view_histories')
    def article_view_histories(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'article_view_histories')

    @action(detail=True, methods=['get'], url_path='education_video_view_histories')
    def education_video_view_histories(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'education_video_view_histories')

    @action(detail=True, methods=['get'], url_path='meditation_histories')
    def meditation_histories(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'meditation_histories')

    @action(detail=True, methods=['get'], url_path='access_codes')
    def access_codes(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'access_codes')

    @action(detail=True, methods=['get'], url_path='customer_inquiries')
    def customer_inquiries(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'customer_inquiries')

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

    @action(detail=True, methods=['get'], url_path='user_deletes')
    def user_deletes(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'user_deletes')

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

class CustomerInquiryViewSet(CustomViewSet):
    """
    ViewSet for managing customer inquiries
    """
    model_manager = CustomerInquiry.objects
    queryset = CustomerInquiry.objects.all()
    serializer_class = CustomerInquirySerializer
    representor_class = CustomerInquiryRepresentor
    permission_classes = []
    
    search_fields = ['inquiry', 'user_id']
    limit = 20
