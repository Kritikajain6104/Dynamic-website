from django.shortcuts import render
from rest_framework import viewsets
from contact.models import contact1
from contact.serializers import contactserializer
# Create your views here.


class contactViewset(viewsets.ModelViewSet):
    queryset=contact1.objects.all()
    serializer_class=contactserializer
