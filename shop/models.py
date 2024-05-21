from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=150)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    info = models.TextField(verbose_name='Информация', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновление')
    price = models.PositiveIntegerField('Цена', default=0)
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    in_stock = models.BooleanField('В наличии', default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})
