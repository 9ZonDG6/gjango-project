from django.views.generic import ListView, RedirectView
from .models import Product, Category


class IndexView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = 'Список товаров'
        return context


class CategoryView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/category.html'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        selected_category = Category.objects.get(slug=self.kwargs['category_slug'])
        context['selected_category'] = selected_category
        context['title'] = selected_category.title
        return context


class ProductView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        product = Product.objects.get(slug=self.kwargs['product_slug'])
        context['title'] = product.title
        context['product'] = product
        context['selected_category'] = product.category
        return context


class Redirect(RedirectView):
    query_string = True
    url = 'https://goo.su/yfNkna'
