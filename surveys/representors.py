from core.representors import CustomRepresentor
from .models import (
    Survey, Answer, PainAnswer, PainAreaDetail,
    Question, QuestionCategory, QuestionType,
    QuestionTypeDetail, Diary, DiaryQuestion, DiaryQuestionCategory,
    DiaryQuestionType, DiaryQuestionTypeDetail
)

class SurveyRepresentor(CustomRepresentor):
    class Meta:
        model = Survey
        fields = ['id', 'name', 'explanation', 'is_pain', 'orders', 'created_at', 'deleted_at', 'type',
                 'questions', 'question_categories']

class AnswerRepresentor(CustomRepresentor):
    class Meta:
        model = Answer
        fields = ['id', 'user', 'question', 'value', 'created_at', 'week']

class PainAnswerRepresentor(CustomRepresentor):
    class Meta:
        model = PainAnswer
        fields = ['id', 'user', 'content', 'created_at', 'week', 'pain_area_details']

class PainAreaDetailRepresentor(CustomRepresentor):
    class Meta:
        model = PainAreaDetail
        fields = ['id', 'pain_answer', 'area', 'value', 'created_at', 'deleted_at']

class QuestionRepresentor(CustomRepresentor):
    class Meta:
        model = Question
        fields = ['id', 'type', 'question_category', 'name', 'orders', 'created_at', 'deleted_at', 'question_category', 'survey', 'answers']

class QuestionCategoryRepresentor(CustomRepresentor):
    class Meta:
        model = QuestionCategory
        fields = ['id', 'survey', 'name', 'orders', 'created_at', 'deleted_at', 'questions']

class QuestionTypeRepresentor(CustomRepresentor):
    class Meta:
        model = QuestionType
        fields = ['id', 'type', 'created_at', 'deleted_at', 'questions', 'type_details']

class QuestionTypeDetailRepresentor(CustomRepresentor):
    class Meta:
        model = QuestionTypeDetail
        fields = ['id', 'type', 'name', 'orders', 'created_at', 'deleted_at']

class DiaryRepresentor(CustomRepresentor):
    class Meta:
        model = Diary
        fields = ['id', 'user', 'question', 'value', 'created_at', 'deleted_at']

class DiaryQuestionRepresentor(CustomRepresentor):
    class Meta:
        model = DiaryQuestion
        fields = ['id', 'category', 'type', 'name', 'orders', 'created_at', 'deleted_at', 'enum_name', 'diary_entries']

class DiaryQuestionCategoryRepresentor(CustomRepresentor):
    class Meta:
        model = DiaryQuestionCategory
        fields = ['id', 'name', 'orders', 'created_at', 'deleted_at', 'questions']

class DiaryQuestionTypeRepresentor(CustomRepresentor):
    class Meta:
        model = DiaryQuestionType
        fields = ['id', 'type', 'created_at', 'deleted_at', 'questions', 'type_details']

class DiaryQuestionTypeDetailRepresentor(CustomRepresentor):
    class Meta:
        model = DiaryQuestionTypeDetail
        fields = ['id', 'type', 'name', 'orders', 'created_at', 'deleted_at'] 