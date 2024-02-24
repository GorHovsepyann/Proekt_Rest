from django.db import models
from colorfield.fields import ColorField

# Create your models here.

class Header(models.Model):
    
    logo = models.ImageField('header logo',upload_to='header/')
    name = models.CharField('header name',max_length=250)
    page1 = models.CharField('page1 name',max_length=250)
    page2 = models.CharField('page2 name',max_length=250)
    page3 = models.CharField('page3 name',max_length=250)
    page4 = models.CharField('page4 name',max_length=250)
    search = models.CharField('search name',max_length=250)
    search_logo = models.ImageField('search_logo',upload_to='header/')
    currency_logo = models.ImageField('currency_logo',upload_to='header/')
    language_logo = models.ImageField('language_logo',upload_to='header/')
    
    def __str__(self) -> str:
        return self.name

class Slayder(models.Model):
    
    name = models.CharField('main name',max_length=250)
    background = ColorField('background color', default='#FF0000')
    img = models.ImageField('slayder image',upload_to='etap1/')
    
    def __str__(self) -> str:
        return self.name

class Choice(models.Model):
    
    name = models.CharField('choise name',max_length=250)
    car_logo = models.ImageField('car image',upload_to='Choise/')
    car_about = models.CharField('Car name',max_length=250)
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    
    name = models.CharField('product name',max_length=250)
    button_name = models.CharField('button name',max_length=250)
    pleace_name = models.CharField('pleace name',max_length=250)
    pleace_logo = models.ImageField('place image',upload_to='Product/')
    car_name = models.CharField('car name',max_length=250)
    car_logo = models.ImageField('car image',upload_to='Product/')
    speed_name = models.CharField('speed name',max_length=250)
    speed_logo = models.ImageField('speed image',upload_to='Product/')    
    gearbox_name = models.CharField('gearbox name',max_length=250)
    gearbox_logo = models.ImageField('gearbox image',upload_to='Product/') 
    person_name = models.CharField('person name',max_length=250)
    person_logo = models.ImageField('person image',upload_to='Product/') 
    fuel_name = models.CharField('fuel name',max_length=250)
    fuel_logo = models.ImageField('fuel image',upload_to='Product/') 
    car_button = models.CharField('button name',max_length=250)
    price = models.BigIntegerField('rent price')
    price_text = models.CharField('price about',max_length=250)
    
    def __str__(self) -> str:
        return self.name
    
class About(models.Model):
    name = models.CharField('about name',max_length=250)
    about = models.TextField('about text')

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        
        def __str__(self) -> str:
            return self.name
        
class Advantages(models.Model):
    img = models.ImageField('advantages image',upload_to='advantages/')
    name = models.CharField('advantages name',max_length=250)
    about = models.TextField('advantages text')

    class Meta:
        verbose_name = 'Advantage'
        verbose_name_plural = 'Advantages'
        
        def __str__(self) -> str:
            return self.name