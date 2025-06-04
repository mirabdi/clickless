from django.db import models
from core.models import CustomModel

# Create your models here.

class Pain(models.Model):
    id = models.BigAutoField(primary_key=True)
    answer_id = models.BigIntegerField(null=True, blank=True)
    category_id = models.BigIntegerField()
    content = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    user_id = models.IntegerField()
    feedback_id = models.BigIntegerField()

    class Meta:
        db_table = 'v2_pain'

class PainAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=50)
    orders = models.IntegerField(null=True, blank=True)
    category_id = models.BigIntegerField(null=True, blank=True)
    article_category_id = models.BigIntegerField()
    has_text_area = models.BooleanField()

    class Meta:
        db_table = 'v2_pain_answer'

class PainArea(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=15)
    is_right = models.BooleanField()
    x = models.FloatField()
    y = models.FloatField()

    class Meta:
        db_table = 'v2_pain_area'

class PainAreaDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    area_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    value = models.IntegerField()
    pain_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'v2_pain_area_detail'

class PainCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=50)
    orders = models.IntegerField(null=True, blank=True)
    question_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'v2_pain_category'

class PainFeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    category_id = models.BigIntegerField()

    class Meta:
        db_table = 'v2_pain_feedback'

class PainQuestion(CustomModel):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'v2_pain_question'
