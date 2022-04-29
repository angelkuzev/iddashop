from django import forms
from iddashop.main.models import Item, Quantity, Category


class CreateItemForm(forms.ModelForm):
    s_size_quantity = forms.IntegerField(initial=0)
    m_size_quantity = forms.IntegerField(initial=0)
    l_size_quantity = forms.IntegerField(initial=0)
    price = forms.FloatField(initial=0.01)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'browser-default'
            }
        )
    )

    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Name'}))

    picture = forms.FileField()

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
        fields = ('picture', 'name', 'description', 'price', 'category', 's_size_quantity', 'm_size_quantity',
                  'l_size_quantity')
