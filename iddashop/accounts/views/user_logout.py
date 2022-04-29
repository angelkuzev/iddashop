from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class UserLogoutView(auth_views.LogoutView):
    success_url = reverse_lazy('home')
