from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (HeaderSerializers,SlayderSerializers,ChoiceSerializers,CostSerializers,RequirementsSerializers,
                          ProductSerializers,AdvantagesSerializers,ReservationSerializers,InsuranceSerializers,AdditionalSerializers)
from .models import Header,Slayder,Choice,Product,Advantages,Reservation,Cost,Requirements,Insurance,Additional
from .filters import ReservationFilter,CostFilter

# Create your views here.

class HeaderView(viewsets.ModelViewSet):
    
    queryset = Header.objects.all()
    serializer_class = HeaderSerializers
    
class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReservationFilter
    
class CostView(viewsets.ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = CostFilter  

class RequirementsView(viewsets.ModelViewSet):
    
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializers

class InsuranceView(viewsets.ModelViewSet):
    
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializers
    
class AdditionalView(viewsets.ModelViewSet):
    
    queryset = Additional.objects.all()
    serializer_class = AdditionalSerializers

class SlayderView(viewsets.ModelViewSet):
    
    queryset = Slayder.objects.all()
    serializer_class = SlayderSerializers
    
class ChoiseView(viewsets.ModelViewSet):
    
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializers

class ProductView(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
  
    
class AdvantagesView(viewsets.ModelViewSet):
    
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializers