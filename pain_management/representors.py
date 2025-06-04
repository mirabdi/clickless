from rest_framework import serializers
from core.representors import CustomRepresentor
from .models import (
    Pain, PainAnswer, PainArea, PainAreaDetail,
    PainCategory, PainFeedback, PainQuestion
)

class PainRepresentor(CustomRepresentor):
    class Meta:
        model = Pain
        fields = ['id', 'answer_id', 'category_id', 'content', 'created_at', 'deleted_at', 'user_id', 'feedback_id']

class PainAnswerRepresentor(CustomRepresentor):
    class Meta:
        model = PainAnswer
        fields = ['id', 'name', 'orders', 'category_id', 'article_category_id', 'has_text_area', 'created_at', 'deleted_at']

class PainAreaRepresentor(CustomRepresentor):
    class Meta:
        model = PainArea
        fields = ['id', 'name', 'is_right', 'x', 'y', 'created_at', 'deleted_at']

class PainAreaDetailRepresentor(CustomRepresentor):
    class Meta:
        model = PainAreaDetail
        fields = ['id', 'area_id', 'value', 'pain_id', 'created_at', 'deleted_at']

class PainCategoryRepresentor(CustomRepresentor):
    class Meta:
        model = PainCategory
        fields = ['id', 'name', 'orders', 'question_id', 'created_at', 'deleted_at']

class PainFeedbackRepresentor(CustomRepresentor):
    class Meta:
        model = PainFeedback
        fields = ['id', 'content', 'category_id', 'created_at', 'deleted_at']

class PainQuestionRepresentor(CustomRepresentor):
    class Meta:
        model = PainQuestion
        fields = ['id', 'name', 'created_at', 'deleted_at'] 