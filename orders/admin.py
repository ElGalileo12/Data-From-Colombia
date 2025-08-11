from django.contrib import admin
from .models import Order, OrderProduct


class OerderProductInLineAdamin(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model: Order
    inlines = [OerderProductInLineAdamin]


admin.site.register(Order, OrderAdmin)
