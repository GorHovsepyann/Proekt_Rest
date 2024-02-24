from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (HeaderSerializers,SlayderSerializers,ChoiceSerializers,
                          ProductSerializers,AboutSerializers,AdvantagesSerializers)
from .models import Header,Slayder,Choice,Product,About,Advantages

# Create your views here.

class HeaderView(viewsets.ModelViewSet):
    
    queryset = Header.objects.all()
    serializer_class = HeaderSerializers
    
class SlayderView(viewsets.ModelViewSet):
    
    queryset = Slayder.objects.all()
    serializer_class = SlayderSerializers
    
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