import colorama
import random

import config
from star import Star
import planet
from asteroid import Asteroid


class Sol(Star):
    def __init__(self, world, x, y):
        self.world_x = x
        self.world_y = y
        self.name = "Sol"
        self.owner = world.races["Humans"]
        self.color = colorama.Fore.BLUE
        self.bodies = []
        self.bodies.append(planet.Mercury(self))
        self.bodies.append(planet.Venus(self))
        self.bodies.append(planet.Earth(self))
        self.bodies.append(planet.Mars(self))
        self.bodies.append(planet.Jupiter(self))
        self.bodies.append(planet.Saturn(self))
        self.bodies.append(planet.Uranus(self))
        self.bodies.append(planet.Neptune(self))
        for a in range(config.max_asteroids_per_belt):
            angle = random.randint(0,359)
            self.bodies.append(Asteroid(self, angle, 8))
        self.fleets = []