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
        print("Wanderer v.alpha0")
        print("World size: " + str(self.config.world_width) + "x" + str(self.config.world_height))
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
        
        cols, lines = shutil.get_terminal_size()
        min_x = max(self.player.world_x - (cols / 2), 0)
        min_x = min(min_x, self.config.world_width - cols)
        max_x = min_x + cols - 1

        min_y = max(self.player.world_y - (lines / 2), 0)
        min_y = min(min_y, self.config.world_height - lines)
        max_y = min_y + lines - 1

        # clear screen
        print('\x1b[2J')

        #print("Window size: " + str(cols) + "x" + str(lines))
        #print("Viewing: (" + str(min_x) + "," + str(min_y) + ") - (" + str(max_x) + "," + str(max_y) + ")")

        for s in self.world.stars:
            if s.world_x < min_x or s.world_x > max_x \
            or s.world_y < min_y or s.world_y > max_y:
                continue

            sv_x = s.world_x - min_x
            sv_y = s.world_y - min_y
            print('\x1b[' + str(sv_y) + ';' + str(sv_x) + 'H' + s.style + s.color + '*', end='')
        
        print(
            '\x1b[' + str(self.player.world_y - min_y) + ';' + str(self.player.world_x - min_x) + 'H' + 
            colorama.Style.BRIGHT + 
            colorama.Fore.WHITE + 
            '@'
        )

        print(colorama.Style.RESET_ALL);

        k = '?'
        cursor_x = self.player.world_x - min_x
        cursor_y = self.player.world_y - min_y
        while(ord(k) != 13 and ord(k) != 27):

            target = '(' + str(cursor_x) + ',' + str(cursor_y) + ')'
            for s in self.world.stars:
                if s.world_x == cursor_x and s.world_y == cursor_y:
                    target = s.name
                    break

            print('\x1b[' + str(lines) + ';0H' + 'Jump to: ' + '\x1b[0J' + target, end='', flush=True)
            print('\x1b[' + str(cursor_y) + ';' + str(cursor_x) + 'H', end='', flush=True)
            
            k = getch.getch()
            if k == 'w':
                cursor_y -= 1
            elif k == 'a':
                cursor_x -= 1
            elif k == 'd':
                cursor_x += 1
            elif k == 's':
                cursor_y += 1

    def cmd_test(self):
        cols, lines = shutil.get_terminal_size()

        print('\x1b[2J')

        print('\x1b[0;0H' + 'Top-Left')
        print('\x1b[' + str(lines) + ';0H' + 'Bottom-Left', end='')
