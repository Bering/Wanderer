from colorama import Fore
import random

from body import Body

_suffixes = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega"]
_sizes = ["Tiny", "Small", "Medium", "Large", "Huge"]
_types = ["Baren", "Arid", "Terran", "Rich", "Gaia", "Gas Giant"]
_colors = [Fore.WHITE, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.GREEN, Fore.LIGHTYELLOW_EX]

class Planet(Body):

	def __init__(self, star, angle, distance):
		i = random.randrange(len(_types))
		self.type = _types[i]
		self.color = _colors[i]
		
		if self.type == "Gas Giant":
			self.size = "Huge"
		else:
			self.size = _sizes[random.randrange(len(_sizes))]

		if self.size == "Huge":
			symbol = 'O'
		elif self.size == "Tiny":
			symbol = 'o'
		else:
			symbol = '0'

		name = 'Planet ' + star.name + " " + _suffixes[len(star.bodies)] + " (" + self.size + " " + self.type + ")"

		super().__init__(star, name, angle, distance, self.color, symbol)


class Mercury(Planet):
	def __init__(self, star):
		super().__init__(star, random.randint(0,359), 3)
		self.size = "Tiny"
		self.type = _types[0]
		self.color = _colors[0]
		self.symbol = 'o'
		self.name = 'Planet Mercury (Tiny Baren)'

class Venus(Planet):
	def __init__(self, star):
		super().__init__(star, random.randint(0,359), 4)
		self.size = "Medium"
		self.type = _types[0]
		self.color = _colors[0]
		self.symbol = '0'
		self.name = 'Planet Venus (Medium Baren)'

class Earth(Planet):
	def __init__(self, star):
		super().__init__(star, random.randint(0,359), 5)
		self.size = "Medium"
		self.type = _types[2]
		self.color = _colors[2]
		self.symbol = '0'
		self.name = 'Planet Earth (Medium Terran)'

class Mars(Planet):
	def __init__(self, star):
		super().__init__(star, random.randint(0,359), 6)
		self.size = "Small"
		self.type = _types[1]
		self.color = _colors[1]
		self.symbol = '0'
		self.name = 'Planet Mars (Small Arid)'

class Jupiter(Planet):
	def __init__(self, star):
		super().__init__(star, random.randint(0,359), 11)
		self.size = "Huge"
		self.type = _types[5]
		self.color = _colors[5]
		self.symbol = 'O'
		self.name = 'Planet Jupiter (Huge Gas Giant)'

class Saturn(Planet):
	def __init__(self, star):
		super().__init__(star, random.randint(0,359), 13)
		self.size = "Huge"
		self.type = _types[5]
		self.color = _colors[5]
		self.symbol = 'O'
		self.name = 'Planet Jupiter (Huge Gas Giant)'

class Uranus(Planet):
	def __init__(self, star):
		super().__init__(star, random.randint(0,359), 15)
		self.size = "Large"
		self.type = _types[5]
		self.color = _colors[5]
		self.symbol = '0'
		self.name = 'Planet Uranus (Large Gas Giant)'

class Neptune(Planet):
	def __init__(self, star):
		super().__init__(star, random.randint(0,359), 17)
		self.size = "Large"
		self.type = _types[5]
		self.color = _colors[5]
		self.symbol = '0'
		self.name = 'Planet Neptune (Large Gas Giant)'

