from django.views import generic as views
from iddashop.accounts.models import IddashopUser
from iddashop.common.views_mixins import NotAdminRedirect


class ManageUsersView(NotAdminRedirect, views.ListView):
    model = IddashopUser
    template_name = 'accounts/manage_users.html'
    context_object_name = 'users'

    def get_queryset(self):
        qs = self.model.objects.order_by('-date_joined')
        return qs
