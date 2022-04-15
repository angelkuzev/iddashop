from django import forms
from django.forms import ModelForm, HiddenInput
from iddashop.common.views_mixins import BootstrapFormMixin
from iddashop.main.models import Item, Quantity, Order, OrderedItem


class CreateItemForm(BootstrapFormMixin, ModelForm):
    s_size_quantity = forms.IntegerField(initial=0)
    m_size_quantity = forms.IntegerField(initial=0)
    l_size_quantity = forms.IntegerField(initial=0)
    price = forms.FloatField(initial=0.01)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        item = super().save(commit=commit)

        quantity = Quantity(s_size_quantity=self.cleaned_data['s_size_quantity'],
                            m_size_quantity=self.cleaned_data['m_size_quantity'],
                            l_size_quantity=self.cleaned_data['l_size_quantity'],
                            item=item,
                            )

        if commit:
            quantity.save()
        return item

    class Meta:
        model = Item
        fields = ('picture', 'name', 'description', 'price', 's_size_quantity', 'm_size_quantity', 'l_size_quantity')
