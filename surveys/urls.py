from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SurveyViewSet, SurveyAnswerViewSet, SurveyPainAnswerViewSet,
    SurveyPainAreaDetailViewSet, SurveyQuestionViewSet,
    SurveyQuestionCategoryViewSet, SurveyQuestionTypeViewSet,
    SurveyQuestionTypeDetailViewSet
)

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'survey-answers', SurveyAnswerViewSet)
router.register(r'survey-pain-answers', SurveyPainAnswerViewSet)
router.register(r'survey-pain-area-details', SurveyPainAreaDetailViewSet)
router.register(r'survey-questions', SurveyQuestionViewSet)
router.register(r'survey-question-categories', SurveyQuestionCategoryViewSet)
router.register(r'survey-question-types', SurveyQuestionTypeViewSet)
router.register(r'survey-question-type-details', SurveyQuestionTypeDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 