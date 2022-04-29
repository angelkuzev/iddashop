from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class UserLogoutView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    success_url = reverse_lazy('home')
