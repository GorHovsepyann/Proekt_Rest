from rest_framework import serializers
from .models import Header,Slayder,Choice,Product,Advantages,Reservation,Cost,Requirements,Insurance,Additional


class HeaderSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Header
        fields = '__all__'

class ReservationSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Reservation
        fields = '__all__'
        
class CostSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Cost
        fields = '__all__'
    
class RequirementsSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Requirements
        fields = '__all__'
        
class InsuranceSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Insurance
        fields = '__all__'

class AdditionalSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Additional
        fields = '__all__'
        
class SlayderSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Slayder
        fields = '__all__'
        
class ChoiceSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Choice
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Product
        fields = '__all__'
        
        
class AdvantagesSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Advantages
        fields = '__all__'