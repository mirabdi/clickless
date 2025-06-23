from rest_framework import serializers
from core.representors import CustomRepresentor
from .models import Habit, HabitAnswer, HabitCategory, HabitViolation

class HabitRepresentor(CustomRepresentor):
    class Meta:
        model = Habit
        fields = ['id', 'category', 'name', 'orders', 'created_at', 'deleted_at', 'answers']

class HabitAnswerRepresentor(CustomRepresentor):
    class Meta:
        model = HabitAnswer
        fields = ['id', 'user', 'habit', 'created_at', 'deleted_at', 'violations']

class HabitCategoryRepresentor(CustomRepresentor):
    class Meta:
        model = HabitCategory
        fields = ['id', 'name', 'is_etc', 'orders', 'created_at', 'deleted_at', 'habits']

class HabitViolationRepresentor(CustomRepresentor):
    class Meta:
        model = HabitViolation
        fields = ['id', 'answer', 'created_at', 'deleted_at'] 