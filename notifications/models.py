from django.db import models
from core.models import CustomModel
from users.models import User

# Create your models here.

class Notification(CustomModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.TextField()  # This field type is a guess.
    title = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id', related_name='notifications')
    type = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'v2_notification'

    def __str__(self):
        return f"{self.title or 'No title'} - {self.user.email} ({self.type})"

class NotificationCategory(CustomModel):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    orders = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    enum_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'v2_notification_category'

    def __str__(self):
        return self.name or f"Category {self.id}"

class NotificationExclusion(CustomModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('users.User', models.DO_NOTHING, related_name='notification_exclusions')
    category = models.ForeignKey(NotificationCategory, models.DO_NOTHING, blank=True, null=True, related_name='exclusions')
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'v2_notification_exclusion'

    def __str__(self):
        return f"Notification Exclusion {self.id} - {self.user.email} - {self.category.name if self.category else 'All categories'}"
