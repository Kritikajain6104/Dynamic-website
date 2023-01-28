from django.contrib import admin
from django.urls import path,include
from rest_framework import routers,viewsets
from contact.models import contact1
from contact.views import contactViewset
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

router=routers.DefaultRouter()
router.register(r'contact1',contactViewset)

urlpatterns = [
    path('', include(router.urls)),
]