import random

from inventory import Inventory, InventoryItem
from inventory import Inventory


class StationService:
    def __init__(self, station, name):
        self.station = station
        self.name = name


class Repair(StationService):
    def __init__(self, station):
        super().__init__(station, "Repair")

class Rearm(StationService):
    def __init__(self, station):
        super().__init__(station, "Rearm")

class Trade(StationService):
    def __init__(self, station, config):
        super().__init__(station, "Trade")

        self.inventory = Inventory(10000)
        self.prices = {}

        # pick items at random and fill inventory with random amount of it
        while self.inventory.size < self.inventory.size_max:
            i = config.trade_items_stack.items[random.randrange(len(config.trade_items_stack.items))]
            
            remaining_space = self.inventory.size_max - self.inventory.size
            if i.size > remaining_space:
                continue

            chance = random.randint(1, 100)
            if chance <= i.rarity:
                quantity = remaining_space // i.size
                self.inventory.add(i.name, i.size, random.randint(1, quantity))
                twenty_five_percent = i.price * 25 // 100
                price = random.randint(
                    i.price - twenty_five_percent,
                    i.price + twenty_five_percent)
                self.prices[i.name] = price

class Research(StationService):
    def __init__(self, station):
        super().__init__(station, "Researach")
