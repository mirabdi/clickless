from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Admin
from .token_auth import AdminTokenAuth
from rest_framework import viewsets
from core.views import CustomViewSet
from .serializers import AdminSerializer
from .representors import AdminRepresentor

# Create your views here.

class AdminViewSet(CustomViewSet):
    model_manager = Admin.objects
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    representor_class = AdminRepresentor
    search_fields = ['email']

    @action(detail=False, methods=['post'])
    def login(self, request):
        """Login endpoint to get JWT token"""
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response({
                'status': 1,
                'message': 'Email and password are required',
                'response': None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            admin = Admin.objects.get(email=email)
            if not admin.check_password(password):
                return Response({
                    'status': 1,
                    'message': 'Invalid credentials',
                    'response': None
                }, status=status.HTTP_401_UNAUTHORIZED)
            
            if not admin.is_active:
                return Response({
                    'status': 1,
                    'message': 'Admin account is inactive',
                    'response': None
                }, status=status.HTTP_401_UNAUTHORIZED)
            
            token = AdminTokenAuth.generate_token(admin)
            return Response({
                'status': 0,
                'message': 'success',
                'response': {
                    'token': token,
                    'admin': {
                        'id': admin.id,
                        'email': admin.email,
                        'first_name': admin.first_name,
                        'last_name': admin.last_name
                    }
                }
            })
        except Admin.DoesNotExist:
            return Response({
                'status': 1,
                'message': 'Admin not found',
                'response': None
            }, status=status.HTTP_404_NOT_FOUND)
