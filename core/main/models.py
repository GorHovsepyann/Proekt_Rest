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
    language_logo = models.ImageField('language_logo',upload_to='header/')
    
    def __str__(self) -> str:
        return self.name

class Slayder(models.Model):
    
    name = models.CharField('main name',max_length=250)
    img = models.ImageField('car image',upload_to='Slayder/')
    car_name = models.CharField('car name',max_length=250,null=True)
    button_name = models.CharField('button name',max_length=250,null=True)
    
    def __str__(self) -> str:
        return self.car_name

class Choice(models.Model):
    
    name = models.CharField('choise name',max_length=250)
    car_logo = models.ImageField('car image',upload_to='Choise/')
    act_car_logo = models.ImageField('active car image',upload_to='Choise/')
    car_about = models.CharField('car name',max_length=250)
    
    def __str__(self) -> str:
        return self.car_about
    
class Product(models.Model):
    
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE ,related_name='choice_pro')
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
        return self.car_name
    
class Reservation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='prod_res')
    name = models.CharField('spetification name',max_length=250)
    car_name = models.CharField('car name', max_length=250) 
    car_img = models.ImageField('car image',upload_to='reservation/')
    gear_name = models.CharField('gear_box name',max_length=250,null=True)
    gear_about = models.CharField('gear_box about',max_length=250,null=True)
    engine_name = models.CharField('engine name',max_length=250,null=True)
    engine_about = models.CharField('engine about',max_length=250,null=True)
    year_name = models.CharField('year_manufacture name',max_length=250,null=True)
    year_about = models.CharField('year_manufacture about',max_length=250,null=True)
    air_name = models.CharField('air_conditioner name',max_length=250,null=True)
    air_about = models.CharField('air_conditioner about',max_length=250,null=True)
    number_name = models.CharField('number_seats name',max_length=250,null=True)
    number_about = models.BigIntegerField('number_seats number',null=True)
    roof_name = models.CharField('roof name',max_length=250,null=True)
    roof_about = models.CharField('roof about',max_length=250,null=True)
    
    
    def __str__(self) -> str:
        return self.name

class Cost(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='prod_cost')
    name = models.CharField('cost name',max_length=250)
    rent_name = models.CharField('rent_for name',max_length=250,null=True)
    rent_num = models.IntegerField('rent_for price',null=True)
    rent_date = models.CharField('rent date',max_length=250)
    del_name = models.CharField('deliveri name',max_length=250,null=True)
    del_num = models.IntegerField('delivery price',null=True)
    pick_name = models.CharField('pick_up name',max_length=250,null=True)
    pick_num = models.IntegerField('pick_up price',null=True)
    drop_name = models.CharField('drop_off name',max_length=250,null=True)
    drop_num = models.IntegerField('drop_off price',null=True)
    other_name = models.CharField('other name',max_length=250,null=True)
    tpl_name = models.CharField('tpl name',max_length=250,null=True)
    tpl_num = models.IntegerField('tpl price',null=True)
    free_name = models.CharField('free_cancellation name',max_length=250,null=True)
    free_num = models.IntegerField('free_cancellation price',null=True)
    total_name = models.CharField('total name',max_length=250,null=True)
    total_num = models.IntegerField('total price',null=True)
    deposit_name = models.CharField('deposit name',max_length=250,null=True)
    deposit_num = models.IntegerField('deposit price',null=True)
    pay_name = models.CharField('to_pay name',max_length=250,null=True)
    pay_num = models.IntegerField('to_pay price',null=True)    
    but_name = models.CharField('amragrel name',max_length=250)
    
    def __str__(self) -> str:
        return self.name
    
class Requirements(models.Model):
    name = models.CharField('requirements name',max_length=250)
    drivers_name = models.CharField('drivers name',max_length=250,null=True)
    drivers_num = models.CharField('drivers about',max_length=250,null=True)
    min_name = models.CharField('minimum_driving name',max_length=250,null=True)
    min_num = models.CharField('minimum_driving about',max_length=250,null=True)
    mil_name = models.CharField('mileage name',max_length=250,null=True)
    mil_num = models.CharField('mileage about',max_length=250,null=True)
    
        
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
    safeti_name = models.CharField('child_safeti name',max_length=250,null=True)
    safeti_num = models.CharField('child_safeti price',max_length=250,null=True)
    seat_name = models.CharField('child_seat name',max_length=250,null=True)
    seat_num = models.CharField('child_seat price',max_length=250,null=True)
    booster_name = models.CharField('child_booster name',max_length=250,null=True)
    booster_num = models.CharField('child_booster price',max_length=250,null=True)
    second_name = models.CharField('second name',max_length=250,null=True)
    second_num = models.CharField('second price',max_length=250,null=True)
    router_name = models.CharField('wifi_router name',max_length=250,null=True)
    router_num = models.CharField('wifi_router price',max_length=250,null=True)
    winter_name = models.CharField('winter name',max_length=250,null=True)
    winter_num = models.CharField('winter price',max_length=250,null=True)
    geo_name = models.CharField('georgia name',max_length=250,null=True)
    geo_num = models.CharField('georgia price',max_length=250,null=True)
    
    
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

