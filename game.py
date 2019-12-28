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
from inventory import ItemNotInStockError

class Game:

    def __init__(self, config):
        self.config = config
        self.player = Player(config)
        self.world = World(config, self.player)
        self.turn = 1
        
        # Store here like that for now but I need a better way
        self.intel_earth_status = "Safe"
        self.intel_beta_site_status = "Safe"


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
        print(" - " + str(len(self.world.fleets)) + " fleets")

        print(colorama.Style.RESET_ALL + colorama.Fore .WHITE)
        self.cmd_help()

        k = "?"
        while(k != 'q' and ord(k) != 27):

            print(
                colorama.Fore.LIGHTWHITE_EX + 
                "(?,r,g,s,d,c,t,q) > " + 
                colorama.Fore.WHITE,
                end='', flush=True)
            k = getch.getch()

            if k == 'q' or ord(k) == 27:
                next_turn = self.cmd_quit()
            elif k == '?':
                next_turn = self.cmd_help()
            elif k == 'w':
                next_turn = self.cmd_wait()
            elif k == 'r':
                next_turn = self.cmd_report()
            elif k == 'g':
                next_turn = self.cmd_galaxy_map()
            elif k == 's':
                next_turn = self.cmd_system_map()
            elif k == 'd':
                next_turn = self.cmd_dropship()
            elif k == 'c':
                next_turn = self.cmd_jettison_cargo()
            elif k == 't':
                next_turn = self.cmd_test()
            else:
                print("Unknown or unavailable command: " + k)
                next_turn = False

            if next_turn:
                self.player.drink()
                self.player.eat()
                self.world.tick(self.player)

        print(colorama.Style.RESET_ALL)
        colorama.deinit()


    def cmd_quit(self):
        print("Quit")
        return False


    def cmd_help(self):
        print("Help")
        print()
        print("    " + colorama.Fore.LIGHTWHITE_EX + "?" + colorama.Fore.WHITE + "    This help")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "w" + colorama.Fore.WHITE + "    Wait         (do nothing for 1 turn)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "r" + colorama.Fore.WHITE + "    Report       (show ship status and position)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "g" + colorama.Fore.WHITE + "    Galaxy map   (jump from star to star)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "s" + colorama.Fore.WHITE + "    System map   (jump inside a star system)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "d" + colorama.Fore.WHITE + "    Dropship     (visit planets, asteroids, comets and stations)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "c" + colorama.Fore.WHITE + "    Cargo Bay    (View inventory, jettison cargo, etc.)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "t" + colorama.Fore.WHITE + "    Tests        (debug stuff)")
        print("    " + colorama.Fore.LIGHTWHITE_EX + "q" + colorama.Fore.WHITE + "    Quit")
        print()
        return False


    def cmd_wait(self):
        print("Wait\n")
        return True

    def cmd_report(self):
        print("Report")
        print()
        
        print('--------------------')
        print('Turn'.ljust(9) + ':' + str(self.turn).rjust(10))
        print('Earth'.ljust(9) + ':' + self.intel_earth_status.rjust(10))
        print('Beta Site'.ljust(9) + ':' + self.intel_beta_site_status.rjust(10))
        print()

        ship = self.player.ship
        print(ship.name)
        print('--------------------')
        print('Crew'.ljust(9) + ':' + str(ship.crew).rjust(3) + ui.health_bar(ship.crew, ship.crew_max))
        print('Fuel'.ljust(9) + ':' + str(ship.fuel).rjust(3) + ui.health_bar(ship.fuel, ship.fuel_max))
        print('Inventory:' + \
            str(round(ship.inventory.size / 1000)).rjust(2) + "k" + \
            ui.cargo_bar(ship.inventory.size, ship.inventory.size_max))
        print('Hull'.ljust(9) + ':' + str(ship.hull).rjust(3) + ui.health_bar(ship.hull, ship.hull_max))
        print('Power'.ljust(9) + ':' + str(ship.power).rjust(3) + ui.cargo_bar(ship.power, ship.power_max))
        print('Shields'.ljust(9) + ':' + str(ship.shields).rjust(3) + ui.health_bar(ship.shields, ship.shields_max))
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

        print("Objective:")
        print(" Not set")

        print()
        return False


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
            if s.owner:
                color = s.owner.color
            else:
                color = colorama.Fore.WHITE
            print(ui.pos(col, line + 1) + color + '*', end='')
        
        col = self.player.world_x - view_left + 1
        line = self.player.world_y - view_top + 1
        print(
            ui.pos(col, line + 1) + 
            colorama.Fore.LIGHTWHITE_EX + 
            '@',
            end = ''
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
                    if s.owner:
                        target_text += " (" \
                                     + s.owner.color \
                                     + s.owner.name \
                                     + colorama.Fore.WHITE \
                                     + ")"
                    target = s
                    break
            
            fuel_cost = self.player.fuel_cost(cursor_x, cursor_y)
            target_text += " (fuel cost: "
            if fuel_cost > self.player.ship.fuel:
                target_text += colorama.Fore.LIGHTRED_EX
            target_text += str(fuel_cost) + \
                            colorama.Fore.WHITE + \
                            ")"
            
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
            return False
        
        print(ui.pos(1, lines))
        if fuel_cost <= self.player.ship.fuel:
            print('Initiating jump...')
            self.player.jump(cursor_x, cursor_y, target)
            sleep(1)
            # TODO: random event or something :-)
            print('Jump successful!\n')
            return True
        else:
            print('Cannot jump: Not enough fuel!\n')
            return False


    def cmd_system_map(self):
        
        if self.player.star == None:
            print('Currently in interstellar space, not in a system.\n')
            return False

        cols, lines = shutil.get_terminal_size()

        # System coordinates are centered around the star, hence + star_x and + star_y all over the place
        star_x = cols // 2
        star_y = lines // 2

        view_left = -(cols // 2)
        view_right = (cols // 2)

        view_top = -(lines // 2) + 2        # +1 for // 2 flooring the value instead of rounding, +1 for header
        view_bottom = (lines // 2) - 1      # -1 for footer

        # clear screen
        print(ui.clear_screen() + ui.pos(1,1) + self.player.star.name + ' System')
        #print("Viewing: (" + str(view_left) + "," + str(view_top) + ") - (" + str(view_right) + "," + str(view_bottom) + ")")

        if self.player.star.owner:
            color = self.player.star.owner.color
        else:
            color = colorama.Fore.WHITE
        print(
            ui.pos(star_x, star_y) + 
            color + 
            '*',
            end=''
        )

        for b in self.player.star.bodies:
            if b.body_x < view_left or b.body_x > view_right \
            or b.body_y < view_top or b.body_y > view_bottom:
                continue

            col = star_x + b.body_x
            line = star_y + b.body_y
            print(ui.pos(col, line) + b.color + b.symbol, end='')

        for f in self.player.star.fleets:
            col = star_x + f.body_x
            line = star_y + f.body_y
            print(ui.pos(col, line) + f.race.color + f.race.letter, end='')

        col = star_x + self.player.system_x
        line = star_y + self.player.system_y
        print(
            ui.pos(col, line) + 
            colorama.Fore.LIGHTWHITE_EX + 
            '@',
            end = ''
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

            for f in self.player.star.fleets:
                if f.body_x == cursor_x and f.body_y == cursor_y:
                    target_text += ' (' + \
                                f.race.color + \
                                f.name + \
                                colorama.Fore.WHITE + \
                                ')'

            print(
                ui.pos(1, lines) + 
                colorama.Fore.LIGHTWHITE_EX + 
                '(w,a,s,d,space,enter,esc) ' + 
                colorama.Fore.WHITE + 
                'Jump to: ' + 
                ui.clear_line() + 
                target_text,
                end='', flush=True)
            print(ui.pos(col, line), end='', flush=True)
            
            k = getch.getch()
            if k == 'w':
                if line > 2:
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
        
        if ord(k) == 27 or (cursor_x == self.player.system_x and cursor_y == self.player.system_y):
            print(ui.pos(1, lines) + '\n' + 'Jump CANCELED\n')
            return False
        
        print(ui.pos(1, lines) + '\n' + 'Initiating jump...')
        sleep(1)
        # TODO: random event or something :-)
        print('Jump successful!\n')
        self.player.jump_in_system(cursor_x, cursor_y, target)
        return True


    def cmd_dropship(self):
        print("Launch a Dropship\n")

        cols, lines = shutil.get_terminal_size()

        if not self.player.body:
            print("We're in the middle of nowhere...\n")
            return False

        if isinstance(self.player.body, Star):
            print("I don't think you want to go out in a dropship while orbiting a star :-)\n")

        elif isinstance(self.player.body, Planet):
            if self.player.body.type == "Gas Giant":
                print("Cannot do refueling operations yet :( In a future version maybe...\n")
            else:
                print("Cannot drop to planet surface yet :( In a future version maybe...\n")
        
        elif isinstance(self.player.body, Asteroid):
            print("Cannot investigate asteroids yet :( In a future version maybe...\n")
        
        elif isinstance(self.player.body, Comet):
            print("Cannot investigate comets yet :( In a future version maybe...\n")
        
        elif isinstance(self.player.body, Station):
            station = self.player.body
            print("Welcome to " + station.name + "!")
            print("What can I do for you?")

            k = '?'
            cursor = 0
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

            next_turn = False
            if k == 'q' or ord(k) == 27:
                print("Bye\n")
                return next_turn

            print(station.services[cursor].name)
            ssui = StationServiceUI()
            next_turn = ssui.render(station, cursor, self)


    def cmd_jettison_cargo(self):
        print("Visit Cargo Bay\n")

        if len(self.player.ship.inventory.items) == 0:
            print("There is nothing in here! We need to plunder a station or base...\n")
            return False

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
            print("\n")
            return False
        
        names_to_jettison = []
        for index,name in enumerate(self.player.ship.inventory.items):
            if index in indexes_to_jettison:
                names_to_jettison.append(name)
        
        for name in names_to_jettison:
            i = self.player.ship.inventory.items[name]
            self.player.ship.inventory.remove(i.name, i.quantity)

        print("Done!\n")
        return True


    def cmd_test(self):
        cols, lines = shutil.get_terminal_size()

        print(ui.clear_screen())

        print(ui.pos(1,1) + 'Top-Left')

        print(ui.pos(1, 3), end='')
        for n in range(0,101, 5):
            print(str(n).rjust(3) + " " + ui.health_bar(n, 100))
        
        print(
            ui.pos(1, lines) + 
            colorama.Fore.LIGHTWHITE_EX + 
            'Press any key... ' + 
            colorama.Fore.WHITE,
            end='', flush=True)
        k = getch.getch_that_can_do_arrow_keys()
        print(str(ord(k)) + "\n")
        return False

