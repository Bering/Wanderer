import math
import random
from colorama import Fore

from body import Body

class Asteroid(Body):

    def __init__(self, star, angle, distance):
        name = 'Asteroid ' + str(random.randint(500,2000))
        super().__init__(star, name, angle, distance, Fore.WHITE, '.')
        