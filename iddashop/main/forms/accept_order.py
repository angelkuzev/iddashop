from django import forms
from iddashop.main.models import Order


class AcceptOrderForm(forms.ModelForm):
    expected_arrival = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = ('expected_arrival',)
