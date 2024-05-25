import django_filters
from shop.models import Product


class ProductFilter(django_filters.FilterSet):
    price_from = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Цена от')
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Цена до')
    ordering = django_filters.OrderingFilter(
        fields=(
            ('price', 'Цена'),
        ),
        label='Сортировка по цене'
    )

    class Meta:
        model = Product
        fields = ('ordering', 'price_from', 'price_to', 'in_stock')
