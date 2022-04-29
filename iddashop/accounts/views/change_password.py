from django.contrib.auth import views as auth_views
from iddashop.common.views_mixins import NotAuthRedirect


class ChangeUserPasswordView(NotAuthRedirect, auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'
