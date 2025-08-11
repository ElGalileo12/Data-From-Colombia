from django.views.generic import DetailView
from django.db.models import Sum, F
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order


class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()

        if order:
            total = (
                order.orderproduct_set.aggregate(total=Sum(F("product__price")))[
                    "total"
                ]
                or 0
            )
        else:
            total = 0

        context["total"] = total
        return context
