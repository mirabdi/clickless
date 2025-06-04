from rest_framework import serializers
from core.serializers import CustomSerializer
from .models import Habit, HabitAnswer, HabitCategory, HabitViolation

class HabitSerializer(CustomSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'category_id', 'name', 'orders', 'created_at', 'deleted_at']

class HabitAnswerSerializer(CustomSerializer):
    class Meta:
        model = HabitAnswer
        fields = ['id', 'user_id', 'habit_id', 'created_at', 'deleted_at']

class HabitCategorySerializer(CustomSerializer):
    class Meta:
        model = HabitCategory
        fields = ['id', 'name', 'is_etc', 'orders', 'created_at', 'deleted_at']

class HabitViolationSerializer(CustomSerializer):
    class Meta:
        model = HabitViolation
        fields = ['id', 'answer_id', 'created_at', 'deleted_at'] 