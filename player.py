import random
from enum import Enum

class Environment(Enum):
    GROUND = 1
    SYSTEM = 2
    WORLD = 3

class Player:

    def __init__(self, config):
        # self.world_x = random.randrange(config.world_width)
        # self.world_y = random.randrange(config.world_height)
        self.world_x = 1
        self.world_y = 1
        self.system_x = config.system_width // 5
        self.system_y = config.system_height // 5
        self.ground_x = 1
        self.ground_y = 1

        self.environment = Environment.WORLD
        self.star = None
        self.body = None
