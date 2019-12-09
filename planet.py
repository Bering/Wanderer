from colorama import Fore
import random

from body import Body

_suffixes = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega"]
_sizes = ["Tiny", "Small", "Medium", "Large", "Huge"]
_types = ["Baren", "Arid", "Terran", "Rich", "Gaia"]
_colors = [Fore.WHITE, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.GREEN]

class Planet(Body):

	def __init__(self, star, x, y):
		self.size = _sizes[random.randrange(len(_sizes))]
		if self.size == "HUGE":
			symbol = 'O'
		elif self.size == "Tiny":
			symbol = 'o'
		else:
			symbol = '0'

		i = random.randrange(len(_types))
		self.type = _types[i]
		self.color = _colors[i]
		
		name = 'Planet ' + star.name + " " + _suffixes[len(star.bodies)] + " (" + self.size + " " + self.type + ")"

		super().__init__(star, name, x, y, symbol, self.color)
