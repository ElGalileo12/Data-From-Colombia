from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class MyOrderViewTest(TestCase):
    def test_no_user_should_redirect(self):
        url = reverse("my-order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/login/?next=/pedidos/mi-orden")

    def test_logged_user_shouold_redirect(self):
        url = reverse("my-order")
        user = get_user_model().objects.create(username="test")
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
