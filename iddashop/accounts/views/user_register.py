from django.urls import reverse_lazy
from django.views import generic as views
from iddashop.accounts.forms import CreateProfileForm
from iddashop.common.views_mixins import LoginRegisterRedirect


class UserRegisterView(LoginRegisterRedirect, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register_user.html'
    success_url = reverse_lazy('home')
