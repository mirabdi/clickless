from django.db import models

# Create your models here.

class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    is_read = models.BooleanField()
    title = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.IntegerField()
    type = models.CharField(max_length=255)

    class Meta:
        db_table = 'v2_notification'

class NotificationCategory(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    orders = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    enum_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'v2_notification_category'

class NotificationExclusion(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    category_id = models.SmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'v2_notification_exclusion'
