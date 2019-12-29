import random
import math

import config
from ship_the_flying_dutchman import TheFlyingDutchman

class Player:

    def __init__(self):
        self.world_x = config.world_width // 2
        self.world_y = config.world_height // 2
        self.system_x = 0
        self.system_y = 0
        self.ground_x = 0
        self.ground_y = 0

        self.star = None
        self.body = None

        self.ship = TheFlyingDutchman()
    

    def get_distance(self, x, y):
        return round(math.sqrt((x - self.world_x) ** 2 + (y - self.world_y) ** 2))


    def get_fuel_cost(self, x, y):
        return self.get_distance(x, y) ** 2


    # remember that target can be empty space, not always a star, hence x, y
    def jump(self, x, y, target):

        # TODO: raise errors instead, and let the game class handle display

        if self.get_distance(x, y) > config.maximum_jump_distance:
            print("Cannot jump that far! Maximum is " + str(config.maximum_jump_distance) + ".\n")
            return False
        
        fuel_cost = self.get_fuel_cost(x, y)
        if self.ship.fuel < fuel_cost:
            print("Not enough gas!\n")
            return False
        
        self.ship.fuel -= fuel_cost
        self.world_x = x
        self.world_y = y
        self.star = target
        self.system_x = 0
        self.system_y = 0
        self.body = self.star
        return True


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
        
