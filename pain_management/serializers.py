from rest_framework import serializers
from core.serializers import CustomSerializer
from .models import (
    Pain, PainAnswer, PainArea, PainAreaDetail,
    PainCategory, PainFeedback, PainQuestion
)

class PainSerializer(CustomSerializer):
    class Meta:
        model = Pain
        fields = ['id', 'answer_id', 'category_id', 'content', 'created_at', 'deleted_at', 'user_id', 'feedback_id']

class PainAnswerSerializer(CustomSerializer):
    class Meta:
        model = PainAnswer
        fields = ['id', 'name', 'orders', 'category_id', 'article_category_id', 'has_text_area', 'created_at', 'deleted_at']

class PainAreaSerializer(CustomSerializer):
    class Meta:
        model = PainArea
        fields = ['id', 'name', 'is_right', 'x', 'y', 'created_at', 'deleted_at']

class PainAreaDetailSerializer(CustomSerializer):
    class Meta:
        model = PainAreaDetail
        fields = ['id', 'area_id', 'value', 'pain_id', 'created_at', 'deleted_at']

class PainCategorySerializer(CustomSerializer):
    class Meta:
        model = PainCategory
        fields = ['id', 'name', 'orders', 'question_id', 'created_at', 'deleted_at']

class PainFeedbackSerializer(CustomSerializer):
    class Meta:
        model = PainFeedback
        fields = ['id', 'content', 'category_id', 'created_at', 'deleted_at']

class PainQuestionSerializer(CustomSerializer):
    class Meta:
        model = PainQuestion
        fields = ['id', 'name', 'created_at', 'deleted_at'] 