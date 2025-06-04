from core.serializers import CustomSerializer
from .models import (
    Survey, SurveyAnswer, SurveyPainAnswer, SurveyPainAreaDetail,
    SurveyQuestion, SurveyQuestionCategory, SurveyQuestionType,
    SurveyQuestionTypeDetail
)

class SurveySerializer(CustomSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'name', 'explanation', 'is_pain', 'orders', 'created_at', 'deleted_at', 'type']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class SurveyAnswerSerializer(CustomSerializer):
    class Meta:
        model = SurveyAnswer
        fields = ['id', 'user_id', 'question_id', 'value', 'created_at', 'week']
        read_only_fields = ['id', 'created_at']

class SurveyPainAnswerSerializer(CustomSerializer):
    class Meta:
        model = SurveyPainAnswer
        fields = ['id', 'user_id', 'content', 'created_at', 'week']
        read_only_fields = ['id', 'created_at']

class SurveyPainAreaDetailSerializer(CustomSerializer):
    class Meta:
        model = SurveyPainAreaDetail
        fields = ['id', 'survey_pain_answer_id', 'area_id', 'value', 'created_at', 'deleted_at']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class SurveyQuestionSerializer(CustomSerializer):
    class Meta:
        model = SurveyQuestion
        fields = ['id', 'type_id', 'question_category_id', 'name', 'orders', 'created_at', 'deleted_at', 'question_category', 'survey_id']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class SurveyQuestionCategorySerializer(CustomSerializer):
    class Meta:
        model = SurveyQuestionCategory
        fields = ['id', 'survey_id', 'name', 'orders', 'created_at', 'deleted_at']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class SurveyQuestionTypeSerializer(CustomSerializer):
    class Meta:
        model = SurveyQuestionType
        fields = ['id', 'type', 'created_at', 'deleted_at']
        read_only_fields = ['id', 'created_at', 'deleted_at']

class SurveyQuestionTypeDetailSerializer(CustomSerializer):
    class Meta:
        model = SurveyQuestionTypeDetail
        fields = ['id', 'type_id', 'name', 'orders', 'created_at', 'deleted_at']
        read_only_fields = ['id', 'created_at', 'deleted_at'] 