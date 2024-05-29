from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient

from shop import models


class Tests(TestCase):
    def setUp(self):
        self.category = models.Category.objects.create(
            title='Телевизоры',
            slug='televizory',
        )
        self.product = models.Product.objects.create(
            title='LG',
            slug='lg',
            price=1000,
            info='фул шд телевизор',
            in_stock=True,
            category=self.category,
        )

        self.client = APIClient()
        self.user = User.objects.create_superuser(username='admin', password='pip135790')
        self.client.force_authenticate(user=self.user)

    def test_list(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        url = reverse('product-list')
        data = {
            'title': 'TV',
            'slug': 'tv',
            'price': 11500,
            'info': 'Еще телевизор',
            'in_stock': False,
            'category': self.category.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        url = reverse('product-detail', args=[self.product.id])
        data = {
            'title': 'LG-1',
            'price': 1500,
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update(self):
        url = reverse('product-detail', args=[self.product.id])
        data = {
            'price': 2500,
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
