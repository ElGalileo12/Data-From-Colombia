from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="list_product"),
    path("agregar/", views.ProductFormView.as_view(), name="add_product"),
    path("api/", views.ProductListApi.as_view(), name="product_list_api"),
]
