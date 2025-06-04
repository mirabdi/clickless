from django.db import models
from core.models import CustomModel

# Create your models here.

class Exercise(CustomModel):
    id = models.BigAutoField(primary_key=True)
    tutorial = models.CharField(max_length=200, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    orders = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    has_face = models.BooleanField()

    class Meta:
        db_table = 'v2_exercise'

class ExerciseHistory(CustomModel):
    id = models.BigAutoField(primary_key=True)
    exercise_id = models.BigIntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_face = models.BooleanField()

    class Meta:
        db_table = 'v2_exercise_history'

class ExerciseTime(CustomModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    time_since_midnight = models.IntegerField()
    user_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'v2_exercise_time'
