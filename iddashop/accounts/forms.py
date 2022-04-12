from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from iddashop.accounts.models import Profile
from iddashop.common.views_mixins import BootstrapFormMixin


class CreateProfileForm(BootstrapFormMixin, UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    date_of_birth = forms.DateField()
    phone_num = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(first_name=self.cleaned_data['first_name'],
                          last_name=self.cleaned_data['last_name'],
                          date_of_birth=self.cleaned_data['date_of_birth'],
                          phone_num=self.cleaned_data['phone_num'],
                          user=user)

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name'
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name'
                }
            ),
        }
