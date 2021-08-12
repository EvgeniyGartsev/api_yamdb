from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from api.serializers import UserSerializer, TokenSerializer
from .models import User


def create_confirmation_code_and_send_email(username):
    # создаем confirmation code и отправляем по email
    user = get_object_or_404(User, username=username)
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject='Confirmation code',
        message=f'Your confirmation code {confirmation_code}',
        from_email='webmaster@localhost',
        recipient_list=['e@y.ru'])


class APISignUp(APIView):
    '''Регистрация пользователя'''
    permission_classes = (AllowAny, )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # создаем confirmation code и отправляем на почту
            create_confirmation_code_and_send_email(serializer.data['username'])
            return Response(
                {'email': serializer.data['email'],'username': serializer.data['username']},
                status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIToken(APIView):
    '''Выдача токена'''
    permission_classes = (AllowAny, )
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(User, username=serializer.data['username'])
            # проверяем confirmation code, если верный, выдаем токен
            if default_token_generator.check_token(user, serializer.data['confirmation_code']):
                token = AccessToken.for_user(user)
                return Response(
                    {'token': str(token)}, status=status.HTTP_200_OK)
            return Response({
                'confirmation code': 'Incorrect confirmation code!'},
                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


class UserViewSet(ModelViewSet):
    '''Работа с пользователями'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
