from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic import UpdateView
from iddashop.accounts.forms import CreateProfileForm, EditProfileForm
from iddashop.accounts.models import Profile, IddashopUser
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


class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'accounts/edit_user.html'

    def get_success_url(self):
        user_id = self.kwargs['pk']
        return reverse_lazy('show profile', kwargs={'pk': user_id})


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    pass


class ShowUsersView(views.ListView):
    model = IddashopUser
    template_name = 'accounts/list_users.html'
    context_object_name = 'users'


def toggle_staff_status(request, pk):
    user = IddashopUser.objects.get(pk=pk)
    user.is_staff = not user.is_staff
    user.save()

    return redirect('show all users')
