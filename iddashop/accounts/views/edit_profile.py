from django.urls import reverse_lazy
from django.views.generic import UpdateView
from iddashop.accounts.forms import EditProfileForm
from iddashop.accounts.models import Profile


class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'accounts/edit_user.html'

    def get_success_url(self):
        user_id = self.kwargs['pk']
        return reverse_lazy('show profile', kwargs={'pk': user_id})
