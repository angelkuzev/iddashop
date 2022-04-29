from django.shortcuts import redirect
from iddashop.main.models import Quantity


def remove_from_cart(request, pk, size):
    item = [item for item in request.session['cart'] if item['pk'] == pk and item['size'] == size][0]

    cart = request.session['cart']
    cart = list(filter(lambda i: i['pk'] != pk or i['size'] != size, cart))
    request.session['cart'] = cart

    field_name = f"{size.lower()}_size_quantity"
    quantity = Quantity.objects.get(pk=pk)
    stock = Quantity.objects.values_list(field_name, flat=True).get(pk__exact=pk)
    stock += item['quantity']
    setattr(quantity, field_name, stock)
    quantity.save()

    return redirect('show cart')