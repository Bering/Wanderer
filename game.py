import shutil
import random
import colorama
from time import sleep

import getch
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
            elif k == 'g':
                self.cmd_galaxy_map()
            elif k == 's':
                self.cmd_system_map()
            elif k == 't':
                self.cmd_test()
            else:
                print("Unknown or unavailable command: " + k)
        
        print(colorama.Style.RESET_ALL)
        colorama.deinit()


    def cmd_quit(self):
        print("Quit")


    def cmd_galaxy_map(self):
        
        cols, lines = shutil.get_terminal_size()

        view_left = max(self.player.world_x - (cols // 2), 1)
        view_left = min(view_left, self.config.world_width - cols)
        view_right = view_left + cols - 1

        view_top = max(self.player.world_y - (lines // 2), 1)
        view_top = min(view_top, self.config.world_height - lines)
        view_bottom = view_top + lines - 3 # -1 for math, -1 for header, -1 for footer

        # clear screen
        print('\x1b[2J')
        print('\x1b[0;0HGalactic View')

        #print("Window size: " + str(cols) + "x" + str(lines))
        #print("Viewing: (" + str(view_left) + "," + str(view_top) + ") - (" + str(view_right) + "," + str(view_bottom) + ")")

        for s in self.world.stars:
            if s.world_x < view_left or s.world_x > view_right \
            or s.world_y < view_top or s.world_y > view_bottom:
                continue

            col = s.world_x - view_left + 1
            line = s.world_y - view_top + 1
            print('\x1b[' + str(line + 1) + ';' + str(col) + 'H' + s.style + s.color + '*', end='')
        
        col = self.player.world_x - view_left + 1
        line = self.player.world_y - view_top + 1
        print(
            '\x1b[' + str(line + 1) + ';' + str(col) + 'H' + 
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
            print('\x1b[' + str(line + 1) + ';' + str(col) + 'H', end='', flush=True)
            
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
                if line < lines - 2:
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
        self.player.system_x = 0
        self.player.system_y = 0
        self.player.body = self.player.star


    def cmd_system_map(self):
        
        if self.player.star == None:
            print('Currently in interstellar space, not in a system.')
            return

        cols, lines = shutil.get_terminal_size()

        view_left = max(self.player.system_x - (cols // 2), 1)
        view_left = min(view_left, self.config.system_width - cols)
        view_right = view_left + cols - 1

        view_top = max(self.player.system_y - (lines // 2), 1)
        view_top = min(view_top, self.config.system_height - lines)
        view_bottom = view_top + lines - 3 # -1 for math, -1 for header, -1 for footer

        # clear screen
        print('\x1b[2J')
        print('\x1b[0;0H' + self.player.star.name + ' System')

        # System coordinates are centered around the star, hence + star_x and + star_y all over the place
        star_x = cols // 2
        star_y = lines // 2

        print(
            '\x1b[' + str(star_y + 1) + ';' + str(star_x) + 'H' + 
            self.player.star.color + 
            '*',
            end=''
        )

        for b in self.player.star.bodies:
            if b.body_x < view_left or b.body_x > view_right \
            or b.body_y < view_top or b.body_y > view_bottom:
                continue

            col = star_x + b.body_x
            line = star_y + b.body_y
            print('\x1b[' + str(line + 1) + ';' + str(col) + 'H' + b.color + b.symbol, end='')
        
        col = star_x + self.player.system_x
        line = star_y + self.player.system_y
        print(
            '\x1b[' + str(line + 1) + ';' + str(col) + 'H' + 
            colorama.Style.BRIGHT + 
            colorama.Fore.WHITE + 
            '@'
        )

        print(colorama.Style.RESET_ALL);

        k = '?'
        while(ord(k) != 13 and k != ' ' and ord(k) != 27):

            cursor_x = col - star_x
            cursor_y = line - star_y

            target = self.player.star.get_body_at(cursor_x, cursor_y)
            if target == None:
                target_text = '(' + str(cursor_x) + ',' + str(cursor_y) + ')'
            else:
                target_text = target.name
            
            print('\x1b[' + str(lines) + ';0H' + 'Jump to: ' + '\x1b[0J' + target_text, end='', flush=True)
            print('\x1b[' + str(line + 1) + ';' + str(col) + 'H', end='', flush=True)
            
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
                if line < lines - 2:
                    line += 1
        
        if ord(k) == 27 or (cursor_x == self.player.system_x and cursor_y == self.player.system_y):
            print('\x1b[' + str(lines) + ';0H' + '\n' + 'Jump CANCELED')
            return
        
        print('\x1b[' + str(lines) + ';0H' + '\n' + 'Initiating jump...')
        sleep(1)
        # TODO: random event or something :-)
        print('Jump successful!')

        self.player.system_x = cursor_x
        self.player.system_y = cursor_y
        self.player.body = target
    

    def cmd_test(self):
        cols, lines = shutil.get_terminal_size()

        print('\x1b[2J')

        print('\x1b[0;0H' + 'Top-Left')
        print('\x1b[' + str(lines) + ';0H' + 'Bottom-Left', end='')
