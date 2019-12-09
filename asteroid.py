import random
from colorama import Fore

from body import Body

class Asteroid(Body):

    def __init__(self, star, x, y):
        name = 'Asteroid ' + str(random.randint(500,2000))
        super().__init__(star, name, x, y, '.', Fore.WHITE)
        