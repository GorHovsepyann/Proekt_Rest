from .models import Header,Etap1,Choice,Product
from modeltranslation.translator import register, TranslationOptions

@register(Header)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'page1','page2','page3','search')
    
@register(Etap1)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','about')
    
@register(Choice)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','car_about')
    
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','button_name','pleace_name','car_name','speed_name',
              'gearbox_name','person_name','fuel_name','car_button','price_text')