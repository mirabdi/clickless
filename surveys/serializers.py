from core.serializers import CustomSerializer
from .models import (
    Survey, Answer, PainAnswer, PainAreaDetail,
    Question, QuestionCategory, QuestionType,
    QuestionTypeDetail, Diary, DiaryQuestion, DiaryQuestionCategory,
    DiaryQuestionType, DiaryQuestionTypeDetail
)

class SurveySerializer(CustomSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'name', 'explanation', 'is_pain', 'orders', 'created_at', 'deleted_at', 'type']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class AnswerSerializer(CustomSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'user', 'question', 'value', 'created_at', 'week']
        read_only_fields = ['id', 'created_at']

class PainAnswerSerializer(CustomSerializer):
    class Meta:
        model = PainAnswer
        fields = ['id', 'user', 'content', 'created_at', 'week']
        read_only_fields = ['id', 'created_at']

class PainAreaDetailSerializer(CustomSerializer):
    class Meta:
        model = PainAreaDetail
        fields = ['id', 'pain_answer', 'area', 'value', 'created_at', 'deleted_at']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class QuestionSerializer(CustomSerializer):
    class Meta:
        model = Question
        fields = ['id', 'type', 'question_category', 'name', 'orders', 'created_at', 'deleted_at', 'question_category', 'survey']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class QuestionCategorySerializer(CustomSerializer):
    class Meta:
        model = QuestionCategory
        fields = ['id', 'survey', 'name', 'orders', 'created_at', 'deleted_at']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class QuestionTypeSerializer(CustomSerializer):
    class Meta:
        model = QuestionType
        fields = ['id', 'type', 'created_at', 'deleted_at']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class QuestionTypeDetailSerializer(CustomSerializer):
    class Meta:
        model = QuestionTypeDetail
        fields = ['id', 'type', 'name', 'orders', 'created_at', 'deleted_at']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class DiarySerializer(CustomSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'user', 'question', 'value', 'created_at', 'deleted_at']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class DiaryQuestionSerializer(CustomSerializer):
    class Meta:
        model = DiaryQuestion
        fields = ['id', 'category', 'type', 'name', 'orders', 'created_at', 'deleted_at', 'enum_name']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class DiaryQuestionCategorySerializer(CustomSerializer):
    class Meta:
        model = DiaryQuestionCategory
        fields = ['id', 'name', 'orders', 'created_at', 'deleted_at']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class DiaryQuestionTypeSerializer(CustomSerializer):
    class Meta:
        model = DiaryQuestionType
        fields = ['id', 'type', 'created_at', 'deleted_at']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class DiaryQuestionTypeDetailSerializer(CustomSerializer):
    class Meta:
        model = DiaryQuestionTypeDetail
        fields = ['id', 'type', 'name', 'orders', 'created_at', 'deleted_at']
        read_only_fields = ['id', 'created_at', 'deleted_at'] 