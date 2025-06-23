from rest_framework import serializers
from core.representors import CustomRepresentor
from .models import (
    Pain, PainAnswer, PainArea, PainAreaDetail,
    PainCategory, PainFeedback, PainQuestion, PainArticle
)

class PainRepresentor(CustomRepresentor):
    class Meta:
        model = Pain
        fields = ['id', 'answer', 'category', 'content', 'created_at', 'deleted_at', 'user', 'feedback',
                 'area_details', 'pain_articles']

class PainAnswerRepresentor(CustomRepresentor):
    class Meta:
        model = PainAnswer
        fields = ['id', 'name', 'orders', 'category', 'article_category', 'has_text_area', 'created_at', 'deleted_at',
                 'pain_records']

class PainAreaRepresentor(CustomRepresentor):
    class Meta:
        model = PainArea
        fields = ['id', 'name', 'is_right', 'x', 'y', 'created_at', 'deleted_at', 'area_details']

class PainAreaDetailRepresentor(CustomRepresentor):
    class Meta:
        model = PainAreaDetail
        fields = ['id', 'area', 'value', 'pain', 'created_at', 'deleted_at']

class PainCategoryRepresentor(CustomRepresentor):
    class Meta:
        model = PainCategory
        fields = ['id', 'name', 'orders', 'question', 'created_at', 'deleted_at',
                 'pain_records', 'pain_answers', 'pain_feedbacks']

class PainFeedbackRepresentor(CustomRepresentor):
    class Meta:
        model = PainFeedback
        fields = ['id', 'content', 'category', 'created_at', 'deleted_at', 'pain_records']

class PainQuestionRepresentor(CustomRepresentor):
    class Meta:
        model = PainQuestion
        fields = ['id', 'name', 'created_at', 'deleted_at', 'pain_categories']

class PainArticleRepresentor(CustomRepresentor):
    class Meta:
        model = PainArticle
        fields = ['id', 'article', 'created_at', 'deleted_at', 'pain'] 