from django.test import TestCase, Client
from shop import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
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

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_category(self):
        response = self.client.get(f'/category/{self.category.slug}')
        self.assertEqual(response.status_code, 200)

    def test_product(self):
        response = self.client.get(f'/product/{self.product.slug}')
        self.assertEqual(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/redirect/')
        self.assertEqual(response.status_code, 302)
