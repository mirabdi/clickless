from django.db import models
from core.models import CustomModel

# Create your models here.

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=255)
    orders = models.IntegerField(null=True, blank=True)
    category_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'v2_article'

class ArticleCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=255)
    orders = models.IntegerField(null=True, blank=True)
    is_common = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = 'v2_article_category'

class ArticleDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.BigIntegerField()
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    image = models.CharField(max_length=255)
    orders = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=255)

    class Meta:
        db_table = 'v2_article_detail'

class ArticleViewHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    user_id = models.IntegerField()

    class Meta:
        db_table = 'v2_article_view_history'

class Banner(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=200)
    background_color = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    orders = models.IntegerField()
    route = models.CharField(max_length=20)
    deleted_at = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    index = models.IntegerField(null=True, blank=True, default=-1)
    background_color_swatch = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'v2_banner'

class EducationVideo(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    orders = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_education_video'

class EducationVideoViewHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    video_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'v2_education_video_view_history'

class Meditation(CustomModel):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=100)
    orders = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'v2_meditation'

class MeditationHistory(CustomModel):
    id = models.BigAutoField(primary_key=True)
    meditation_id = models.BigIntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'v2_meditation_history'

class Notice(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'v2_notice'

class PrivacyPolicy(CustomModel):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'v2_privacy_policy'

class Term(CustomModel):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'v2_term'
