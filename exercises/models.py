from django.db import models
from core.models import CustomModel
from users.models import User

# Create your models here.

class Exercise(CustomModel):
    id = models.BigAutoField(primary_key=True)
    tutorial = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    orders = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    has_face = models.IntegerField()

    class Meta:
        
        db_table = 'v2_exercise'

    def __str__(self):
        return f"{self.title} ({self.type})"

class ExerciseHistory(CustomModel):
    id = models.BigAutoField(primary_key=True)
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING, related_name='histories')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id', related_name='exercise_histories')
    created_at = models.DateTimeField()
    is_face = models.IntegerField()

    class Meta:
        
        db_table = 'v2_exercise_history'

    def __str__(self):
        return f"Exercise History {self.id} - {self.exercise.title} by {self.user.email}"

class ExerciseTime(CustomModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    time_since_midnight = models.IntegerField()
    user = models.ForeignKey('users.User', models.DO_NOTHING, blank=True, null=True, related_name='exercise_times')

    class Meta:
        
        db_table = 'v2_exercise_time'

    def __str__(self):
        return f"Exercise Time {self.id} - User: {self.user.email if self.user else 'No user'}, Time: {self.time_since_midnight}"
