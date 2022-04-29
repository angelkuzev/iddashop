from django.views import generic as views
from iddashop.main.models import Order


class ManageOrdersView(views.ListView):
    model = Order
    template_name = 'orders_list.html'
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['orders'] = Order.objects.filter(accepted_by=None, accepted_on=None)
        context['viewed_as_manager'] = True

        return context
