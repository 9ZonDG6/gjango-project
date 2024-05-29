import django_filters
from shop.models import Product


class ProductFilter(django_filters.FilterSet):
    # Фильтрация цены от
    price_from = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Цена от')
    # Фильтрация цены до
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Цена до')
    # Сортировка по цене и время публикации
    ordering = django_filters.OrderingFilter(
        fields=(
            ('price', 'Цена'),
            ('created_at', 'Новинки')
        ),
        label='Сортировка'
    )

    class Meta:
        model = Product
        fields = ('title', 'ordering', 'price_from', 'price_to', 'in_stock')
