from django.shortcuts import redirect
from iddashop.main.models import Item, Quantity


def add_to_cart(request, pk):
    size = request.POST['group1']
    item_db = Item.objects.get(pk=pk)

    item = {
        'pk': pk,
        'size': size,
        'title': item_db.name,
        'image_url': item_db.picture.url,
        'quantity': 1,
        'price_per_item': item_db.price,
    }

    if 'cart' not in request.session:
        request.session['cart'] = [item]
    else:
        items = request.session['cart']

        exist = next((item for item in items if item['pk'] == pk and item['size'] == size), None)
        if exist:
            exist['quantity'] += 1
        else:
            items.append(item)

        request.session['cart'] = items

    field_name = f"{str(item['size']).lower()}_size_quantity"
    quantity = Quantity.objects.get(pk=pk)
    stock = Quantity.objects.values_list(field_name, flat=True).get(pk__exact=pk)
    stock -= 1
    setattr(quantity, field_name, stock)
    quantity.save()

    return redirect('show cart')