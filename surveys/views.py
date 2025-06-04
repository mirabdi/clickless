from django.shortcuts import render
from core.views import CustomViewSet
from rest_framework.decorators import action
from .models import (
    Survey, SurveyAnswer, SurveyPainAnswer, SurveyPainAreaDetail,
    SurveyQuestion, SurveyQuestionCategory, SurveyQuestionType,
    SurveyQuestionTypeDetail
)
from .serializers import (
    SurveySerializer, SurveyAnswerSerializer, SurveyPainAnswerSerializer,
    SurveyPainAreaDetailSerializer, SurveyQuestionSerializer,
    SurveyQuestionCategorySerializer, SurveyQuestionTypeSerializer,
    SurveyQuestionTypeDetailSerializer
)
from .representors import (
    SurveyRepresentor, SurveyAnswerRepresentor, SurveyPainAnswerRepresentor,
    SurveyPainAreaDetailRepresentor, SurveyQuestionRepresentor,
    SurveyQuestionCategoryRepresentor, SurveyQuestionTypeRepresentor,
    SurveyQuestionTypeDetailRepresentor
)

# Create your views here.

class SurveyViewSet(CustomViewSet):
    model_manager = Survey.objects
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    representor_class = SurveyRepresentor
    permission_classes = []
    
    search_fields = ['name', 'type']
    limit = 20

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'questions')

class SurveyAnswerViewSet(CustomViewSet):
    model_manager = SurveyAnswer.objects
    queryset = SurveyAnswer.objects.all()
    serializer_class = SurveyAnswerSerializer
    representor_class = SurveyAnswerRepresentor
    permission_classes = []
    
    search_fields = ['user_id', 'question_id', 'week']
    limit = 20

class SurveyPainAnswerViewSet(CustomViewSet):
    model_manager = SurveyPainAnswer.objects
    queryset = SurveyPainAnswer.objects.all()
    serializer_class = SurveyPainAnswerSerializer
    representor_class = SurveyPainAnswerRepresentor
    permission_classes = []
    
    search_fields = ['user_id', 'week']
    limit = 20

    @action(detail=True, methods=['get'])
    def area_details(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'area_details')

class SurveyPainAreaDetailViewSet(CustomViewSet):
    model_manager = SurveyPainAreaDetail.objects
    queryset = SurveyPainAreaDetail.objects.all()
    serializer_class = SurveyPainAreaDetailSerializer
    representor_class = SurveyPainAreaDetailRepresentor
    permission_classes = []
    
    search_fields = ['survey_pain_answer_id', 'area_id']
    limit = 20

class SurveyQuestionViewSet(CustomViewSet):
    model_manager = SurveyQuestion.objects
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer
    representor_class = SurveyQuestionRepresentor
    permission_classes = []
    
    search_fields = ['name', 'question_category', 'survey_id']
    limit = 20

class SurveyQuestionCategoryViewSet(CustomViewSet):
    model_manager = SurveyQuestionCategory.objects
    queryset = SurveyQuestionCategory.objects.all()
    serializer_class = SurveyQuestionCategorySerializer
    representor_class = SurveyQuestionCategoryRepresentor
    permission_classes = []
    
    search_fields = ['name', 'survey_id']
    limit = 20

class SurveyQuestionTypeViewSet(CustomViewSet):
    model_manager = SurveyQuestionType.objects
    queryset = SurveyQuestionType.objects.all()
    serializer_class = SurveyQuestionTypeSerializer
    representor_class = SurveyQuestionTypeRepresentor
    permission_classes = []
    
    search_fields = ['type']
    limit = 20

    @action(detail=True, methods=['get'])
    def type_details(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'type_details')

class SurveyQuestionTypeDetailViewSet(CustomViewSet):
    model_manager = SurveyQuestionTypeDetail.objects
    queryset = SurveyQuestionTypeDetail.objects.all()
    serializer_class = SurveyQuestionTypeDetailSerializer
    representor_class = SurveyQuestionTypeDetailRepresentor
    permission_classes = []
    
    search_fields = ['name', 'type_id']
    limit = 20
