from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrugViewSet, DrugDetailViewSet, DrugTypeViewSet

router = DefaultRouter()
router.register(r'drugs', DrugViewSet)
router.register(r'drug-details', DrugDetailViewSet)
router.register(r'drug-types', DrugTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 