from django import forms
from iddashop.main.models import Category


class AddCategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=Category.NAME_MAX_LENGTH,
        min_length=Category.NAME_MIN_LENGTH
    )

    gender = forms.ChoiceField(
        choices=Category.GENDERS,
        widget=forms.Select(attrs={'class': 'browser-default'})
    )

    class Meta:
        model = Category
        fields = ('gender', 'name')
