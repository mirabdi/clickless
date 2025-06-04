from core.representors import CustomRepresentor
from .models import (
    Survey, SurveyAnswer, SurveyPainAnswer, SurveyPainAreaDetail,
    SurveyQuestion, SurveyQuestionCategory, SurveyQuestionType,
    SurveyQuestionTypeDetail
)

class SurveyRepresentor(CustomRepresentor):
    class Meta:
        model = Survey
        fields = ['id', 'name', 'explanation', 'is_pain', 'orders', 'created_at', 'deleted_at', 'type']

class SurveyAnswerRepresentor(CustomRepresentor):
    class Meta:
        model = SurveyAnswer
        fields = ['id', 'user_id', 'question_id', 'value', 'created_at', 'week']

class SurveyPainAnswerRepresentor(CustomRepresentor):
    class Meta:
        model = SurveyPainAnswer
        fields = ['id', 'user_id', 'content', 'created_at', 'week']

class SurveyPainAreaDetailRepresentor(CustomRepresentor):
    class Meta:
        model = SurveyPainAreaDetail
        fields = ['id', 'survey_pain_answer_id', 'area_id', 'value', 'created_at', 'deleted_at']

class SurveyQuestionRepresentor(CustomRepresentor):
    class Meta:
        model = SurveyQuestion
        fields = ['id', 'type_id', 'question_category_id', 'name', 'orders', 'created_at', 'deleted_at', 'question_category', 'survey_id']

class SurveyQuestionCategoryRepresentor(CustomRepresentor):
    class Meta:
        model = SurveyQuestionCategory
        fields = ['id', 'survey_id', 'name', 'orders', 'created_at', 'deleted_at']

class SurveyQuestionTypeRepresentor(CustomRepresentor):
    class Meta:
        model = SurveyQuestionType
        fields = ['id', 'type', 'created_at', 'deleted_at']

class SurveyQuestionTypeDetailRepresentor(CustomRepresentor):
    class Meta:
        model = SurveyQuestionTypeDetail
        fields = ['id', 'type_id', 'name', 'orders', 'created_at', 'deleted_at'] 