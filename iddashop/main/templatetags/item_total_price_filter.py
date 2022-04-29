from django.template.defaulttags import register


@register.filter
def get_total_price(item):
    return float(item['price_per_item']) * int(item['quantity'])


@register.filter
def get_total_price_order(item):
    return float(item.item.price * item.item_quantity)
