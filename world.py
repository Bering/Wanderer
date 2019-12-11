import random
from star import Star
from planet import Planet
from asteroid import Asteroid
from star_names_stack import StarNamesStack

class World:

    def __init__(self, config):
        self._star_names = StarNamesStack()
        self.stars = []
        for n in range(len(self._star_names.names)):
            star = Star(
                config,
                random.randrange(config.world_width),
                random.randrange(config.world_height),
                self._star_names.pop()
            )
            self.stars.append(star)

        self._scatter_stars(config)
        self._scatter_stars(config)

    def _scatter_stars(self, config):
        pass
        # for s in self.stars:
        # 	for o in self.stars:
        # 		if (o == s): continue

        # 		if (abs(s.rect.x - o.rect.x) + abs(s.rect.y - o.rect.y) < 32):

        # 			if (s.rect.x < o.rect.x):
        # 				if (s.rect.x > 32):
        # 					s.rect.move_ip(-32, 0)
        # 					s.name_rect.move_ip(-32, 0)
        # 				else:
        # 					s.rect.move_ip(64, 0)
        # 					s.name_rect.move_ip(64, 0)
        # 			else:
        # 				if (s.rect.x < config.window_width - 16):
        # 					s.rect.move_ip(32, 0)
        # 					s.name_rect.move_ip(32, 0)
        # 				else:
        # 					s.rect.move_ip(-64, 0)
        # 					s.name_rect.move_ip(-64, 0)


    def get_body_counts(self):
        nb_stars = len(self.stars)
        nb_planets = 0
        nb_asteroids = 0

        for s in self.stars:
            for b in s.bodies:
                if isinstance(b, Planet):
                    nb_planets += 1
                elif isinstance(b, Asteroid):
                    nb_asteroids += 1
    
        return (nb_stars, nb_planets, nb_asteroids)
    
