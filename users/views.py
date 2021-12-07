from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from django.contrib.auth.hashers import mask_hash

from .serializers import LoginSerializer, signupSerializer
from .models import Login
import jwt
import datetime
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Electronic Product API')

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = request.data['email']
            password = mask_hash(request.data['password'])

            user = Login.objects.filter(email=email).first()
            if user is None:
                raise AuthenticationFailed('User not found!')
            if not Login.objects.filter(email=email, password=password).exists():
                raise AuthenticationFailed('Incorrect password!')

            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256')

            response = Response()

            response.set_cookie(key='authorization',
                                value=token, httponly=True)
            response.data = {
                'authorization': token,
                'message': 'User Logged in Successfully'
            }
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def get(self, request):
        response = Response()
        for cookie in request.COOKIES:
            response.delete_cookie(cookie)
        return response


class signupView(APIView):
    serializer_class = signupSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = request.data['username']
            email = request.data['email']
            password = mask_hash(request.data['password'])
            password2 = mask_hash(request.data['password2'])

            if password != password2:
                raise ValidationError('Password did not match!!')

            user = Login.objects.filter(email=email).exists()
            if user:
                response_data = {'Error': 'Email Already Exists'}
                return Response(response_data, status=status.HTTP_403_FORBIDDEN)
            Login(
                username=username,
                email=email,
                password=password
            ).save()
            response_data = {
                'Message': 'New User Created Successfully',
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
