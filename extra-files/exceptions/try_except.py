ItemCart = 0
ItemQuantity = 0
ItemPrice = 0

# try/except example

try:
    with open('cart.txt', 'r') as f:
        f.read()


# Ways to call Exception are as follows
# except:
#     print('No cart')

# Another way of except calling is
except Exception as e:
    print(e)

# Another way of except calling is
# except FileNotFoundError:
#     print('File')

finally:
    print("Cleaning up resources")
