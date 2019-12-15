import random

from inventory import Inventory


class StationService:
    def __init__(self, station, name):
        self.station = station
        self.name = name


class News(StationService):
    def __init__(self, station):
        super().__init__(station, "News")


class Repair(StationService):
    def __init__(self, station):
        super().__init__(station, "Repair")


class Refuel(StationService):
    def __init__(self, station):
        super().__init__(station, "Refuel")


class Plunder(StationService):
    def __init__(self, station, config):
        super().__init__(station, "Plunder")

        self.inventory = Inventory(10000)

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


class Research(StationService):
    def __init__(self, station):
        super().__init__(station, "Research")
