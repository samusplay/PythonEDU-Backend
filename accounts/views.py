from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    def create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            tokens=get_tokens_for_user(user)
            return Response({
                'user':serializer.data,
                'tokens':tokens
            },status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)