from django import forms
from iddashop.common.views_mixins import BootstrapFormMixin
from iddashop.main.models import Item, Quantity, Order, Category


class CreateItemForm(BootstrapFormMixin, forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self._init_bootstrap_form_controls()

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


class AcceptOrderForm(BootstrapFormMixin, forms.ModelForm):
    expected_arrival = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = ('expected_arrival',)


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
