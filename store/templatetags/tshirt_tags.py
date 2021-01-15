from django import template
from math import floor

register = template.Library()

@register.filter #decorator
def rupee(number):
    return f'₹ {number}'


@register.filter #decorator
def cal_total_payable_amount(cart):
    total = 0
    for c in cart: #iterating loop in cart to get all the value 
        discount  = c.get('tshirt').discount #keeping discont in varialble 
        price = c.get('size').price #keeping price in variable
        sale_price = clc_sale_price(price , discount) #already defined function so passing two values as argument 
        total_of_single_product = sale_price* c.get('quantity')
        total = total + total_of_single_product

    return(total)



@register.simple_tag

def min_price(tshirt):
    size = tshirt.sizevariant_set.all().order_by('price').first()
    return floor(size.price)

@register.simple_tag

def multiply(a,b):
   return a*b

@register.simple_tag

def clc_sale_price(price, discount):
   return floor(price - (price * (discount /100)))



@register.simple_tag

def sale_price(tshirt):
    price = min_price(tshirt)
    discount = tshirt.discount
    return floor(price - (price * (discount /100)))


@register.simple_tag

def get_active_size_button_class(active_size, size):
    if active_size == size:
        return "dark"
    
    return "light"
