from django.shortcuts import render
from rest_framework import viewsets
from core.views import CustomViewSet
from rest_framework.decorators import action
from .models import Habit, HabitAnswer, HabitCategory, HabitViolation
from .serializers import HabitSerializer, HabitAnswerSerializer, HabitCategorySerializer, HabitViolationSerializer
from .representors import HabitRepresentor, HabitAnswerRepresentor, HabitCategoryRepresentor, HabitViolationRepresentor

# Create your views here.

class HabitViewSet(CustomViewSet):
    model_manager = Habit.objects
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    representor_class = HabitRepresentor
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def answers(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'answers')

class HabitAnswerViewSet(CustomViewSet):
    model_manager = HabitAnswer.objects
    queryset = HabitAnswer.objects.all()
    serializer_class = HabitAnswerSerializer
    representor_class = HabitAnswerRepresentor

    @action(detail=True, methods=['get'])
    def violations(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'violations')

class HabitCategoryViewSet(CustomViewSet):
    model_manager = HabitCategory.objects
    queryset = HabitCategory.objects.all()
    serializer_class = HabitCategorySerializer
    representor_class = HabitCategoryRepresentor
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def habits(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'habits')

class HabitViolationViewSet(CustomViewSet):
    model_manager = HabitViolation.objects
    queryset = HabitViolation.objects.all()
    serializer_class = HabitViolationSerializer
    representor_class = HabitViolationRepresentor
