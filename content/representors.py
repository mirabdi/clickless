from rest_framework import serializers
from core.representors import CustomRepresentor
from .models import (
    Article, ArticleCategory, ArticleDetail, ArticleViewHistory,
    Banner, EducationVideo, EducationVideoViewHistory,
    Meditation, MeditationHistory, Notice, PrivacyPolicy, Term
)

class ArticleRepresentor(CustomRepresentor):
    class Meta:
        model = Article
        fields = ['id', 'title', 'orders', 'category_id', 'created_at', 'deleted_at']

class ArticleCategoryRepresentor(CustomRepresentor):
    class Meta:
        model = ArticleCategory
        fields = ['id', 'name', 'orders', 'is_common', 'created_at', 'deleted_at']

class ArticleDetailRepresentor(CustomRepresentor):
    class Meta:
        model = ArticleDetail
        fields = ['id', 'article_id', 'content', 'image', 'orders', 'title', 'created_at', 'deleted_at']

class ArticleViewHistoryRepresentor(CustomRepresentor):
    class Meta:
        model = ArticleViewHistory
        fields = ['id', 'article_id', 'user_id', 'created_at', 'deleted_at']

class BannerRepresentor(CustomRepresentor):
    class Meta:
        model = Banner
        fields = ['id', 'image', 'background_color', 'orders', 'route', 'title', 'subtitle', 
                 'index', 'background_color_swatch', 'created_at', 'deleted_at']

class EducationVideoRepresentor(CustomRepresentor):
    class Meta:
        model = EducationVideo
        fields = ['id', 'url', 'title', 'content', 'orders', 'created_at', 'deleted_at']

class EducationVideoViewHistoryRepresentor(CustomRepresentor):
    class Meta:
        model = EducationVideoViewHistory
        fields = ['id', 'user_id', 'video_id', 'created_at', 'deleted_at']

class MeditationRepresentor(CustomRepresentor):
    class Meta:
        model = Meditation
        fields = ['id', 'url', 'title', 'orders', 'type', 'created_at', 'deleted_at']

class MeditationHistoryRepresentor(CustomRepresentor):
    class Meta:
        model = MeditationHistory
        fields = ['id', 'meditation_id', 'user_id', 'created_at']

class NoticeRepresentor(CustomRepresentor):
    class Meta:
        model = Notice
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']

class PrivacyPolicyRepresentor(CustomRepresentor):
    class Meta:
        model = PrivacyPolicy
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']

class TermRepresentor(CustomRepresentor):
    class Meta:
        model = Term
        fields = ['id', 'title', 'content', 'created_at', 'updated_at'] 