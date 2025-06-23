from django.shortcuts import render
from rest_framework import viewsets
from core.views import CustomViewSet
from rest_framework.decorators import action
from .models import (
    Pain, PainAnswer, PainArea, PainAreaDetail,
    PainCategory, PainFeedback, PainQuestion, PainArticle
)
from .serializers import (
    PainSerializer, PainAnswerSerializer, PainAreaSerializer,
    PainAreaDetailSerializer, PainCategorySerializer,
    PainFeedbackSerializer, PainQuestionSerializer, PainArticleSerializer
)
from .representors import (
    PainRepresentor, PainAnswerRepresentor, PainAreaRepresentor,
    PainAreaDetailRepresentor, PainCategoryRepresentor,
    PainFeedbackRepresentor, PainQuestionRepresentor, PainArticleRepresentor
)

# Create your views here.

class PainViewSet(CustomViewSet):
    model_manager = Pain.objects
    queryset = Pain.objects.all()
    serializer_class = PainSerializer
    representor_class = PainRepresentor
    search_fields = ['content']

    @action(detail=True, methods=['get'])
    def area_details(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'area_details')

    @action(detail=True, methods=['get'])
    def pain_articles(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'pain_articles')

class PainAnswerViewSet(CustomViewSet):
    model_manager = PainAnswer.objects
    queryset = PainAnswer.objects.all()
    serializer_class = PainAnswerSerializer
    representor_class = PainAnswerRepresentor
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def pain_records(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'pain_records')

class PainAreaViewSet(CustomViewSet):
    model_manager = PainArea.objects
    queryset = PainArea.objects.all()
    serializer_class = PainAreaSerializer
    representor_class = PainAreaRepresentor
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def area_details(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'area_details')

class PainAreaDetailViewSet(CustomViewSet):
    model_manager = PainAreaDetail.objects
    queryset = PainAreaDetail.objects.all()
    serializer_class = PainAreaDetailSerializer
    representor_class = PainAreaDetailRepresentor

class PainCategoryViewSet(CustomViewSet):
    model_manager = PainCategory.objects
    queryset = PainCategory.objects.all()
    serializer_class = PainCategorySerializer
    representor_class = PainCategoryRepresentor
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def pain_records(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'pain_records')

    @action(detail=True, methods=['get'])
    def pain_answers(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'pain_answers')

    @action(detail=True, methods=['get'])
    def pain_feedbacks(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'pain_feedbacks')

class PainFeedbackViewSet(CustomViewSet):
    model_manager = PainFeedback.objects
    queryset = PainFeedback.objects.all()
    serializer_class = PainFeedbackSerializer
    representor_class = PainFeedbackRepresentor
    search_fields = ['content']

    @action(detail=True, methods=['get'])
    def pain_records(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'pain_records')

class PainQuestionViewSet(CustomViewSet):
    model_manager = PainQuestion.objects
    queryset = PainQuestion.objects.all()
    serializer_class = PainQuestionSerializer
    representor_class = PainQuestionRepresentor
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def pain_categories(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'pain_categories')

class PainArticleViewSet(CustomViewSet):
    model_manager = PainArticle.objects
    queryset = PainArticle.objects.all()
    serializer_class = PainArticleSerializer
    representor_class = PainArticleRepresentor
    permission_classes = []
    
    search_fields = ['article_id', 'pain_id']
    limit = 20
