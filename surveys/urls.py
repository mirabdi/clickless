from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SurveyViewSet, AnswerViewSet, PainAnswerViewSet,
    PainAreaDetailViewSet, QuestionViewSet,
    QuestionCategoryViewSet, QuestionTypeViewSet,
    QuestionTypeDetailViewSet
)

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'survey-answers', AnswerViewSet)
router.register(r'survey-pain-answers', PainAnswerViewSet)
router.register(r'survey-pain-area-details', PainAreaDetailViewSet)
router.register(r'survey-questions', QuestionViewSet)
router.register(r'survey-question-categories', QuestionCategoryViewSet)
router.register(r'survey-question-types', QuestionTypeViewSet)
router.register(r'survey-question-type-details', QuestionTypeDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 