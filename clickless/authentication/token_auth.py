from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class UserTokenActiveAuth(BaseAuthentication):
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
            
            # Get the user
            user = User.objects.get(id=payload['user_id'])
            
            # Check if user is active
            if not user.is_active:
                raise AuthenticationFailed('User is inactive')
                
            return (user, None)
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found')
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
    def generate_token(user):
        """
        Generate a JWT token for the user
        """
        payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=1),  # Token expires in 1 day
            'iat': datetime.utcnow()
        }
        
        return jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm='HS256'
        ) 