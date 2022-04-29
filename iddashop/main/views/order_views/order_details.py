from django.views import generic as views
from iddashop.common.views_mixins import NotAuthRedirect
from iddashop.main.models import Order, OrderedItem


class OrderDetailsView(NotAuthRedirect, views.DetailView):
    model = Order
    template_name = 'orders/order_details.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = OrderedItem.objects.filter(order_id=self.kwargs['pk'])

        return context
