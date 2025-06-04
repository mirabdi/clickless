from django.db import models
from core.models import CustomModel
from pain_management.models import PainArea

# Create your models here.

class Survey(CustomModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    explanation = models.CharField(max_length=50)
    is_pain = models.BooleanField()
    orders = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=30)

    class Meta:
        db_table = 'v2_survey'

class SurveyAnswer(CustomModel):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    question = models.ForeignKey('SurveyQuestion', on_delete=models.CASCADE, db_column='question_id')
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    week = models.IntegerField()

    class Meta:
        db_table = 'v2_survey_answer'

class SurveyPainAnswer(CustomModel):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    week = models.IntegerField()

    class Meta:
        db_table = 'v2_survey_pain_answer'

class SurveyPainAreaDetail(CustomModel):
    id = models.BigAutoField(primary_key=True)
    survey_pain_answer = models.ForeignKey(SurveyPainAnswer, on_delete=models.CASCADE, db_column='survey_pain_answer_id')
    area = models.ForeignKey(PainArea, on_delete=models.CASCADE, db_column='area_id')
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_survey_pain_area_detail'

class SurveyQuestion(CustomModel):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey('SurveyQuestionType', on_delete=models.CASCADE, db_column='type_id')
    question_category = models.ForeignKey('SurveyQuestionCategory', on_delete=models.CASCADE, db_column='question_category_id')
    name = models.CharField(max_length=255)
    orders = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    question_category_name = models.CharField(max_length=255, db_column='question_category')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, db_column='survey_id')

    class Meta:
        db_table = 'v2_survey_question'

class SurveyQuestionCategory(CustomModel):
    id = models.BigAutoField(primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, db_column='survey_id')
    name = models.CharField(max_length=255)
    orders = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_survey_question_category'

class SurveyQuestionType(CustomModel):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_survey_question_type'

class SurveyQuestionTypeDetail(CustomModel):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey(SurveyQuestionType, on_delete=models.CASCADE, db_column='type_id')
    name = models.CharField(max_length=50)
    orders = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_survey_question_type_detail'
