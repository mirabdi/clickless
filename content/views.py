from django.shortcuts import render
from rest_framework import viewsets
from core.views import CustomViewSet
from rest_framework.decorators import action
from .models import (
    Article, ArticleCategory, ArticleDetail, ArticleViewHistory,
    Banner, EducationVideo, EducationVideoViewHistory,
    Meditation, MeditationHistory, Notice, PrivacyPolicy, Term,
    ConfidentialTerm, Faq, MedicalDevice
)
from .serializers import (
    ArticleSerializer, ArticleCategorySerializer, ArticleDetailSerializer,
    ArticleViewHistorySerializer, BannerSerializer, EducationVideoSerializer,
    EducationVideoViewHistorySerializer, MeditationSerializer,
    MeditationHistorySerializer, NoticeSerializer, PrivacyPolicySerializer,
    TermSerializer, ConfidentialTermSerializer, FaqSerializer, MedicalDeviceSerializer
)
from .representors import (
    ArticleRepresentor, ArticleCategoryRepresentor, ArticleDetailRepresentor,
    ArticleViewHistoryRepresentor, BannerRepresentor, EducationVideoRepresentor,
    EducationVideoViewHistoryRepresentor, MeditationRepresentor,
    MeditationHistoryRepresentor, NoticeRepresentor, PrivacyPolicyRepresentor,
    TermRepresentor, ConfidentialTermRepresentor, FaqRepresentor, MedicalDeviceRepresentor
)

# Create your views here.

class ArticleViewSet(CustomViewSet):
    model_manager = Article.objects
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    representor_class = ArticleRepresentor
    search_fields = ['title']

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'details')

    @action(detail=True, methods=['get'])
    def view_histories(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'view_histories')

    @action(detail=True, methods=['get'])
    def pain_answers(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'pain_answers')

class ArticleCategoryViewSet(CustomViewSet):
    model_manager = ArticleCategory.objects
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer
    representor_class = ArticleCategoryRepresentor
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def articles(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'articles')

    @action(detail=True, methods=['get'])
    def pain_answers(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'pain_answers')

class ArticleDetailViewSet(CustomViewSet):
    model_manager = ArticleDetail.objects
    queryset = ArticleDetail.objects.all()
    serializer_class = ArticleDetailSerializer
    representor_class = ArticleDetailRepresentor
    search_fields = ['title', 'content']

class ArticleViewHistoryViewSet(CustomViewSet):
    model_manager = ArticleViewHistory.objects
    queryset = ArticleViewHistory.objects.all()
    serializer_class = ArticleViewHistorySerializer
    representor_class = ArticleViewHistoryRepresentor

class BannerViewSet(CustomViewSet):
    model_manager = Banner.objects
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    representor_class = BannerRepresentor
    search_fields = ['title', 'subtitle']

class EducationVideoViewSet(CustomViewSet):
    model_manager = EducationVideo.objects
    queryset = EducationVideo.objects.all()
    serializer_class = EducationVideoSerializer
    representor_class = EducationVideoRepresentor
    search_fields = ['title', 'content']

    @action(detail=True, methods=['get'])
    def view_histories(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'view_histories')

class EducationVideoViewHistoryViewSet(CustomViewSet):
    model_manager = EducationVideoViewHistory.objects
    queryset = EducationVideoViewHistory.objects.all()
    serializer_class = EducationVideoViewHistorySerializer
    representor_class = EducationVideoViewHistoryRepresentor

class MeditationViewSet(CustomViewSet):
    model_manager = Meditation.objects
    queryset = Meditation.objects.all()
    serializer_class = MeditationSerializer
    representor_class = MeditationRepresentor
    search_fields = ['title']

    @action(detail=True, methods=['get'])
    def histories(self, request, pk=None):
        instance = self.get_object(pk)
        return self._related_field_action(request, instance, 'histories')

class MeditationHistoryViewSet(CustomViewSet):
    model_manager = MeditationHistory.objects
    queryset = MeditationHistory.objects.all()
    serializer_class = MeditationHistorySerializer
    representor_class = MeditationHistoryRepresentor

class NoticeViewSet(CustomViewSet):
    model_manager = Notice.objects
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    representor_class = NoticeRepresentor
    search_fields = ['title', 'content']

class PrivacyPolicyViewSet(CustomViewSet):
    model_manager = PrivacyPolicy.objects
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer
    representor_class = PrivacyPolicyRepresentor
    search_fields = ['title', 'content']

class TermViewSet(CustomViewSet):
    model_manager = Term.objects
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    representor_class = TermRepresentor
    search_fields = ['title', 'content']

class ConfidentialTermViewSet(CustomViewSet):
    model_manager = ConfidentialTerm.objects
    queryset = ConfidentialTerm.objects.all()
    serializer_class = ConfidentialTermSerializer
    representor_class = ConfidentialTermRepresentor
    search_fields = ['content', 'type']

class FaqViewSet(CustomViewSet):
    model_manager = Faq.objects
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    representor_class = FaqRepresentor
    search_fields = ['question', 'answer']

class MedicalDeviceViewSet(CustomViewSet):
    model_manager = MedicalDevice.objects
    queryset = MedicalDevice.objects.all()
    serializer_class = MedicalDeviceSerializer
    representor_class = MedicalDeviceRepresentor
    search_fields = ['label', 'content']
