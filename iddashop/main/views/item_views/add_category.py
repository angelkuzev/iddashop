from django.urls import reverse_lazy
from django.views import generic as views
from iddashop.common.views_mixins import NotStaffRedirect
from iddashop.main.forms import AddCategoryForm


class AddCategoryView(NotStaffRedirect, views.CreateView):
    form_class = AddCategoryForm
    template_name = 'items/add_category.html'
    success_url = reverse_lazy('add category')
