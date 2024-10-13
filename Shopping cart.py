class Orders:

    def __init__(self):
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def remove(self, item):
        self.cart.remove(item)

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        items = 'Cart Contents :'
        for i  in self.cart:
            items += i + ','
        return items

o = Orders()
o. add_to_cart('PS5')
o.add_to_cart('Headphones')
o.add_to_cart('Monitor')

print('Cart Size :', len(o))
print(o)