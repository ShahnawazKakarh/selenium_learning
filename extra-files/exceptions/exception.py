ItemCart = 0
ItemQuantity = 0
ItemPrice = 0

# if item-cart is not equal to 2
if ItemCart != 2:
    raise Exception('Item is not in the cart')

# if item-quantity is not equal to 2
if ItemQuantity != 2:
    pass

# if item-price is not equal to zero it will fail
assert (ItemPrice != 0)
