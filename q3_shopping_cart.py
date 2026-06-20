#Part-A:Spot the Bug
def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))
#Output
['apple']
['apple', 'banana']
['bread', 'milk']
['apple', 'banana', 'eggs']
#Why the error happens?
#cart=[] is a mutable default argument.

#Python creates this list only once, so all function calls that don't pass a cart share the same list.

#That's why:

add_item("apple")   # ['apple']
add_item("banana")  # ['apple', 'banana']
add_item("eggs")    # ['apple', 'banana', 'eggs']

#all modify the same default list.

#Part-B: Fix It
def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

#Part-C:Build the Cart
def create_cart(owner, discount=0):
    return {"owner": owner, "items": [], "discount": discount}

def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})

def update_price(t, new_price):
    try:
        t[0] = new_price
    except TypeError as e:
        print("Error:", e)

def calculate_total(cart):
    total = sum(i["price"] * i["qty"] for i in cart["items"])
    return total - (total * cart["discount"] / 100)

cart1 = create_cart("Niranjanaa", 10)
add_to_cart(cart1, "Laptop", 50000)
add_to_cart(cart1, "Mouse", 1000, 2)

cart2 = create_cart("Priya", 5)
add_to_cart(cart2, "Keyboard", 1500)
add_to_cart(cart2, "Headphones", 2500)

print("Cart 1:", cart1)
print("Total:", calculate_total(cart1))

print("\nCart 2:", cart2)
print("Total:", calculate_total(cart2))

prices = (100, 200, 300)
update_price(prices, 500)

#Discussion points
# 1. Why is discount=0 safe but cart=[] dangerous?
# discount=0 is immutable. It cannot be modified.
# cart=[] is mutable. If changed in one function call,
# the same list is reused in future calls.

# 2. Difference between rebinding and mutating?
# Rebinding:
# x = [1, 2]
# x = [3, 4]
# Variable now points to a new object.
# Mutating:
# x.append(5)
# Same object is modified.

# 3. Which are mutable?
# list  -> Mutable
# tuple -> Immutable
# dict  -> Mutable
# set   -> Mutable
# str   -> Immutable
# int   -> Immutable

# 4. When you pass a list into a function and modify it, do changes reflect outside?
# Yes. Because both the caller and function refer to the same list object. Mutating the list changes theoriginal object itself.