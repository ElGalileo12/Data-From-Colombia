from django.urls import path, include
from .views import MyOrderView

urlpatterns = [path("mi-orden", MyOrderView.as_view(), name="my-order")]
