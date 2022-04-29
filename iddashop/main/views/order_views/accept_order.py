from django.urls import reverse_lazy
from django.utils.datetime_safe import datetime
from django.views import generic as views
from iddashop.main.forms import AcceptOrderForm
from iddashop.main.models import Order, OrderedItem


class AcceptOrderView(views.UpdateView):
    model = Order
    form_class = AcceptOrderForm
    template_name = 'orders/order_details.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['viewed_as_manager'] = True
        context['order_items'] = OrderedItem.objects.filter(order_id=self.kwargs['pk'])

        return context

    def get_success_url(self):
        self.object.accepted_on = datetime.now()
        self.object.accepted_by = self.request.user
        self.object.save()
        return reverse_lazy('home')
