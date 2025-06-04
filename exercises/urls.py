from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, ExerciseHistoryViewSet, ExerciseTimeViewSet

router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet)
router.register(r'exercise-histories', ExerciseHistoryViewSet)
router.register(r'exercise-times', ExerciseTimeViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 