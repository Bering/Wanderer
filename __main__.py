import os
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

	def run(self):
		k = "?"
		while(k != 'q' and ord(k) != 27):
			print("> ", end='', flush=True)
			k = getch.getch()

			if k == 'q' or ord(k) == 27:
				self.cmd_quit()
			elif k == 'j':
				self.cmd_jump()
			elif k == 't':
				self.cmd_test()
			else:
				print("Unknown or unavailable command: " + k)
		
		print(colorama.Style.RESET_ALL)
		colorama.deinit()

	def cmd_quit(self):
		print("Quit")

	def cmd_jump(self):
		
		# clear screen
		print('\x1b[2J')

		cols, lines = os.get_terminal_size()
		min_x = self.player.world_x - (cols / 2)
		max_x = self.player.world_x + (cols / 2)
		min_y = self.player.world_y - (lines / 2)
		max_y = self.player.world_y + (lines / 2)

		print("World size: " + str(config.world_width) + "," + str(config.world_height))
		print("Player position: " + str(self.player.world_x) + "," + str(self.player.world_y))
		print("Window size: " + str(cols) + "," + str(lines))
		print(str(min_x) + "," + str(max_x) + " - " + str(min_y) + "," + str(max_y))

		for s in self.world.stars:
			if s.world_x < min_x or s.world_x > max_x \
			or s.world_y < min_y or s.world_y > max_y:
				continue

			sv_x = s.world_x - self.player.world_x
			sv_y = s.world_y - self.player.world_y
			print('\x1b[' + str(sv_y) + ';' + str(sv_x) + 'H' + s.color + '*', end='')
		
		print(colorama.Style.RESET_ALL);
		print('\x1b[' + str(lines) + ';0H' + 'Jump to: ')

	def cmd_test(self):
		print('\x1b[2J')
		print('\x1b[0;0H' + 'Test')


print("Wanderer v.alpha0")
app = Application(config)
app.run()
