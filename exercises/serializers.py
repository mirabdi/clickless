from rest_framework import serializers
from core.serializers import CustomSerializer
from .models import Exercise, ExerciseHistory, ExerciseTime

class ExerciseSerializer(CustomSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'tutorial', 'url', 'title', 'type', 'orders', 'created_at', 'deleted_at', 'has_face']

class ExerciseHistorySerializer(CustomSerializer):
    class Meta:
        model = ExerciseHistory
        fields = ['id', 'exercise_id', 'user_id', 'created_at', 'is_face']

class ExerciseTimeSerializer(CustomSerializer):
    class Meta:
        model = ExerciseTime
        fields = ['id', 'time_since_midnight', 'user_id', 'created_at', 'updated_at'] 