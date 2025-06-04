from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from .models import Admin
from rest_framework import status

class AdminTokenAuth(BaseAuthentication):
    """
    Custom token-based authentication for admin users.
    """
    
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None

        try:
            # Extract the token from the header
            auth_parts = auth_header.split()
            if len(auth_parts) != 2 or auth_parts[0].lower() != 'bearer':
                raise AuthenticationFailed('Invalid token header')

            token = auth_parts[1]
            payload = self._decode_token(token)
            
            # Get the admin
            admin = Admin.objects.get(id=payload['admin_id'])
            
            # Check if admin is active
            if not admin.is_active:
                raise AuthenticationFailed('Admin is inactive')
                
            return (admin, None)
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        except Admin.DoesNotExist:
            raise AuthenticationFailed('Admin not found')
        except Exception as e:
            raise AuthenticationFailed(str(e))

    def authenticate_header(self, request):
        return 'Bearer'

    @staticmethod
    def _decode_token(token):
        try:
            return jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=['HS256']
            )
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')

    @staticmethod
    def generate_token(admin):
        """
        Generate a JWT token for the admin
        """
        payload = {
            'admin_id': admin.id,
            'exp': datetime.utcnow() + timedelta(days=1),  # Token expires in 1 day
            'iat': datetime.utcnow()
        }
        
        return jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm='HS256'
        ) 