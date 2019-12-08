from colorama import Fore
import random

_sizes = ["Tiny", "Small", "Medium", "Large", "Huge"]
_types = ["Baren", "Arid", "Terran", "Rich", "Gaia"]
_colors = [Fore.WHITE, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.GREEN]
_suffixes = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega"]
_population_limits = {
	"Tiny" : 10,
	"Small" : 100,
	"Medium" : 1000,
	"Large" : 10000,
	"Huge" : 100000
}

class Planet:

	def __init__(self, star, x, y):
		self.star = star
		self.name = star.name + " " + _suffixes[len(star.planets)]
		self.size = _sizes[random.randrange(len(_sizes))]
		
		i = random.randrange(len(_types))
		self.type = _types[i]
		self.color = _colors[i]
		
		self.population_limit = _population_limits[self.size]
		