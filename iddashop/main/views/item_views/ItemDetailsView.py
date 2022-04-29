from django.views import generic as views
from iddashop.main.models import Item, Quantity


class ItemDetailsView(views.DetailView):
    model = Item
    template_name = 'items/view_item.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quantities'] = Quantity.objects.get(pk=context['item'].id)
        return context
