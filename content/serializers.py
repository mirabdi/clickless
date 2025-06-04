from rest_framework import serializers
from core.serializers import CustomSerializer
from .models import (
    Article, ArticleCategory, ArticleDetail, ArticleViewHistory,
    Banner, EducationVideo, EducationVideoViewHistory,
    Meditation, MeditationHistory, Notice, PrivacyPolicy, Term
)

class ArticleSerializer(CustomSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'orders', 'category_id', 'created_at', 'deleted_at']

class ArticleCategorySerializer(CustomSerializer):
    class Meta:
        model = ArticleCategory
        fields = ['id', 'name', 'orders', 'is_common', 'created_at', 'deleted_at']

class ArticleDetailSerializer(CustomSerializer):
    class Meta:
        model = ArticleDetail
        fields = ['id', 'article_id', 'content', 'image', 'orders', 'title', 'created_at', 'deleted_at']

class ArticleViewHistorySerializer(CustomSerializer):
    class Meta:
        model = ArticleViewHistory
        fields = ['id', 'article_id', 'user_id', 'created_at', 'deleted_at']

class BannerSerializer(CustomSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'image', 'background_color', 'orders', 'route', 'title', 'subtitle', 
                 'index', 'background_color_swatch', 'created_at', 'deleted_at']

class EducationVideoSerializer(CustomSerializer):
    class Meta:
        model = EducationVideo
        fields = ['id', 'url', 'title', 'content', 'orders', 'created_at', 'deleted_at']

class EducationVideoViewHistorySerializer(CustomSerializer):
    class Meta:
        model = EducationVideoViewHistory
        fields = ['id', 'user_id', 'video_id', 'created_at', 'deleted_at']

class MeditationSerializer(CustomSerializer):
    class Meta:
        model = Meditation
        fields = ['id', 'url', 'title', 'orders', 'type', 'created_at', 'deleted_at']

class MeditationHistorySerializer(CustomSerializer):
    class Meta:
        model = MeditationHistory
        fields = ['id', 'meditation_id', 'user_id', 'created_at']

class NoticeSerializer(CustomSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']

class PrivacyPolicySerializer(CustomSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']

class TermSerializer(CustomSerializer):
    class Meta:
        model = Term
        fields = ['id', 'title', 'content', 'created_at', 'updated_at'] 