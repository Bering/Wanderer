
class InventoryItem:
    def __init__(self, name, price, unit_size, quantity):
        self.name = name
        self.price = price
        self.unit_size = unit_size
        self.quantity = quantity


class Inventory:
    def __init__(self, size):
        self.size_max = size
        self.size = 0
        self.items = []


    def buy(name, price, unit_size, quantity):
        if self.size + (unit_size * quantity) > self.size_max:
            # TODO: throw error instead
            return

        item = None
        for i in self.items:
            if i.name == name and i.price == price:
                item = i
                break
        
        if item == None:
            self.items.append(name, price, unit_size, quantity)
        else:
            item.quantity += quantity

        self.size += (unit_size * quantity)
        return (prize * quantity)

    
    def sell(name, quantity, size, price):
        matches = []
        for i in self.items:
            if i.name == name:
                matches.append(i)
        
        if len(matches) == 0:
            raise Exception("No such item in stock: " + name)

        matches.sort(key=lambda x: x.price, reverse=True)

        quantity_stocked = 0
        for i in matches:
            quantity_stocked += i.quantity
        
        if quantity_stocked < quantity:
            raise Exception("Not enough to sell. Only " + str(quantity_stocked) + " in stock")
        
        payback = 0
        quantity_removed = 0
        while quantity_removed < quantity:
            i = matches[0]
            if i.quantity >= quantiy:
                quantity_to_remove = quantity
            else:
                quantity_to_remove = quantity - i.quantity

            i.quantity -= quantity_to_remove
            if i.quantity == 0:
                self.items.remove(i)
            
            quantity_removed += quantity_to_remove
            self.size += size * quantity_to_remove
            payback += price * quantity

            del matches[0]
        
        return payback