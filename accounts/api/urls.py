from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import AuthView, RegisterAPIView, logout_view

urlpatterns = [
    url(r'^$', AuthView.as_view(), name='auth'),
    url(r'^logout/$', logout_view),
    url(r'^register/$', RegisterAPIView.as_view()),
    url(r'^jwt/$', obtain_jwt_token),
    url(r'^jwt/refresh/$', refresh_jwt_token),
]
