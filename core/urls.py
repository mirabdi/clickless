from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import views if any specific core views are added later
from .views import DashboardStatsViewSet

router = DefaultRouter()
router.register(r'dashboard-stats', DashboardStatsViewSet, basename='dashboard-stats')

urlpatterns = [
    # Add core-specific URL patterns here when needed
    path('', include(router.urls)),
] 