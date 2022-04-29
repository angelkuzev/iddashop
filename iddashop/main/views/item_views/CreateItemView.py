from django.urls import reverse_lazy
from django.views import generic as views
from iddashop.main.forms import CreateItemForm


class CreateItemView(views.CreateView):
    form_class = CreateItemForm
    template_name = 'items/add_item.html'
    success_url = reverse_lazy('home')
