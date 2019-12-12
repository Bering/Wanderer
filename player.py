import random

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


    def jump(self, x, y, target):
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
