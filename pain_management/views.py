from django.shortcuts import render
from rest_framework import viewsets
from core.views import CustomViewSet
from .models import (
    Pain, PainAnswer, PainArea, PainAreaDetail,
    PainCategory, PainFeedback, PainQuestion
)
from .serializers import (
    PainSerializer, PainAnswerSerializer, PainAreaSerializer,
    PainAreaDetailSerializer, PainCategorySerializer,
    PainFeedbackSerializer, PainQuestionSerializer
)
from .representors import (
    PainRepresentor, PainAnswerRepresentor, PainAreaRepresentor,
    PainAreaDetailRepresentor, PainCategoryRepresentor,
    PainFeedbackRepresentor, PainQuestionRepresentor
)

# Create your views here.

class PainViewSet(CustomViewSet):
    model_manager = Pain.objects
    queryset = Pain.objects.all()
    serializer_class = PainSerializer
    representor_class = PainRepresentor
    search_fields = ['content']

class PainAnswerViewSet(CustomViewSet):
    model_manager = PainAnswer.objects
    queryset = PainAnswer.objects.all()
    serializer_class = PainAnswerSerializer
    representor_class = PainAnswerRepresentor
    search_fields = ['name']

class PainAreaViewSet(CustomViewSet):
    model_manager = PainArea.objects
    queryset = PainArea.objects.all()
    serializer_class = PainAreaSerializer
    representor_class = PainAreaRepresentor
    search_fields = ['name']

class PainAreaDetailViewSet(CustomViewSet):
    model_manager = PainAreaDetail.objects
    queryset = PainAreaDetail.objects.all()
    serializer_class = PainAreaDetailSerializer
    representor_class = PainAreaDetailRepresentor

class PainCategoryViewSet(CustomViewSet):
    model_manager = PainCategory.objects
    queryset = PainCategory.objects.all()
    serializer_class = PainCategorySerializer
    representor_class = PainCategoryRepresentor
    search_fields = ['name']

class PainFeedbackViewSet(CustomViewSet):
    model_manager = PainFeedback.objects
    queryset = PainFeedback.objects.all()
    serializer_class = PainFeedbackSerializer
    representor_class = PainFeedbackRepresentor
    search_fields = ['content']

class PainQuestionViewSet(CustomViewSet):
    model_manager = PainQuestion.objects
    queryset = PainQuestion.objects.all()
    serializer_class = PainQuestionSerializer
    representor_class = PainQuestionRepresentor
    search_fields = ['name']
