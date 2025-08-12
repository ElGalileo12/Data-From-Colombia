from django.test import TestCase
from django.urls import reverse
from .models import Product


class ProductListViewTest(TestCase):
    def test_ShouldReturn200(self):
        url = reverse("list_product")
        response = self.client.get(url)
        # breakpoint()  aquí nos podemos detener a analizar la respuesta
        self.assertEqual(response.status_code, 200)

    def test_ShouldReturn200_with_products(self):
        url = reverse("list_product")
        Product.objects.create(
            name="test", description="test description", price="5", available=True
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products"].count(), 1)
