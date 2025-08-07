from django.urls import path
from . import views
from .views import my_test


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path("blog", views.CarListView.as_view(), name="blog"),
    path("listado/<int:id>", my_test),
    path("marcas/<str:brand>", my_test),
]
