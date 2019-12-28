import random
import math

from ship_the_flying_dutchman import TheFlyingDutchman

class Player:

    def __init__(self, config):
        self.world_x = config.world_width // 2
        self.world_y = config.world_height // 2
        self.system_x = 0
        self.system_y = 0
        self.ground_x = 0
        self.ground_y = 0

        self.star = None
        self.body = None

        self.ship = TheFlyingDutchman()
    

    def fuel_cost(self, x, y):
        return round(math.sqrt((x-self.world_x)*(x-self.world_x) + (y-self.world_y)*(y-self.world_y)))


    def jump(self, x, y, target):
        self.ship.fuel -= self.fuel_cost(x, y)
        self.world_x = x
        self.world_y = y
        self.star = target
        self.system_x = 0
        self.system_y = 0
        self.body = self.star


    def jump_in_system(self, x, y, target):
        self.system_x = x
        self.system_y = y
        self.body = target


    def eat(self):
        try:
            self.ship.inventory.remove("Food (Rations)", 1)
        except inventory.ItemNotInStockError:
            print("We're out of food!")


    def drink(self):
        try:
            self.ship.inventory.remove("Food (Water)", 1)
        except inventory.ItemNotInStockError:
            print("We're out of water!")
        
