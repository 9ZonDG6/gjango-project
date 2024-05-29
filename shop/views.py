from django.views.generic import ListView, RedirectView, CreateView
from django.urls import reverse_lazy
from shop import filters
from .models import Product, Category
from .serializers import ProductSerializer
from .forms import RegisterForm
from rest_framework.viewsets import ModelViewSet


class IndexView(ListView):
    paginate_by = 16  # Устанавливает количество продуктов на страницу - пагинация
    model = Product
    context_object_name = 'products'
    template_name = 'shop/index.html'

    def get_filters(self):
        return filters.ProductFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['filters'] = self.get_filters()
        context['title'] = 'Список товаров'
        return context


class CategoryView(ListView):
    paginate_by = 16
    model = Product
    context_object_name = 'products'
    template_name = 'shop/category.html'

    def get_filters(self):
        return filters.ProductFilter(self.request.GET, queryset=Product.objects.filter(
            category__slug=self.kwargs['category_slug']))

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        selected_category = Category.objects.get(slug=self.kwargs['category_slug'])
        context['selected_category'] = selected_category
        context['filters'] = self.get_filters()
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


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    filterset_class = filters.Product
    serializer_class = ProductSerializer


class Redirect(RedirectView):
    query_string = True
    url = 'https://github.com/9ZonDG6/gjango-project'
