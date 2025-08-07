from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    contexto = {
        "nombre": "Home Page"
    }
    return render(request, "homepage/inicio.html", contexto)

def blog(request):
    car_list = [
        {"title": "BMW"},
        {"title": "Mazda"}
    ]
    contexto = {
        "blog": "blog",
        "card_list": car_list
    }
    return render(request, "blog/blog.html", contexto)

def my_test(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

class CarListView(TemplateView):
    template_name= "blog/blog.html"
    
    def get_context_data(self):
         car_list = [
            {"title": "BMW"},
            {"title": "Mazda"}
          ]
         
         return {
            "car_list": car_list
         }
         