from django.views import generic as views
from iddashop.main.models import Order, OrderedItem


class OrderDetailsView(views.DetailView):
    model = Order
    template_name = 'order_details.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = OrderedItem.objects.filter(order_id=self.kwargs['pk'])

        return context
