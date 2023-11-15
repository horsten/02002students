"""This file contains the project's code and solution."""
class Item:
    """A class to represent an inventory item.""" 

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __lt__(self, other):
        return self.quantity*self.price < other.quantity*other.price
    def __gt__(self, other):
        return self.quantity*self.price > other.quantity*other.price
    def __eq__(self, other):
        return self.quantity*self.price == other.quantity*other.price    

class Inventory:
    """A class to represent an inventory of items."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def calculate_total_value(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

    def __lt__(self, other):
        return self.calculate_total_value() < other.calculate_total_value()
    def __gt__(self, other):
        return self.calculate_total_value() > other.calculate_total_value()
    def __eq__(self, other):
        return self.calculate_total_value() == other.calculate_total_value()
