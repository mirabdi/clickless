from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PainViewSet, PainAnswerViewSet, PainAreaViewSet,
    PainAreaDetailViewSet, PainCategoryViewSet,
    PainFeedbackViewSet, PainQuestionViewSet
)

router = DefaultRouter()
router.register(r'pains', PainViewSet)
router.register(r'pain-answers', PainAnswerViewSet)
router.register(r'pain-areas', PainAreaViewSet)
router.register(r'pain-area-details', PainAreaDetailViewSet)
router.register(r'pain-categories', PainCategoryViewSet)
router.register(r'pain-feedbacks', PainFeedbackViewSet)
router.register(r'pain-questions', PainQuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 