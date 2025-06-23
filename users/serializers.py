from rest_framework import serializers
from .models import User, SignInHistory, UserDelete, UserDeleteReason, AccessCode, CustomerInquiry
from core.serializers import CustomSerializer
from core.representors import CustomRepresentor

class UserSerializer(CustomSerializer):
    """
    Serializer for User model input validation and object creation/updates.
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'gender', 'is_lock', 'nickname', 'aws_user', 'birth_date', 'created_at']
        read_only_fields = ['id', 'created_at']

class SignInHistorySerializer(CustomSerializer):
    class Meta:
        model = SignInHistory
        fields = ['id', 'device_name', 'device_token', 'email', 'language', 'os', 'status', 'created_at']
        read_only_fields = ['id', 'created_at']

class UserDeleteSerializer(CustomSerializer):
    class Meta:
        model = UserDelete
        fields = ['user', 'reason', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class UserDeleteReasonSerializer(CustomSerializer):
    class Meta:
        model = UserDeleteReason
        fields = ['id', 'reason', 'created_at', 'orders']
        read_only_fields = ['id', 'created_at']

class AccessCodeSerializer(CustomSerializer):
    class Meta:
        model = AccessCode
        fields = ['access_code', 'created_at', 'expired_at', 'user', 'activated_at', 'completed_survey_week']
        read_only_fields = ['created_at', 'activated_at']

class CustomerInquirySerializer(CustomSerializer):
    class Meta:
        model = CustomerInquiry
        fields = ['id', 'created_at', 'inquiry', 'user']
        read_only_fields = ['id', 'created_at']
