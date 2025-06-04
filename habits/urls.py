from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, HabitAnswerViewSet, HabitCategoryViewSet, HabitViolationViewSet

router = DefaultRouter()
router.register(r'habits', HabitViewSet)
router.register(r'habit-answers', HabitAnswerViewSet)
router.register(r'habit-categories', HabitCategoryViewSet)
router.register(r'habit-violations', HabitViolationViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 