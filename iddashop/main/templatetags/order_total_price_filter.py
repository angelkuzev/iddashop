from django.template.defaulttags import register


@register.filter
def order_get_total_price(items):
    price = 0
    for item in items:
        price += float(item['price_per_item']) * int(item['quantity'])
    return price
