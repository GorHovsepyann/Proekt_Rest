import django_filters
from .models import Reservation,Product,Cost

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