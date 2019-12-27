import random
from colorama import Fore, Style

import body
from planet import Planet
from asteroid import Asteroid
from station import Station
from comet import Comet

_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
_styles = [Style.NORMAL, Style.BRIGHT]

class Star:

    def __init__(self, config, x, y, name, owner):
        self.world_x = x
        self.world_y = y
        self.name = name
        self.owner = owner
        self.color = _colors[random.randrange(len(_colors))]
        self.bodies = []
        self.fleets = []

        min_distance = 3
        max_distance = min(config.system_width, config.system_height) // 2
        for n in range(min_distance, max_distance + 1, 3):
            chance = random.randint(1, 100)
            if len(self.bodies) < config.max_planet_per_system \
            and chance <= config.probability_planet:
                angle = random.randint(0, 359)
                self.bodies.append(Planet(self, angle, n))
            else:
                chance = random.randint(1, 100)
                if chance <= config.probability_asteroids:
                    nb_asteroids = random.randrange(
                        config.max_asteroids_per_belt // 3,
                        config.max_asteroids_per_belt)
                    for a in range(nb_asteroids):
                        angle = random.randint(0, 359)
                        self.bodies.append(Asteroid(self, angle, n))
                else:
                    chance = random.randint(1, 100)
                    if chance <= config.probability_station:
                        angle = random.randint(0, 359)
                        self.bodies.append(Station(config, self, angle, n))
                    else:
                        chance = random.randint(1, 100)
                        if chance <= config.probability_comet:
                            angle = random.randint(0, 359)
                            self.bodies.append(Comet(self, angle, n))


    def get_body_at(self, x, y):
        for b in self.bodies:
            if b.body_x == x and b.body_y == y:
                return b
        
        return None
    