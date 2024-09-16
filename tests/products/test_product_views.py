from decimal import Decimal
import pytest
from django.test import Client
from django.urls import reverse
from products.models import Product


@pytest.mark.django_db
class TestProductsViews:

    def test_get_products_page(self):
        client = Client()

        response = client.get(reverse('products'))
        assert response.status_code == 200
