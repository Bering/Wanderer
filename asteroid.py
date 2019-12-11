import math
import random
from colorama import Fore

from body import Body

class Asteroid(Body):

    def __init__(self, star, angle, distance):
        name = 'Asteroid ' + str(random.randint(500,2000))
        x = round(distance * math.cos(math.radians(angle)))
        y = round(distance * math.sin(math.radians(angle)))
        super().__init__(star, name, x, y, Fore.WHITE, '.')
        