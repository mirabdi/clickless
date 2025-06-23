from django.shortcuts import render
from rest_framework import viewsets
from core.views import CustomViewSet
from rest_framework.decorators import action
from .models import Exercise, ExerciseHistory, ExerciseTime
from .serializers import ExerciseSerializer, ExerciseHistorySerializer, ExerciseTimeSerializer
from .representors import ExerciseRepresentor, ExerciseHistoryRepresentor, ExerciseTimeRepresentor

# Create your views here.

class ExerciseViewSet(CustomViewSet):
    model_manager = Exercise.objects
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    representor_class = ExerciseRepresentor
    search_fields = ['title', 'type']

    @action(detail=True, methods=['get'])
    def histories(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'histories')

class ExerciseHistoryViewSet(CustomViewSet):
    model_manager = ExerciseHistory.objects
    queryset = ExerciseHistory.objects.all()
    serializer_class = ExerciseHistorySerializer
    representor_class = ExerciseHistoryRepresentor

class ExerciseTimeViewSet(CustomViewSet):
    model_manager = ExerciseTime.objects
    queryset = ExerciseTime.objects.all()
    serializer_class = ExerciseTimeSerializer
    representor_class = ExerciseTimeRepresentor
