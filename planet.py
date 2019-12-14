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
