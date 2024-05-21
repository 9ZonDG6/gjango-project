from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('category/<slug:category_slug>', CategoryView.as_view(), name='category'),
    path('product/<slug:product_slug>', ProductView.as_view(), name='product'),
    path('redirect/', Redirect.as_view(), name='redirect')
]
