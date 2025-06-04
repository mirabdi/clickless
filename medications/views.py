from django.shortcuts import render
from rest_framework import viewsets
from core.views import CustomViewSet
from .models import Drug, DrugDetail, DrugType
from .serializers import DrugSerializer, DrugDetailSerializer, DrugTypeSerializer
from .representors import DrugRepresentor, DrugDetailRepresentor, DrugTypeRepresentor

# Create your views here.

class DrugViewSet(CustomViewSet):
    model_manager = Drug.objects
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    representor_class = DrugRepresentor
    search_fields = ['name', 'type']

class DrugDetailViewSet(CustomViewSet):
    model_manager = DrugDetail.objects
    queryset = DrugDetail.objects.all()
    serializer_class = DrugDetailSerializer
    representor_class = DrugDetailRepresentor

class DrugTypeViewSet(CustomViewSet):
    model_manager = DrugType.objects
    queryset = DrugType.objects.all()
    serializer_class = DrugTypeSerializer
    representor_class = DrugTypeRepresentor
    search_fields = ['type']
