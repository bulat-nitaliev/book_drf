from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from general.serializers import UserRegistrationSerializer, UserListSerializer
from general.models import User

from rest_framework_simplejwt.views import TokenObtainPairView
from general.serializers import CookieTokenRefreshSerializer, MyTokenObtainPairSerializer
from datetime import timedelta

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class UserViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    def get_serializer_class(self):
        if self.action == 'create':
           return UserRegistrationSerializer
        return UserListSerializer