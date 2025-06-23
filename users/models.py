from django.db import models
from django.utils import timezone
from core.models import CustomModel

class User(CustomModel):
    created_at = models.DateTimeField()
    email = models.CharField(unique=True, max_length=255)
    gender = models.IntegerField()
    is_lock = models.TextField()  # This field type is a guess.
    nickname = models.CharField(max_length=255)
    aws_user_id = models.CharField(max_length=45)
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        # 
        db_table = 'user'

    def __str__(self):
        return f"{self.nickname} ({self.email})"

class SignInHistory(CustomModel):
    created_at = models.DateTimeField()
    device_name = models.CharField(max_length=255)
    device_token = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'sign_in_history'

    def __str__(self):
        return f"Sign In - {self.email} on {self.device_name} ({self.os})"

class UserDelete(CustomModel):
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    reason = models.ForeignKey('UserDeleteReason', models.DO_NOTHING, blank=True, null=True, related_name='user_deletes')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'v2_user_delete'

    def __str__(self):
        return f"User Delete - {self.user.email}"

class UserDeleteReason(CustomModel):
    id = models.SmallAutoField(primary_key=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    orders = models.IntegerField()

    class Meta:
        
        db_table = 'v2_user_delete_reason'

    def __str__(self):
        return self.reason or f"Reason {self.id}"

class AccessCode(CustomModel):
    access_code = models.CharField(primary_key=True, max_length=255)
    created_at = models.DateTimeField()
    expired_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_id', blank=True, null=True, related_name='access_codes')
    activated_at = models.DateTimeField(blank=True, null=True)
    completed_survey_week = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'access_code'

    def __str__(self):
        return f"Access Code: {self.access_code}"

class CustomerInquiry(CustomModel):
    created_at = models.DateTimeField(blank=True, null=True)
    inquiry = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='customer_inquiries')

    class Meta:
        
        db_table = 'v2_customer_inquiry'

    def __str__(self):
        return f"Inquiry {self.id} - {self.inquiry[:50] if self.inquiry else 'No inquiry'}"
