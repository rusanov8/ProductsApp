from decimal import Decimal
import pytest
from django.test import Client
from django.urls import reverse
from products.models import Product

@pytest.fixture
def create_product():
    product = Product.objects.create(
        title='Продукт_1',
        description='Описание продукта',
        price=19.99
    )
    return product


@pytest.mark.django_db
class TestApiViews:

    def test_get_products(self, create_product):
        client = Client()

        response = client.get(reverse('api_products'))
        assert response.status_code == 200
        assert response.json()[0].get('title') == 'Продукт_1'

    def test_create_product(self):
        client = Client()

        data = {
            'title': 'Продукт_2',
            'description': 'Описание продукта',
            'price': Decimal('100')
        }

        response = client.post(reverse('api_products'), data=data)

        print(response.json())
        assert response.status_code == 201
        assert Product.objects.filter(title='Продукт_2').exists()




