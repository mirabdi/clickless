from django.db import models
from django.utils import timezone
from core.models import CustomModel

class User(CustomModel):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=255)
    gender = models.IntegerField()
    is_lock = models.BooleanField()
    nickname = models.CharField(max_length=255)
    aws_user_id = models.CharField(max_length=45)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'user'

class SignInHistory(CustomModel):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    device_name = models.CharField(max_length=255)
    device_token = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        db_table = 'sign_in_history'

class UserDelete(CustomModel):
    user_id = models.IntegerField(primary_key=True)
    reason_id = models.SmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'v2_user_delete'

class UserDeleteReason(CustomModel):
    id = models.SmallAutoField(primary_key=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    orders = models.IntegerField()

    class Meta:
        db_table = 'v2_user_delete_reason'

class AccessCode(CustomModel):
    access_code = models.CharField(max_length=255, primary_key=True)
    created_at = models.DateTimeField()
    expired_at = models.DateTimeField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    activated_at = models.DateTimeField(null=True, blank=True)
    completed_survey_week = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'access_code'
