from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views
from iddashop.accounts.models import Profile


class UserDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'
