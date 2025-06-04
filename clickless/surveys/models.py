from django.db import models

# Create your models here.

class Survey(models.Model):
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

class SurveyAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    question_id = models.BigIntegerField()
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    week = models.IntegerField()

    class Meta:
        db_table = 'v2_survey_answer'

class SurveyPainAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    week = models.IntegerField()

    class Meta:
        db_table = 'v2_survey_pain_answer'

class SurveyPainAreaDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    survey_pain_answer_id = models.BigIntegerField()
    area_id = models.BigIntegerField()
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_survey_pain_area_detail'

class SurveyQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_id = models.BigIntegerField()
    question_category_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    orders = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    question_category = models.CharField(max_length=255)
    survey_id = models.IntegerField()

    class Meta:
        db_table = 'v2_survey_question'

class SurveyQuestionCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    survey_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    orders = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_survey_question_category'

class SurveyQuestionType(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_survey_question_type'

class SurveyQuestionTypeDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    orders = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_survey_question_type_detail'
