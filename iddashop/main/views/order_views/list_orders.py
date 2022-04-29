from django.views import generic as views
from iddashop.common.views_mixins import NotAuthRedirect
from iddashop.main.models import Order


class ListOrdersView(NotAuthRedirect, views.ListView):
    model = Order
    template_name = 'orders/orders_list.html'
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        user_id = self.request.user.id
        context = super().get_context_data()
        context['accepted_orders'] = Order.objects.filter(ordered_by=user_id, accepted_by__isnull=False, accepted_on__isnull=False)
        context['waiting_orders'] = Order.objects.filter(ordered_by=user_id, accepted_by=None, accepted_on=None)

        return context
