from rest_framework import serializers
from core.representors import CustomRepresentor
from .models import Habit, HabitAnswer, HabitCategory, HabitViolation

class HabitRepresentor(CustomRepresentor):
    class Meta:
        model = Habit
        fields = ['id', 'category_id', 'name', 'orders', 'created_at', 'deleted_at']

class HabitAnswerRepresentor(CustomRepresentor):
    class Meta:
        model = HabitAnswer
        fields = ['id', 'user_id', 'habit_id', 'created_at', 'deleted_at']

class HabitCategoryRepresentor(CustomRepresentor):
    class Meta:
        model = HabitCategory
        fields = ['id', 'name', 'is_etc', 'orders', 'created_at', 'deleted_at']

class HabitViolationRepresentor(CustomRepresentor):
    class Meta:
        model = HabitViolation
        fields = ['id', 'answer_id', 'created_at', 'deleted_at'] 