import random

from inventory import Inventory, InventoryItem


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
        for i in config.trade_items_stack.items:
            chance = random.randint(1, 100)
            if chance < i.rarity:
                twenty_five_percent = i.price * 25 // 100
                price = random.randint(
                    i.price - twenty_five_percent,
                    i.price + twenty_five_percent)
                self.inventory.items.append(InventoryItem(
                    i.name,
                    random.randint(1,1000),
                    price,
                    0))

class Research(StationService):
    def __init__(self, station):
        super().__init__(station, "Researach")
