from uu import *

class NotEnoughRight(Exception):
    def __init__(self, *value) -> None:
        self.value = value

    def __str__(self) -> str:
        return "You have not enought rights for this " + repr(self.value)
    
class Item:
    def __init__(self, name, price) -> None:
        self.name = name 
        self.price = price

class Order:
    def __init__(self) -> None:
        if id_ is None:
            id_ = uuid1().int
        self.id = id_
        self.items = []
        self.total = 0

    def __add__(self, item):
        self.items.append(item)
        self.total += item.price
        print(f"{item} succesfully added")

    def __sub__(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total -= item.price

    def __str__(self) -> str:
        msg = f"Items\n"
        if self.items:
            for item in self.items:
                msg += f"{item.name}:{item.price}\n"
        msg += f"Total: {self.total}"
        return msg    


class Person:

    def add(self, *args):
        raise NotEnoughRight
    
    def sub(self, *args):
        raise NotEnoughRight

    def view(self, *args):
        raise NotEnoughRight

    def check(self, *args):
        raise NotEnoughRight

    def confirm(self, *args):
        raise NotEnoughRight

    def complete(self, *args):
        raise NotEnoughRight
    

class Customer(Person):
    def view(self, order):
        return str(order)
    
class Seller(Person):
    def add(self, item, order=None):
        if order is None:
            order = Order
        order + item
        return order
    
    def sub(self, item, order):
        order - item

    def view(self, order):
        return str(ord)
    
    def confirm(self, order, manufacturer):
        manufacturer.add(order)

class Manufacturer(Person):
    def __init__(self) -> None:
        self.orders = dict()

    @property
    def order_list(self):
        return list(self.orders.keys())
    
    def add(self, order):
        self.orders[order.id] = False

    def view(self, order):
        if order.id in self.orders:
            return self.orders[order.id]

    def check(self, order):
        return self.orders[order.id]
    
    def complete(self, order):
        if order.id in self.orders:
            self.orders[order.id] = True





ball = Item("ball", 10)
cap = Item("cap", 5)
bag = Item("bag", 15)

seller = Seller()
customer = Customer()
manufacturer = Manufacturer()

new_order = seller.add(ball)
print(seller.view(new_order))
print(customer.view(new_order))

seller.add(cap, new_order)
print(customer.view(new_order))

seller.add(bag, new_order)
print(customer.view(new_order))

seller.confirm(new_order, manufacturer)
print(manufacturer.order_list)
print(manufacturer.check(new_order))
print(manufacturer.complete(new_order))
print(manufacturer.check(new_order))

