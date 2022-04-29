from django.views import generic as views
from iddashop.common.views_mixins import NotStaffRedirect
from iddashop.main.models import Order


class ManageOrdersView(NotStaffRedirect, views.ListView):
    model = Order
    template_name = 'orders/orders_list.html'
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['accepted_orders'] = Order.objects.filter(accepted_by__isnull=False, accepted_on__isnull=False)
        context['waiting_orders'] = Order.objects.filter(accepted_by=None, accepted_on=None)
        context['viewed_as_manager'] = True

        if self.request.user.is_superuser:
            context['viewed_as_admin'] = True

        return context
