from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from iddashop.accounts.forms import CreateProfileForm
from iddashop.accounts.models import Profile
from iddashop.common.views_mixins import RedirectToDashboard


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register_user.html'
    success_url = reverse_lazy('home')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    success_url = reverse_lazy('home')


class UserDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EditProfileView:
    pass


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    pass
