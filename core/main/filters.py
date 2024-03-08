import django_filters
from .models import Reservation,Product,Cost,Choice

class ReservationFilter(django_filters.FilterSet):
    product = django_filters.ModelChoiceFilter(queryset=Product.objects.all(), field_name='product')
    car_img = django_filters.CharFilter(field_name='car_img', lookup_expr='exact')

    class Meta:
        model = Reservation
        fields = '__all__'

        
class CostFilter(django_filters.FilterSet):
    product = django_filters.ModelChoiceFilter(queryset=Product.objects.all(), field_name='product')

    class Meta:
        model = Cost
        fields = '__all__'
        
class ProductFilter(django_filters.FilterSet):
    choice = django_filters.ModelChoiceFilter(queryset=Choice.objects.all(), field_name='choice')
    pleace_logo = django_filters.CharFilter(field_name='pleace_logo', lookup_expr='exact')
    car_logo = django_filters.CharFilter(field_name='car_logo', lookup_expr='exact')
    speed_logo = django_filters.CharFilter(field_name='speed_logo', lookup_expr='exact')
    gearbox_logo = django_filters.CharFilter(field_name='gearbox_logo', lookup_expr='exact')
    person_logo = django_filters.CharFilter(field_name='person_logo', lookup_expr='exact')
    fuel_logo = django_filters.CharFilter(field_name='fuel_logo', lookup_expr='exact')

    class Meta:
        model = Product
        fields = '__all__'