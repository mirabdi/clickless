from rest_framework import serializers
from core.serializers import CustomSerializer
from .models import (
    Pain, PainAnswer, PainArea, PainAreaDetail,
    PainCategory, PainFeedback, PainQuestion, PainArticle
)

class PainSerializer(CustomSerializer):
    class Meta:
        model = Pain
        fields = ['id', 'answer', 'category', 'content', 'created_at', 'deleted_at', 'user', 'feedback']

class PainAnswerSerializer(CustomSerializer):
    class Meta:
        model = PainAnswer
        fields = ['id', 'name', 'orders', 'category', 'article_category', 'has_text_area', 'created_at', 'deleted_at']

class PainAreaSerializer(CustomSerializer):
    class Meta:
        model = PainArea
        fields = ['id', 'name', 'is_right', 'x', 'y', 'created_at', 'deleted_at']

class PainAreaDetailSerializer(CustomSerializer):
    class Meta:
        model = PainAreaDetail
        fields = ['id', 'area', 'value', 'pain', 'created_at', 'deleted_at']

class PainCategorySerializer(CustomSerializer):
    class Meta:
        model = PainCategory
        fields = ['id', 'name', 'orders', 'question', 'created_at', 'deleted_at']

class PainFeedbackSerializer(CustomSerializer):
    class Meta:
        model = PainFeedback
        fields = ['id', 'content', 'category', 'created_at', 'deleted_at']

class PainQuestionSerializer(CustomSerializer):
    class Meta:
        model = PainQuestion
        fields = ['id', 'name', 'created_at', 'deleted_at']

class PainArticleSerializer(CustomSerializer):
    class Meta:
        model = PainArticle
        fields = ['id', 'article', 'created_at', 'deleted_at', 'pain']
        read_only_fields = ['id', 'created_at', 'deleted_at'] 