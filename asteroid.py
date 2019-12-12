import random
import string
from colorama import Fore

from body import Body

class Asteroid(Body):

    def __init__(self, star, angle, distance):
        name = 'Asteroid (' + \
                str(random.randint(0, 500000)) + \
                ') ' + \
                str(random.randint(2000,2200)) + \
                ' ' + \
                random.choice(string.ascii_letters).upper() + \
                random.choice(string.ascii_letters).upper() + \
                str(random.randint(0,9)) + \
                str(random.randint(0,9))
        
        super().__init__(star, name, angle, distance, Fore.WHITE, '.')
        