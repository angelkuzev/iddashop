from django.views import generic as views
from iddashop.main.models import Order


class ListOrdersView(views.ListView):
    model = Order
    template_name = 'orders_list.html'
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['orders'] = Order.objects.filter(ordered_by=self.request.user)

        return context
