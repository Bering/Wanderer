import shutil
import getch
import colorama
from time import sleep

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
        
        view_left = max(self.player.world_x - (cols // 2), 1)
        view_left = min(view_left, self.config.world_width - cols)
        view_right = view_left + cols - 1

        view_top = max(self.player.world_y - (lines // 2), 1)
        view_top = min(view_top, self.config.world_height - lines)
        view_bottom = view_top + lines - 1

        # clear screen
        print('\x1b[2J')

        #print("Window size: " + str(cols) + "x" + str(lines))
        #print("Viewing: (" + str(view_left) + "," + str(view_top) + ") - (" + str(view_right) + "," + str(view_bottom) + ")")

        for s in self.world.stars:
            if s.world_x < view_left or s.world_x > view_right \
            or s.world_y < view_top or s.world_y > view_bottom:
                continue

            col = s.world_x - view_left + 1
            line = s.world_y - view_top + 1
            print('\x1b[' + str(line) + ';' + str(col) + 'H' + s.style + s.color + '*', end='')
        
        col = self.player.world_x - view_left + 1
        line = self.player.world_y - view_top + 1
        print(
            '\x1b[' + str(line) + ';' + str(col) + 'H' + 
            colorama.Style.BRIGHT + 
            colorama.Fore.WHITE + 
            '@'
        )

        print(colorama.Style.RESET_ALL);

        k = '?'
        while(ord(k) != 13 and k != ' ' and ord(k) != 27):

            cursor_x = col + view_left - 1
            cursor_y = line + view_top - 1
            target_text = '(' + str(cursor_x) + ',' + str(cursor_y) + ')'
            target = None
            for s in self.world.stars:
                if s.world_x == cursor_x and s.world_y == cursor_y:
                    target_text = s.name
                    target = s
                    break
            
            print('\x1b[' + str(lines) + ';0H' + 'Jump to: ' + '\x1b[0J' + target_text, end='', flush=True)
            print('\x1b[' + str(line) + ';' + str(col) + 'H', end='', flush=True)
            
            k = getch.getch()
            if k == 'w':
                if line > 1:
                    line -= 1
            elif k == 'a':
                if col > 1:
                    col -= 1
            elif k == 'd':
                if col < cols:
                    col += 1
            elif k == 's':
                if line < lines - 1:
                    line += 1
        
        if ord(k) == 27 or (cursor_x == self.player.world_x and cursor_y == self.player.world_y):
            print('\x1b[' + str(lines) + ';0H' + '\n' + 'Jump CANCELED')
            return
        
        print('\x1b[' + str(lines) + ';0H' + '\n' + 'Initiating jump...')
        sleep(1)
        # TODO: random event or something :-)
        print('Jump successful!')

        self.player.world_x = cursor_x
        self.player.world_y = cursor_y
        self.player.star = target

    def cmd_test(self):
        cols, lines = shutil.get_terminal_size()

        print('\x1b[2J')

        print('\x1b[0;0H' + 'Top-Left')
        print('\x1b[' + str(lines) + ';0H' + 'Bottom-Left', end='')
