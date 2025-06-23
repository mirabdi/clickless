from django.db import models
from core.models import CustomModel
from users.models import User

# Create your models here.

class Habit(CustomModel):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey('HabitCategory', models.DO_NOTHING, related_name='habits')
    name = models.CharField(max_length=50)
    orders = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_habit'

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class HabitAnswer(CustomModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id', related_name='habit_answers')
    habit = models.ForeignKey(Habit, models.DO_NOTHING, db_column='habit_id', related_name='answers')
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_habit_answer'

    def __str__(self):
        return f"Habit Answer {self.id} - {self.user.email} - {self.habit.name}"

class HabitCategory(CustomModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    is_etc = models.IntegerField()
    orders = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_habit_category'

    def __str__(self):
        return self.name

class HabitViolation(CustomModel):
    id = models.BigAutoField(primary_key=True)
    answer = models.ForeignKey(HabitAnswer, models.DO_NOTHING, related_name='violations')
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_habit_violation'

    def __str__(self):
        return f"Habit Violation {self.id} - {self.answer.user.email} - {self.answer.habit.name}"
