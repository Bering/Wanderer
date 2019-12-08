from enum import Enum

class Environment(Enum):
    GROUND = 1
    SYSTEM = 2
    WORLD = 3

class Player:

    def __init__(self, config):
        self.world_x = config.world_width / 2
        self.world_y = config.world_height / 2
        self.system_x = config.system_width / 3
        self.system_y = config.system_height / 3
        self.ground_x = 0
        self.ground_y = 0

        self.environment = Environment.WORLD
        