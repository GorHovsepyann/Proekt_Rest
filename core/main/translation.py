from .models import Header,Choice,Product,Reservation,Cost,Requirements,Insurance,Additional,Advantages,Slayder
from modeltranslation.translator import register, TranslationOptions

@register(Header)
class HeaderTranslationOptions(TranslationOptions):
    fields = ('page1','page2','page3','page4','search','language_logo')

@register(Reservation)
class ReservationTranslationOptions(TranslationOptions):
    fields = ('name','gear_name','gear_about','engine_name','engine_about','year_name','year_about','air_name','air_about','number_name','roof_name','roof_about')

@register(Slayder)
class SlayderTranslationOptions(TranslationOptions):
    fields = ('button_name',)
    
@register(Cost)
class CostTranslationOptions(TranslationOptions):
    fields = ('name','rent_name','del_name','pick_name','drop_name','other_name','free_name','total_name','deposit_name','pay_name','but_name','rent_date')

@register(Requirements)
class RequirementsTranslationOptions(TranslationOptions):
    fields = ('name','drivers_name','drivers_num','min_name','min_num','mil_name','mil_num')

@register(Insurance)
class InsuranceTranslationOptions(TranslationOptions):
    fields =('name','full_name','full_about','super_name','super_about','cwd_about','tpl_about','but_name','free_name','free_about','per_name','thef_name')

@register(Additional)
class AdditionalTranslationOptions(TranslationOptions):
    fields = ('name','add_name','safeti_name','seat_name','booster_name','second_name','router_name','winter_name','geo_name')
    
@register(Choice)
class ChoiceTranslationOptions(TranslationOptions):
    fields = ('name','car_about')
    
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name','button_name','pleace_name','car_name','speed_name',
              'gearbox_name','person_name','fuel_name','car_button','price_text')
    
@register(Advantages)
class AdvansagesTranslationOptions(TranslationOptions):
    fields = ('name','about','ad_name','ad_about')