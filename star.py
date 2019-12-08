from colorama import Fore, Style
from planet import Planet
import random

_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
_styles = [Style.NORMAL, Style.BRIGHT]

class Star:

	def __init__(self, name, x, y):
		self.world_x = x
		self.world_y = y
		self.name = name
		self.color = _colors[random.randrange(len(_colors))]
		self.style = _styles[random.randrange(len(_styles))]
		self.planets = []

	def add_planet(self, x, y):
		p = Planet(self, x, y)
		self.planets.append(p)
