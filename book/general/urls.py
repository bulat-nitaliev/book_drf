from rest_framework.routers import SimpleRouter
from general.views import UserViewSet
from django.urls import path


urlpatterns = [
    path('users/', UserViewSet.as_view({'get':"list", "post": "create"})),
]