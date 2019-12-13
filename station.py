import random
from colorama import Fore

from body import Body
import station_service

# TODO: Different sizes, with max inventory and max number of services

class Station(Body):

    def __init__(self, config, star, angle, distance):
        name = 'Station ' + str(random.randint(100,200))
        super().__init__(star, name, angle, distance, Fore.YELLOW, '₴')
        
        self.services = []
        chance = random.randint(1, 100)
        if chance <= config.probability_repair:
            self.services.append(station_service.Repair(self))
        chance = random.randint(1, 100)
        if chance <= config.probability_rearm:
            self.services.append(station_service.Rearm(self))
        chance = random.randint(1, 100)
        if chance <= config.probability_trade:
            self.services.append(station_service.Trade(self, config))
        chance = random.randint(1, 100)
        if chance <= config.probability_research:
            self.services.append(station_service.Research(self))
        