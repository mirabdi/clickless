from django.db import models

# Create your models here.

class Habit(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    orders = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_habit'

class HabitAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    habit_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_habit_answer'

class HabitCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    is_etc = models.BooleanField()
    orders = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_habit_category'

class HabitViolation(models.Model):
    id = models.BigAutoField(primary_key=True)
    answer_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_habit_violation'
