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
        self.world_x = 0
        self.world_y = 0
        self.system_x = config.system_width / 3
        self.system_y = config.system_height / 3
        self.ground_x = 0
        self.ground_y = 0

        self.environment = Environment.WORLD
        