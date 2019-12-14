

class InventoryItem:
    def __init__(self, name, unit_size, quantity):
        self.name = name
        self.unit_size = unit_size
        self.quantity = quantity


class WouldOverflowError(Exception):
    def __init__(self, name, unit_size, quantity, size_available):
        self.name = name
        self.unit_size = unit_size
        self.quantity = quantity
        self.size_available = size_available


class ItemNotInStockError(Exception):
    def __init__(self, name):
        self.name = name


class WouldUnderflowError(Exception):
    def __init__(self, name, quantity_stocked):
        self.name = name
        self.quantity_stocked = quantity_stocked


class Inventory:
    def __init__(self, size):
        self.size_max = size
        self.size = 0
        self.items = {}


    def add(self, name, unit_size, quantity):

        if self.size + (unit_size * quantity) > self.size_max:
            raise WouldOverflowError(name, unit_size, quantity, self.size_max - self.size)
        
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = InventoryItem(name, unit_size, quantity)

        self.size += (unit_size * quantity)

    
    def remove(self, name, quantity):

        if name not in self.items:
            raise ItemNotInStockError(name)

        i = self.items[name]

        if i.quantity < quantity:
            raise WouldUnderflowError(name, i.quantity)
        
        i.quantity -= quantity
        if i.quantity == 0:
            del self.items[name]
        
        self.size -= i.unit_size * quantity
    
