from rest_framework import serializers
from core.representors import CustomRepresentor
from .models import Exercise, ExerciseHistory, ExerciseTime

class ExerciseRepresentor(CustomRepresentor):
    class Meta:
        model = Exercise
        fields = ['id', 'tutorial', 'url', 'title', 'type', 'orders', 'created_at', 'deleted_at', 'has_face']

class ExerciseHistoryRepresentor(CustomRepresentor):
    class Meta:
        model = ExerciseHistory
        fields = ['id', 'exercise_id', 'user_id', 'created_at', 'is_face']

class ExerciseTimeRepresentor(CustomRepresentor):
    class Meta:
        model = ExerciseTime
        fields = ['id', 'time_since_midnight', 'user_id', 'created_at', 'updated_at'] 