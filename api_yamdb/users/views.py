from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer
from .models import User


class APISignUp(APIView):
    '''Регистрация пользователя'''
    pass


class APIToken(APIView):
    '''Выдача токена'''
    pass


class UserViewSet(ModelViewSet):
    '''Работа с пользователями'''
    pass
