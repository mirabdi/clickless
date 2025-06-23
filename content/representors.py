from rest_framework import serializers
from core.representors import CustomRepresentor
from .models import (
    Article, ArticleCategory, ArticleDetail, ArticleViewHistory,
    Banner, EducationVideo, EducationVideoViewHistory,
    Meditation, MeditationHistory, Notice, PrivacyPolicy, Term,
    ConfidentialTerm, Faq, MedicalDevice
)

class ArticleRepresentor(CustomRepresentor):
    class Meta:
        model = Article
        fields = ['id', 'title', 'orders', 'category', 'created_at', 'deleted_at',
                 'details', 'view_histories', 'pain_answers']

class ArticleCategoryRepresentor(CustomRepresentor):
    class Meta:
        model = ArticleCategory
        fields = ['id', 'name', 'orders', 'is_common', 'created_at', 'deleted_at',
                 'articles', 'pain_answers']

class ArticleDetailRepresentor(CustomRepresentor):
    class Meta:
        model = ArticleDetail
        fields = ['id', 'article', 'content', 'image', 'orders', 'title', 'created_at', 'deleted_at']

class ArticleViewHistoryRepresentor(CustomRepresentor):
    class Meta:
        model = ArticleViewHistory
        fields = ['id', 'article', 'user', 'created_at', 'deleted_at']

class BannerRepresentor(CustomRepresentor):
    class Meta:
        model = Banner
        fields = ['id', 'image', 'background_color', 'orders', 'route', 'title', 'subtitle', 
                 'index', 'background_color_swatch', 'created_at', 'deleted_at']

class EducationVideoRepresentor(CustomRepresentor):
    class Meta:
        model = EducationVideo
        fields = ['id', 'url', 'title', 'content', 'orders', 'created_at', 'deleted_at',
                 'view_histories']

class EducationVideoViewHistoryRepresentor(CustomRepresentor):
    class Meta:
        model = EducationVideoViewHistory
        fields = ['id', 'user', 'video', 'created_at', 'deleted_at']

class MeditationRepresentor(CustomRepresentor):
    class Meta:
        model = Meditation
        fields = ['id', 'url', 'title', 'orders', 'type', 'created_at', 'deleted_at',
                 'histories']

class MeditationHistoryRepresentor(CustomRepresentor):
    class Meta:
        model = MeditationHistory
        fields = ['id', 'meditation', 'user', 'created_at']

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

class ConfidentialTermRepresentor(CustomRepresentor):
    class Meta:
        model = ConfidentialTerm
        fields = ['id', 'content', 'created_at', 'deleted_at', 'type']

class FaqRepresentor(CustomRepresentor):
    class Meta:
        model = Faq
        fields = ['id', 'created_at', 'deleted_at', 'answer', 'orders', 'question']

class MedicalDeviceRepresentor(CustomRepresentor):
    class Meta:
        model = MedicalDevice
        fields = ['id', 'content', 'is_markdown', 'label', 'orders', 'created_at', 'deleted_at'] 