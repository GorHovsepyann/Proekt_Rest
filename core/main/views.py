from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (HeaderSerializers,Etap1Serializers,ChoiceSerializers,
                          ProductSerializers,AboutSerializers,AdvantagesSerializers)
from .models import Header,Etap1,Choice,Product,About,Advantages

# Create your views here.

class HeaderView(viewsets.ModelViewSet):
    
    queryset = Header.objects.all()
    serializer_class = HeaderSerializers
    
class Etap1View(viewsets.ModelViewSet):
    
    queryset = Etap1.objects.all()
    serializer_class = Etap1Serializers
    
class ChoiseView(viewsets.ModelViewSet):
    
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializers

class ProductView(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class AboutView(viewsets.ModelViewSet):
    
    queryset = About.objects.all()
    serializer_class = AboutSerializers    
    
class AdvantagesView(viewsets.ModelViewSet):
    
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializers