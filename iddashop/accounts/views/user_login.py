from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from iddashop.common.views_mixins import LoginRegisterRedirect


class UserLoginView(LoginRegisterRedirect, auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()
