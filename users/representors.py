from core.representors import CustomRepresentor
from .models import User, SignInHistory, UserDelete, UserDeleteReason, AccessCode

class UserRepresentor(CustomRepresentor):
    class Meta:
        model = User
        fields = ['id', 'email', 'gender', 'is_lock', 'nickname', 'aws_user_id', 'birth_date', 'created_at']

class SignInHistoryRepresentor(CustomRepresentor):
    class Meta:
        model = SignInHistory
        fields = ['id', 'device_name', 'device_token', 'email', 'language', 'os', 'status', 'created_at']

class UserDeleteRepresentor(CustomRepresentor):
    class Meta:
        model = UserDelete
        fields = ['user_id', 'reason_id', 'created_at', 'updated_at']

class UserDeleteReasonRepresentor(CustomRepresentor):
    class Meta:
        model = UserDeleteReason
        fields = ['id', 'reason', 'created_at', 'orders']

class AccessCodeRepresentor(CustomRepresentor):
    class Meta:
        model = AccessCode
        fields = ['access_code', 'created_at', 'expired_at', 'user_id', 'activated_at', 'completed_survey_week'] 