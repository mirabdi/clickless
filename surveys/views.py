from django.shortcuts import render
from core.views import CustomViewSet
from rest_framework.decorators import action
from .models import (
    Survey, Answer, PainAnswer, PainAreaDetail,
    Question, QuestionCategory, QuestionType,
    QuestionTypeDetail, Diary, DiaryQuestion, DiaryQuestionCategory,
    DiaryQuestionType, DiaryQuestionTypeDetail
)
from .serializers import (
    SurveySerializer, AnswerSerializer, PainAnswerSerializer,
    PainAreaDetailSerializer, QuestionSerializer,
    QuestionCategorySerializer, QuestionTypeSerializer,
    QuestionTypeDetailSerializer, DiarySerializer, DiaryQuestionSerializer,
    DiaryQuestionCategorySerializer, DiaryQuestionTypeSerializer,
    DiaryQuestionTypeDetailSerializer
)
from .representors import (
    SurveyRepresentor, AnswerRepresentor, PainAnswerRepresentor,
    PainAreaDetailRepresentor, QuestionRepresentor,
    QuestionCategoryRepresentor, QuestionTypeRepresentor,
    QuestionTypeDetailRepresentor, DiaryRepresentor, DiaryQuestionRepresentor,
    DiaryQuestionCategoryRepresentor, DiaryQuestionTypeRepresentor,
    DiaryQuestionTypeDetailRepresentor
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
    def question_categories(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'question_categories')
    
    @action(detail=True, methods=['get'])
    def answers(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'answers')
    
    @action(detail=True, methods=['get'], url_path='questions')
    def questions(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'questions')
    
    @action(detail=True, methods=['get'], url_path='question_categories')
    def question_categories(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'question_categories')

class AnswerViewSet(CustomViewSet):
    model_manager = Answer.objects
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    representor_class = AnswerRepresentor
    permission_classes = []
    
    search_fields = ['user_id', 'question_id', 'week']
    limit = 20

class PainAnswerViewSet(CustomViewSet):
    model_manager = PainAnswer.objects
    queryset = PainAnswer.objects.all()
    serializer_class = PainAnswerSerializer
    representor_class = PainAnswerRepresentor
    permission_classes = []
    
    search_fields = ['user_id', 'week']
    limit = 20

    @action(detail=True, methods=['get'])
    def pain_area_details(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'pain_area_details')

class PainAreaDetailViewSet(CustomViewSet):
    model_manager = PainAreaDetail.objects
    queryset = PainAreaDetail.objects.all()
    serializer_class = PainAreaDetailSerializer
    representor_class = PainAreaDetailRepresentor
    permission_classes = []
    
    search_fields = ['pain_answer_id', 'area_id']
    limit = 20

class QuestionViewSet(CustomViewSet):
    model_manager = Question.objects
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    representor_class = QuestionRepresentor
    permission_classes = []
    
    search_fields = ['name', 'question_category', 'id']
    limit = 20

    @action(detail=True, methods=['get'])
    def answers(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'answers')

class QuestionCategoryViewSet(CustomViewSet):
    model_manager = QuestionCategory.objects
    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategorySerializer
    representor_class = QuestionCategoryRepresentor
    permission_classes = []
    
    search_fields = ['name', 'id']
    limit = 20

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'questions')

class QuestionTypeViewSet(CustomViewSet):
    model_manager = QuestionType.objects
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer
    representor_class = QuestionTypeRepresentor
    permission_classes = []
    
    search_fields = ['type']
    limit = 20

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'questions')

    @action(detail=True, methods=['get'])
    def type_details(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'type_details')

class QuestionTypeDetailViewSet(CustomViewSet):
    model_manager = QuestionTypeDetail.objects
    queryset = QuestionTypeDetail.objects.all()
    serializer_class = QuestionTypeDetailSerializer
    representor_class = QuestionTypeDetailRepresentor
    permission_classes = []
    
    search_fields = ['name', 'type_id']
    limit = 20

class DiaryViewSet(CustomViewSet):
    model_manager = Diary.objects
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    representor_class = DiaryRepresentor
    permission_classes = []
    
    search_fields = ['user_id', 'question_id']
    limit = 20

class DiaryQuestionViewSet(CustomViewSet):
    model_manager = DiaryQuestion.objects
    queryset = DiaryQuestion.objects.all()
    serializer_class = DiaryQuestionSerializer
    representor_class = DiaryQuestionRepresentor
    permission_classes = []
    
    search_fields = ['name', 'category_id', 'type_id']
    limit = 20

    @action(detail=True, methods=['get'])
    def diary_entries(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'diary_entries')

class DiaryQuestionCategoryViewSet(CustomViewSet):
    model_manager = DiaryQuestionCategory.objects
    queryset = DiaryQuestionCategory.objects.all()
    serializer_class = DiaryQuestionCategorySerializer
    representor_class = DiaryQuestionCategoryRepresentor
    permission_classes = []
    
    search_fields = ['name']
    limit = 20

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'questions')

class DiaryQuestionTypeViewSet(CustomViewSet):
    model_manager = DiaryQuestionType.objects
    queryset = DiaryQuestionType.objects.all()
    serializer_class = DiaryQuestionTypeSerializer
    representor_class = DiaryQuestionTypeRepresentor
    permission_classes = []
    
    search_fields = ['type']
    limit = 20

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'questions')

    @action(detail=True, methods=['get'])
    def type_details(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'type_details')

class DiaryQuestionTypeDetailViewSet(CustomViewSet):
    model_manager = DiaryQuestionTypeDetail.objects
    queryset = DiaryQuestionTypeDetail.objects.all()
    serializer_class = DiaryQuestionTypeDetailSerializer
    representor_class = DiaryQuestionTypeDetailRepresentor
    permission_classes = []
    
    search_fields = ['name', 'type_id']
    limit = 20
