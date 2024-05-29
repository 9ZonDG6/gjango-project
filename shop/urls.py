from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('category/<slug:category_slug>', views.CategoryView.as_view(), name='category'),
    path('product/<slug:product_slug>', views.ProductView.as_view(), name='product'),
    path('redirect/', views.Redirect.as_view(), name='redirect'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),
] + router.urls
