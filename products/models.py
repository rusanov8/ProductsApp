from django.db import models


class Product(models.Model):

    title = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'products'
