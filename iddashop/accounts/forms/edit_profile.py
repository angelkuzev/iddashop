from django import forms
from iddashop.accounts.models import Profile


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    date_of_birth = forms.DateField()
    phone_num = forms.CharField()
    full_address = forms.CharField()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'date_of_birth', 'phone_num', 'full_address')
