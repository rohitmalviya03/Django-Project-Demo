from django import template

register = template.Library()

@register.filter(name='productExits')


def productExits(product,cart):
    keys=cart.keys()
    for ids in keys:
        if int(ids) == product.id:
            return True
        

    return False  

@register.filter(name='quantity')
def quantity(product,cart):
    keys=cart.keys()
   
    for i in keys:
       if(product.id == int(i)):
          return cart.get(i)
       

@register.filter(name='cartprice')
def cartprice(product,cart):
    keys=cart.keys()
    
    for i in keys:
       if(product.id == int(i)):
          price=product.price*cart.get(i)
          print(product.id,price)
          return price
    
@register.filter(name='price_total')
def price_total(product  , cart):
    return product.price * quantity(product , cart)

   
@register.filter(name='total_cart_price')
def total_cart_price(products,cart):
    sum = 0 
    print(products)
    for p in products:
        sum += price_total(p , cart)

    return sum
    
       
    
