from django.urls import reverse_lazy
from django.views.generic import UpdateView
from iddashop.common.views_mixins import NotStaffRedirect
from iddashop.main.forms import EditItemForm
from iddashop.main.models import Item


class EditItemView(NotStaffRedirect, UpdateView):
    model = Item
    form_class = EditItemForm
    template_name = 'items/edit_item.html'

    def get_success_url(self):
        return reverse_lazy('item details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_id'] = self.object.pk
        return context
