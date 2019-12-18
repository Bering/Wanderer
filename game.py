import shutil
import random
import colorama
from time import sleep

import getch
import ui
from world import World
from player import Player
from star import Star
from planet import Planet
from asteroid import Asteroid
from comet import Comet
from station import Station
from station_service_ui import StationServiceUI

class Game:

    def __init__(self, config):
        self.config = config
        self.world = World(config)
        self.player = Player(config, self.world)
        #self.ais = []
        #for n in range(config.nb_ais):
        #	self.ais.append(AI(self.world))


    def run(self):
        colorama.init()
        nb_stars, nb_planets, nb_asteroids, nb_comets, nb_stations = self.world.get_body_counts()
        print("Wanderer v.alpha0")
        print("World:")
        print(" - " + str(self.config.world_width) + "x" + str(self.config.world_height))
        print(" - " + str(nb_stars) + " stars")
        print(" - " + str(nb_planets) + " planets")
        print(" - " + str(nb_asteroids) + " asteroids")
        print(" - " + str(nb_comets) + " comets")
        print(" - " + str(nb_stations) + " stations")

        print(colorama.Style.RESET_ALL + colorama.Fore.WHITE)
        self.cmd_report()

        k = "?"
        while(k != 'q' and ord(k) != 27):
            print(
                colorama.Fore.LIGHTWHITE_EX + 
                "(?,r,g,s,d,c,t,q) > " + 
                colorama.Fore.WHITE,
                end='', flush=True)
            k = getch.getch()

            if k == 'q' or ord(k) == 27:
                self.cmd_quit()
            elif k == '?':
                self.cmd_help()
            elif k == 'r':
                self.cmd_report()
            elif k == 'g':
                self.cmd_galaxy_map()
            elif k == 's':
                self.cmd_system_map()
            elif k == 'd':
                self.cmd_dropship()
            elif k == 'c':
                self.cmd_jettison_cargo()
            elif k == 't':
                self.cmd_test()
            else:
                print("Unknown or unavailable command: " + k)
        
        print(colorama.Style.RESET_ALL)
        colorama.deinit()


    def cmd_quit(self):
        print("Quit")


    def cmd_help(self):
        print("Help")
        print()
        print("    " + colorama.Fore.LIGHTWHITE_EX + "?" + colorama.Fore.WHITE + "    This help")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "r" + colorama.Fore.WHITE + "    Report       (show ship status and position)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "g" + colorama.Fore.WHITE + "    Galaxy map   (jump from star to star)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "s" + colorama.Fore.WHITE + "    System map   (jump inside a star system)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "d" + colorama.Fore.WHITE + "    Dropship     (visit planets, asteroids, comets and stations)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "c" + colorama.Fore.WHITE + "    Cargo Bay    (View inventory, jettison cargo, etc.)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "t" + colorama.Fore.WHITE + "    Tests        (debug stuff)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "q" + colorama.Fore.WHITE + "    Quit")
        print()


    def cmd_report(self):
        print("Report")

        ship = self.player.ship
        print('\n' + ship.name)
        print('--------------------')
        print('Crew'.ljust(9) + ':' + ui.progress_bar(ship.crew, ship.crew_max).rjust(25))
        print('Fuel'.ljust(9) + ':' + ui.progress_bar(ship.fuel, ship.fuel_max).rjust(25))
        print('Power'.ljust(9) + ':' + ui.progress_bar(ship.power, ship.power_max).rjust(25))
        print('Hull'.ljust(9) + ':' + ui.progress_bar(ship.hull, ship.hull_max).rjust(25))
        print('Shields'.ljust(9) + ':' + ui.progress_bar(ship.shields, ship.shields_max).rjust(25))
        for s in ship.subsystems:
            if s.status == s.green:
                color = colorama.Fore.GREEN
            elif s.status == s.yellow:
                color = colorama.Fore.YELLOW
            else:
                color = colorama.Fore.RED
            print(
                s.name.ljust(9) + 
                ':' + 
                color + 
                s.status.rjust(10) + 
                colorama.Fore.WHITE
            )
        
        print("Position :")
        if self.player.star:
            print(" " + self.player.star.name + " system")
        else:
            print(" Intersideral space")
        
        if self.player.body:
            print(" Orbiting " + self.player.body.name)
        else:
            print(" Nothing near")

        print()


    def cmd_galaxy_map(self):
        
        cols, lines = shutil.get_terminal_size()

        view_left = max(self.player.world_x - (cols // 2), 1)
        view_left = min(view_left, self.config.world_width - cols)
        view_right = view_left + cols - 1

        view_top = max(self.player.world_y - (lines // 2), 1)
        view_top = min(view_top, self.config.world_height - lines)
        view_bottom = view_top + lines - 3 # -1 for math, -1 for header, -1 for footer

        # clear screen
        print(ui.clear_screen() + ui.pos(1,1) + 'Galactic View')

        #print("Window size: " + str(cols) + "x" + str(lines))
        #print("Viewing: (" + str(view_left) + "," + str(view_top) + ") - (" + str(view_right) + "," + str(view_bottom) + ")")

        for s in self.world.stars:
            if s.world_x < view_left or s.world_x > view_right \
            or s.world_y < view_top or s.world_y > view_bottom:
                continue

            col = s.world_x - view_left + 1
            line = s.world_y - view_top + 1
            print(ui.pos(col, line + 1) + s.style + s.color + '*', end='')
        
        col = self.player.world_x - view_left + 1
        line = self.player.world_y - view_top + 1
        print(
            ui.pos(col, line + 1) + 
            colorama.Fore.LIGHTWHITE_EX + 
            '@'
        )

        print(colorama.Style.RESET_ALL + colorama.Fore.WHITE);

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
            
            print(
                ui.pos(1, lines) + 
                colorama.Fore.LIGHTWHITE_EX + 
                '(w,a,s,d,space,enter,esc) ' + 
                colorama.Fore.WHITE + 
                'Jump to: ' + 
                ui.clear_line() + 
                target_text,
                end='', flush=True)
            print(ui.pos(col, line + 1), end='', flush=True)
            
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
            print(ui.pos(1, lines) + '\n' + 'Jump CANCELED\n')
            return
        
        print(ui.pos(1, lines) + '\n' + 'Initiating jump...')
        sleep(1)
        # TODO: random event or something :-)
        print('Jump successful!\n')
        self.player.jump(cursor_x, cursor_y, target)


    def cmd_system_map(self):
        
        if self.player.star == None:
            print('Currently in interstellar space, not in a system.\n')
            return

        cols, lines = shutil.get_terminal_size()

        # System coordinates are centered around the star, hence + star_x and + star_y all over the place
        star_x = cols // 2
        star_y = lines // 2

        view_left = -(cols // 2)
        view_right = view_left + cols - 1

        view_top = -(lines // 2)
        view_bottom = view_top + lines - 3 # -1 for math, -1 for header, -1 for footer

        # clear screen
        print(ui.clear_screen() + ui.pos(1,1) + self.player.star.name + ' System')
        #print("Viewing: (" + str(view_left) + "," + str(view_top) + ") - (" + str(view_right) + "," + str(view_bottom) + ")")

        print(
            ui.pos(star_x, star_y + 1) + 
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
            print(ui.pos(col, line + 1) + b.color + b.symbol, end='')
        
        col = star_x + self.player.system_x
        line = star_y + self.player.system_y
        print(
            ui.pos(col, line + 1) + 
            colorama.Fore.LIGHTWHITE_EX + 
            '@'
        )

        print(colorama.Style.RESET_ALL + colorama.Fore.WHITE);

        k = '?'
        while(ord(k) != 13 and k != ' ' and ord(k) != 27):

            cursor_x = col - star_x
            cursor_y = line - star_y

            target = self.player.star.get_body_at(cursor_x, cursor_y)
            if target == None:
                target_text = '(' + str(cursor_x) + ',' + str(cursor_y) + ')'
            else:
                target_text = target.name
            
            print(
                ui.pos(1, lines) + 
                colorama.Fore.LIGHTWHITE_EX + 
                '(w,a,s,d,space,enter,esc) ' + 
                colorama.Fore.WHITE + 
                'Jump to: ' + 
                ui.clear_line() + 
                target_text,
                end='', flush=True)
            print(ui.pos(col, line + 1), end='', flush=True)
            
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
            print(ui.pos(1, lines) + '\n' + 'Jump CANCELED\n')
            return
        
        print(ui.pos(1, lines) + '\n' + 'Initiating jump...')
        sleep(1)
        # TODO: random event or something :-)
        print('Jump successful!\n')
        self.player.jump_in_system(cursor_x, cursor_y, target)


    def cmd_dropship(self):
        print("Launch a Dropship\n")

        if not self.player.body:
            print("We're in the middle of nowhere...\n")
            return

        if isinstance(self.player.body, Star):
            print("I don't think you want to go out in a dropship while orbiting a star :-)")

        elif isinstance(self.player.body, Planet):
            if self.player.body.type == "Gas Giant":
                print("Cannot do refueling operations yet :( In a future version maybe...")
            else:
                print("Cannot drop to planet surface yet :( In a future version maybe...")
        
        elif isinstance(self.player.body, Asteroid):
            print("Cannot investigate asteroids yet :( In a future version maybe...")
        
        elif isinstance(self.player.body, Comet):
            print("Cannot investigate comets yet :( In a future version maybe...")
        
        elif isinstance(self.player.body, Station):
            station = self.player.body
            print("Welcome to " + station.name + "!")
            print("What can I do for you?")

            k = '?'
            cursor = 0
            cols, lines = shutil.get_terminal_size()
            while k != ' ' and ord(k) != 13 and k != 'q' and ord(k) != 27:
                for index, service in enumerate(station.services):
                    if cursor == index:
                        print(
                            " -" + 
                            colorama.Fore.LIGHTWHITE_EX + 
                            "[" + 
                            colorama.Fore.WHITE + 
                            service.name + 
                            colorama.Fore.LIGHTWHITE_EX + 
                            "]" + 
                            colorama.Fore.WHITE
                        )
                    else:
                        print(" - " + service.name + " ")

                print(
                    "\n" + \
                    colorama.Fore.LIGHTWHITE_EX + \
                    "(w,s,space,enter,q,esc) " + \
                    colorama.Fore.WHITE,
                    end='',
                    flush=True
                )

                k = getch.getch()
                if k == 'w' and cursor > 0:
                    cursor -= 1
                elif k == 's' and cursor < len(station.services) - 1:
                    cursor += 1

                print(ui.pos(1, lines - 2 - len(station.services)))

        print(ui.pos(25,lines), end='')
        if k == 'q' or ord(k) == 27:
            print("Bye\n")
            return

        print(station.services[cursor].name)
        ssui = StationServiceUI()
        ssui.render(station, cursor, self.player)


    def cmd_jettison_cargo(self):
        print("Visit Cargo Bay\n")

        if len(self.player.ship.inventory.items) == 0:
            print("There is nothing left in here!\n")
            return

        print("Select cargo to jettison.")

        k = '?'
        cursor = 0
        indexes_to_jettison = []
        cols, lines = shutil.get_terminal_size()

        while ord(k) != 13 and k != 'q' and ord(k) != 27:
            for index,name in enumerate(self.player.ship.inventory.items):

                if index in indexes_to_jettison:
                    item_color = colorama.Fore.LIGHTYELLOW_EX
                else:
                    item_color = colorama.Fore.WHITE

                if cursor == index:
                    line = " -" + \
                            colorama.Fore.LIGHTWHITE_EX + "[" + \
                            item_color + name + \
                            colorama.Fore.LIGHTWHITE_EX + "]" + \
                            colorama.Fore.WHITE
                    print(line)
                else:
                    print(" - " + item_color + name + colorama.Fore.WHITE + " ")
                
            print(
                "\n" + \
                colorama.Fore.LIGHTWHITE_EX + \
                "(w,s,space,enter,q,esc) " + \
                colorama.Fore.WHITE,
                end='',
                flush=True
            )

            k = getch.getch()
            if k == 'w' and cursor > 0:
                cursor -= 1
            elif k == 's' and cursor < len(self.player.ship.inventory.items) - 1:
                cursor += 1
            elif k == ' ':
                if cursor in indexes_to_jettison:
                    indexes_to_jettison.remove(cursor)
                else:
                    indexes_to_jettison.append(cursor)
            
            print(ui.pos(1, lines - 2 - len(self.player.ship.inventory.items)))

        print(ui.pos(25, lines), end='')

        if k == 'q' or ord(k) == 27:
            print("Nevermind...\n")
            return
        
        names_to_jettison = []
        for index,name in enumerate(self.player.ship.inventory.items):
            if index in indexes_to_jettison:
                names_to_jettison.append(name)
        
        for name in names_to_jettison:
            i = self.player.ship.inventory.items[name]
            self.player.ship.inventory.remove(i.name, i.quantity)

        print("Done!\n")



    def cmd_test(self):
        cols, lines = shutil.get_terminal_size()

        print(ui.clear_screen())

        print(ui.pos(1,1) + 'Top-Left')

        print(ui.pos(1, 3), end='')
        for n in range(0,101, 5):
            print(ui.progress_bar(n, 100).rjust(25))
        
        print(
            ui.pos(1, lines) + 
            colorama.Fore.LIGHTWHITE_EX + 
            'Press any key... ' + 
            colorama.Fore.WHITE,
            end='', flush=True)
        k = getch.getch_that_can_do_arrow_keys()
        print(str(ord(k)) + "\n")

