from django.db import models
from core.models import CustomModel
from pain_management.models import PainArea
from users.models import User

# Create your models here.

class Survey(CustomModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    explanation = models.CharField(max_length=50)
    is_pain = models.IntegerField()
    orders = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    type = models.CharField(max_length=30)

    class Meta:
        
        db_table = 'v2_survey'

    def __str__(self):
        return f"{self.name} ({self.type})"

class Answer(CustomModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id', related_name='answers')
    question = models.ForeignKey('Question', models.DO_NOTHING, db_column='question_id', related_name='answers')
    value = models.IntegerField()
    created_at = models.DateTimeField()
    week = models.IntegerField()

    class Meta:
        
        db_table = 'v2_survey_answer'

    def __str__(self):
        return f"Answer {self.id} - User: {self.user.email}, Question: {self.question.name}, Value: {self.value}"

class PainAnswer(CustomModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id', related_name='pain_answers')
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    week = models.IntegerField()

    class Meta:
        
        db_table = 'v2_survey_pain_answer'

    def __str__(self):
        return f"Pain Answer {self.id} - User: {self.user.email}, Content: {self.content[:50]}"

class PainAreaDetail(CustomModel):
    id = models.BigAutoField(primary_key=True)
    survey_pain_answer = models.ForeignKey(PainAnswer, models.DO_NOTHING, related_name='pain_area_details')
    value = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_survey_pain_area_detail'

    def __str__(self):
        return f"Pain Area Detail {self.id} - Value: {self.value}"

class Question(CustomModel):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey('QuestionType', models.DO_NOTHING, related_name='questions')
    question_category = models.ForeignKey('QuestionCategory', models.DO_NOTHING, db_column='question_category_id', related_name='questions')
    name = models.CharField(max_length=255)
    orders = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    question_category_name = models.CharField(max_length=255, db_column='question_category')
    survey = models.ForeignKey(Survey, models.DO_NOTHING, db_column='survey_id', related_name='questions')

    class Meta:
        
        db_table = 'v2_survey_question'

    def __str__(self):
        return f"{self.name} ({self.question_category_name})"

class QuestionCategory(CustomModel):
    id = models.BigAutoField(primary_key=True)
    survey = models.ForeignKey(Survey, models.DO_NOTHING, related_name='question_categories')
    name = models.CharField(max_length=255)
    orders = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_survey_question_category'

    def __str__(self):
        return f"{self.name} (Survey: {self.survey.name})"

class QuestionType(CustomModel):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_survey_question_type'

    def __str__(self):
        return self.type

class QuestionTypeDetail(CustomModel):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey(QuestionType, models.DO_NOTHING, related_name='type_details')
    name = models.CharField(max_length=50)
    orders = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_survey_question_type_detail'

    def __str__(self):
        return f"{self.name} ({self.type.type})"

class Diary(CustomModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id', related_name='diary_entries')
    question = models.ForeignKey('DiaryQuestion', models.DO_NOTHING, db_column='question_id', related_name='diary_entries')
    value = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_diary'

    def __str__(self):
        return f"Diary Entry {self.id} - User: {self.user.email}, Question: {self.question.name}, Value: {self.value}"

class DiaryQuestion(CustomModel):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey('DiaryQuestionCategory', models.DO_NOTHING, related_name='questions')
    type = models.ForeignKey('DiaryQuestionType', models.DO_NOTHING, related_name='questions')
    name = models.CharField(max_length=255)
    orders = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    enum_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'v2_diary_question'

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class DiaryQuestionCategory(CustomModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    orders = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_diary_question_category'

    def __str__(self):
        return self.name

class DiaryQuestionType(CustomModel):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_diary_question_type'

    def __str__(self):
        return self.type

class DiaryQuestionTypeDetail(CustomModel):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey(DiaryQuestionType, models.DO_NOTHING, related_name='type_details')
    name = models.CharField(max_length=50)
    orders = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        
        db_table = 'v2_diary_question_type_detail'

    def __str__(self):
        return f"{self.name} ({self.type.type})"
