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

    def __init__(self, config, x, y, name):
        self.world_x = x
        self.world_y = y
        self.name = name
        self.color = _colors[random.randrange(len(_colors))]
        self.style = _styles[random.randrange(len(_styles))]
        self.bodies = []

        min_distance = 3
        max_distance = min(config.system_width, config.system_height) - 3
        for n in range(min_distance, max_distance + 1, 3):
            chance = random.randint(1, 100)
            if len(self.bodies) < config.max_planet_per_system \
            and chance <= config.probability_planet:
                angle = random.randint(0, 359)
                self.bodies.append(Planet(self, angle, n))
            else:
                chance = random.randint(1, 100)
                if chance <= config.probability_asteroids:
                    nb_asteroids = random.randrange(config.max_asteroids_per_belt)
                    for a in range(nb_asteroids):
                        angle = random.randint(0, 359)
                        self.bodies.append(Asteroid(self, angle, n))
                else:
                    chance = random.randint(1, 100)
                    if chance <= config.probability_station:
                        angle = random.randint(0, 359)
                        self.bodies.append(Station(self, angle, n))
                    else:
                        chance = random.randint(1, 100)
                        if chance <= config.probability_comet:
                            angle = random.randint(0, 359)
                            self.bodies.append(Comet(self, angle, n))


    def _scatter_bodies(self, config, star):
        star_x = config.system_width // 2
        star_y = config.system_height // 2

        # for p in self.bodies:

            # # Move planets out of (scaled up) star's way
            # if screen_center_x - 64 < p.rect.x < screen_center_x + 64:
            # 	if screen_center_y - 64 < p.rect.y < screen_center_y + 64:
            # 		p.rect.x = random.randrange(config.window_width - 32) + 16
            # 		p.rect.y = random.randrange(config.window_height - 32) + 16
            # 		p.name_rect.midtop = p.rect.midbottom

            # # Move planets out of each other's way
            # for o in star.planets:
            # 	if (o == p): continue

            # 	if (abs(p.rect.x - o.rect.x) + abs(p.rect.y - o.rect.y) < 32):

            # 		if (p.rect.x < o.rect.x):
            # 			if (p.rect.x > 32):
            # 				p.rect.move_ip(-32, 0)
            # 				p.name_rect.move_ip(-32, 0)
            # 			else:
            # 				p.rect.move_ip(64, 0)
            # 				p.name_rect.move_ip(64, 0)
            # 		else:
            # 			if (p.rect.x < config.window_width - 16):
            # 				p.rect.move_ip(32, 0)
            # 				p.name_rect.move_ip(32, 0)
            # 			else:
            # 				p.rect.move_ip(-64, 0)
            # 				p.name_rect.move_ip(-64, 0)

    def get_body_at(self, x, y):
        for b in self.bodies:
            if b.body_x == x and b.body_y == y:
                return b
        
        return None
    