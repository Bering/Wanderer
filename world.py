import colorama
import random

from race import Race
from star_names_stack import StarNamesStack
from star import Star
from sol import Sol
from planet import Planet
from asteroid import Asteroid
from comet import Comet
from station import Station
import fleet

class World:

    def __init__(self, config):
        self.races = {}
        self.races["Elders"] = Race("Elders", None, "E", colorama.Fore.LIGHTWHITE_EX)
        self.races["Humans"] = Race("Human", None, "H", colorama.Fore.WHITE)

        self.races["Rindhalu"] = Race("Rindhalu", None, "R", colorama.Fore.GREEN)
        self.races["Jeraptha"] = Race("Jeraptha", self.races["Rindhalu"], "J", colorama.Fore.BLUE)
        self.races["Ruhar"] = Race("Ruhar", self.races["Jeraptha"], "R", colorama.Fore.LIGHTCYAN_EX)

        self.races["Maxolhx"] = Race("Maxolhx", None, "M", colorama.Fore.LIGHTMAGENTA_EX)
        self.races["Thuranin"] = Race("Thuranin", self.races["Maxolhx"], "T", colorama.Fore.MAGENTA)
        self.races["Kristang"] = Race("Kristang", self.races["Thuranin"], "K", colorama.Fore.YELLOW)
        self.races["Bosphuraq"] = Race("Bosphuraq", self.races["Maxolhx"], "B", colorama.Fore.RED)
        self.races["Wurgalan"] = Race("Wurgalan", self.races["Bosphuraq"], "W", colorama.Fore.LIGHTYELLOW_EX)

        self._star_names = StarNamesStack()
        self.stars = []
        for n in range(len(self._star_names.names)):
            star = Star(
                config,
                random.randrange(config.world_width),
                random.randrange(config.world_height),
                self._star_names.pop(),
                self.get_random_owner_race(config)
            )
            self.stars.append(star)

        self._scatter_stars(config)
        self._scatter_stars(config)

        self.fleets = []


    def get_random_owner_race(self, config):
        chance = random.randint(1, 100)
        if chance > config.probability_is_owned:
            return None
        
        side = random.randint(0,1)
        chance = random.randint(1,100)
        if side == 0:
            if chance <= 33:
                return self.races["Rindhalu"]
            elif chance <= 66:
                return self.races["Jeraptha"]
            else:
                return self.races["Ruhar"]
        else:
            if chance <= 20:
                return self.races["Maxolhx"]
            elif chance <= 40:
                return self.races["Thuranin"]
            elif chance <= 60:
                return self.races["Bosphuraq"]
            elif chance <= 80:
                return self.races["Kristang"]
            else:
                return self.races["Wurgalan"]


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


    def add_sol(self, x, y):
        sol = Sol(self, x, y)
        self.stars.append(sol)
        return sol


    def get_body_counts(self):
        nb_stars = len(self.stars)
        nb_planets = 0
        nb_asteroids = 0
        nb_comets = 0
        nb_stations = 0

        for s in self.stars:
            for b in s.bodies:
                if isinstance(b, Planet):
                    nb_planets += 1
                elif isinstance(b, Asteroid):
                    nb_asteroids += 1
                elif isinstance(b, Comet):
                    nb_comets += 1
                elif isinstance(b, Station):
                    nb_stations += 1
    
        return (nb_stars, nb_planets, nb_asteroids, nb_comets, nb_stations)


    def areAllied(self, a, b):
        if a == b:
            return True

        if a == None or b == None:
            return False
        
        parentA = a
        while parentA.parent:
            parentA = parentA.parent
        
        parentB = b
        while parentB.parent:
            parentB = parentB.parent
        
        return (parentA == parentB)


    def areEnemies(self, a, b):
        return not self.areAllied(a, b)


    def tick(self, config):
        for s in self.stars:
            for b in s.bodies:
                if isinstance(b, Planet) or isinstance(b, Station):
                    chance = random.randint(1, 100)
                    if chance <= config.probability_fleet_spawn:
                        self.fleets.append(fleet.Fleet(self, b, fleet.Orders.RANDOM))
                        
