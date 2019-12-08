import getch
import colorama
import config
from world import World
from player import Player
#from ai import AI

class Application:

	def __init__(self, config):

		self.world = World(config)
		self.player = Player(config)
		#self.ais = []
		#for n in range(config.nb_ais):
		#	self.ais.append(AI(self.world))
		
		colorama.init()

	def print_world(self, config, player):
		min_x = player.ship.world_x - (config.view_width / 2)
		max_x = player.ship.world_x + (config.view_width / 2)
		min_y = player.ship.world_y - (config.view_height / 2)
		max_y = player.ship.world_y + (config.view_height / 2)
		for s in self.world.stars:
			if s.world_x >= min_x and s.world_x <= max_x and s.world_y >= min_y and s.world_y <= max_y:
				print(s.color +  '\x1b[' + s.world_y + ';' + s.world_x + 'H' + '*', end='')
		
		print(colorama.Style.RESET_ALL);

	def run(self):
		k = "?"
		while(k != 'q' and ord(k) != 27):
			print("> ", end='', flush=True)
			k = getch.getch()

			if k == 'q' or ord(k) == 27:
				self.cmd_quit()
			elif k == 'n':
				self.cmd_navigate()
			else:
				print("Unknown or unavailable command: " + k)
		
		print(colorama.Style.RESET_ALL)
		colorama.deinit()

	def cmd_quit(self):
		print("Quit")

	def cmd_navigate(self):
		print('Navigate to:')
		print(' 1) Altair')
		print(' 2) Aldebaran')
		print(' 3) Betelgeuse')
		print(' 4) Deneb')


print("Wanderer v.alpha0")
app = Application(config)
app.run()
