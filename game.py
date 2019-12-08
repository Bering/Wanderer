import shutil
import getch
import colorama

from world import World
from player import Player
#from ai import AI

class Game:

    def __init__(self, config):
        self.config = config
        self.world = World(config)
        self.player = Player(config)
        #self.ais = []
        #for n in range(config.nb_ais):
        #	self.ais.append(AI(self.world))

    def run(self):
        colorama.init()
        cols, lines = shutil.get_terminal_size()
        print("Wanderer v.alpha0")
        print("World size: " + str(self.config.world_width) + "x" + str(self.config.world_height))
        print("Window size: " + str(cols) + "x" + str(lines))
        print("Player position: " + str(self.player.world_x) + "," + str(self.player.world_y))

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
#		print('\x1b[2J')

        cols, lines = shutil.get_terminal_size()
        min_x = max(self.player.world_x - (cols / 2), 0)
        min_x = min(min_x, self.config.world_width - cols)
        max_x = min_x + cols

        min_y = max(self.player.world_y - (lines / 2), 0)
        min_y = min(min_y, self.config.world_height - lines)
        max_y = min_y + lines

        print("Viewing window: (" + str(min_x) + "," + str(min_y) + ") x (" + str(max_x) + "," + str(max_y) + ")")

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
