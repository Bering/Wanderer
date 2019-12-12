import random
import string
from colorama import Fore

from body import Body

class Comet(Body):

    def __init__(self, star, angle, distance):
        name = 'Comet P/' + \
                str(random.randint(2000,2200)) + \
                ' ' + \
                random.choice(string.ascii_letters).upper() + \
                str(random.randint(0,9)) + \
                str(random.randint(0,9))
        
        # Tail away from the star :-)
        if angle < 23:
            symbol = '—'
        elif angle < 68:
            symbol = '\\'
        elif angle < 113:
            symbol = '|'
        elif angle < 158:
            symbol = '/'
        elif angle < 203:
            symbol = '—'
        elif angle < 248:
            symbol = '\\'
        elif angle < 293:
            symbol = '|'
        elif angle < 338:
            symbol = '/'
        else:
            symbol = '—'

        super().__init__(star, name, angle, distance, Fore.WHITE, symbol)
        