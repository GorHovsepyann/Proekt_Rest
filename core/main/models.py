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
    
class Reservation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='prod_res')
    name = models.CharField('spetification name',max_length=250)
    car_name = models.CharField('car name', max_length=250) 
    car_img = models.ImageField('car image',upload_to='reservation/')
    spet_name = models.CharField('spetification name',max_length=250)
    spet_about = models.CharField('spetification about',max_length=250)
    
    def __str__(self) -> str:
        return self.name

class Cost(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='prod_cost')
    name = models.CharField('cost name',max_length=250)
    cost_name = models.CharField('cost name',max_length=250)
    cost_num = models.IntegerField('cost price')
    rent_date = models.CharField('rent date',max_length=250)
    but_name = models.CharField('amragrel name',max_length=250)
    
    def __str__(self) -> str:
        return self.name
    
class Requirements(models.Model):
    name = models.CharField('requirements name',max_length=250)
    req_name = models.CharField('requirements name',max_length=250)
    req_num = models.CharField('requirements age',max_length=250)
        
    def __str__(self) -> str:
        return self.name
    
class Insurance(models.Model):
    name = models.CharField('requirements name',max_length=250)
    full_name = models.CharField('full name',max_length=250)
    full_about = models.TextField('full text')
    full_num = models.IntegerField('full price')
    super_name = models.CharField('super name',max_length=250)
    super_about = models.TextField('super text')
    super_num = models.IntegerField('super price')
    cwd_name = models.CharField('cwd name',max_length=250)
    cwd_about = models.TextField('cwd text')
    cwd_num = models.IntegerField('cwd price')
    tpl_name = models.CharField('tpl name',max_length=250)
    tpl_about = models.CharField('tpl free',max_length=250)
    but_name = models.CharField('amragrel name',max_length=250)    
    free_name = models.CharField('free name',max_length=250)
    free_about = models.CharField('free free',max_length=250)
    per_name = models.CharField('personal name',max_length=250)
    per_num = models.IntegerField('personal price')
    thef_name = models.CharField('theft name',max_length=250)
    thef_num = models.IntegerField('theft price')
    
        
    def __str__(self) -> str:
        return self.name
    
class Additional(models.Model):
    name = models.CharField('requirements name',max_length=250)
    add_name = models.CharField('additional name',max_length=250)
    add_num = models.IntegerField('additional price')
    winter_name = models.CharField('winter name',max_length=250)
    winter_num = models.CharField('winter price',max_length=250)
    
    def __str__(self) -> str:
        return self.name
    
        
class Advantages(models.Model):
    name = models.CharField('about name',max_length=250)
    about = models.TextField('about text')
    img = models.ImageField('advantages image',upload_to='advantages/')
    ad_name = models.CharField('advantages name',max_length=250)
    ad_about = models.TextField('advantages text')

    
        
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Advantage'
        verbose_name_plural = 'Advantages'

