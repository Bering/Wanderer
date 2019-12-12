import random
from colorama import Fore

from body import Body

class Station(Body):

    def __init__(self, star, angle, distance):
        name = 'Station ' + str(random.randint(100,200))
        super().__init__(star, name, angle, distance, Fore.YELLOW, '₴')
        