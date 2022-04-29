from django.urls import reverse_lazy
from django.views import generic as views
from iddashop.main.forms import AddCategoryForm


class AddCategoryView(views.CreateView):
    form_class = AddCategoryForm
    template_name = 'add_category.html'
    success_url = reverse_lazy('add category')
