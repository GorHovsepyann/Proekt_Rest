from rest_framework import serializers
from .models import Header,Etap1,Choice,Product,About,Advantages

class HeaderSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Header
        fields = '__all__'
        
class Etap1Serializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Etap1
        fields = '__all__'
        
class ChoiceSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Choice
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Product
        fields = '__all__'

class AboutSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = About
        fields = '__all__'
        
class AdvantagesSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Advantages
        fields = '__all__'