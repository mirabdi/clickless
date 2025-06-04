from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ArticleViewSet, ArticleCategoryViewSet, ArticleDetailViewSet,
    ArticleViewHistoryViewSet, BannerViewSet, EducationVideoViewSet,
    EducationVideoViewHistoryViewSet, MeditationViewSet,
    MeditationHistoryViewSet, NoticeViewSet, PrivacyPolicyViewSet,
    TermViewSet
)

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'article-categories', ArticleCategoryViewSet)
router.register(r'article-details', ArticleDetailViewSet)
router.register(r'article-view-histories', ArticleViewHistoryViewSet)
router.register(r'banners', BannerViewSet)
router.register(r'education-videos', EducationVideoViewSet)
router.register(r'education-video-view-histories', EducationVideoViewHistoryViewSet)
router.register(r'meditations', MeditationViewSet)
router.register(r'meditation-histories', MeditationHistoryViewSet)
router.register(r'notices', NoticeViewSet)
router.register(r'privacy-policies', PrivacyPolicyViewSet)
router.register(r'terms', TermViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 