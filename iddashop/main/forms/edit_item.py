from django import forms
from iddashop.main.models import Item, Quantity, Category


class EditItemForm(forms.ModelForm):
    s_size_quantity = forms.IntegerField()
    m_size_quantity = forms.IntegerField()
    l_size_quantity = forms.IntegerField()
    price = forms.FloatField()
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'browser-default'
            }
        )
    )



    def save(self, commit=True):
        item = super().save(commit=commit)

        quantity = Quantity.objects.get(pk=item.pk)
        quantity.s_size_quantity = self.cleaned_data['s_size_quantity']
        quantity.m_size_quantity = self.cleaned_data['m_size_quantity']
        quantity.l_size_quantity = self.cleaned_data['l_size_quantity']

        if commit:
            quantity.save()
        return item

    class Meta:
        model = Item
        fields = ('picture', 'name', 'description', 'price', 'category', 's_size_quantity', 'm_size_quantity',
                  'l_size_quantity')

