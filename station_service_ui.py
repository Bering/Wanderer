import getch
import shutil
import colorama
from time import sleep

import ui
import station_service

class StationServiceUI:
    def render(self, station, service_index, game):
        service = station.services[service_index]

        if isinstance(service, station_service.News):
            print()
            print("Local News:")
            for n in game.world.news[station.star.name]:
                print("%03d: %s" % (n.turn, n.text))
            print("000: (Rumor) An enemy fleet is en-route to attack this system")
            print()

            print("Global News:")
            for n in game.world.news["global"]:
                print("%03d: %s" % (n.turn, n.text))
            print("000: Update on ongoing research on <artifact> on <planet or station> in the <system> system")
            print("000: A fleet is being dispatched to Earth (or Plan B planet) from <planet or station> in <system>")
            print()


        elif isinstance(service, station_service.Repair):
            print()
            print(
                "It will take " + 
                str(game.player.ship.hull_max - game.player.ship.hull) + 
                " days. (y/n) ",
                end='',
                flush=True)
            
            k = '?'
            while k != 'y' and k != 'n':
                k = getch.getch()
            
            if k == 'y':
                print("Repairing...")
                # TODO: make time pass by
                sleep(1)
                game.player.ship.hull = game.player.ship.hull_max
                print("It was a pleasure doing business with you!\n")
            else:
                print("Ok bye\n")
        

        elif isinstance(service, station_service.Refuel):
            print()
            # TODO: make time pass by
            sleep(1)
            game.player.ship.fuel = game.player.ship.fuel_max
            print("OK we're full!\n")


        elif isinstance(service, station_service.Plunder):
            print()

            if len(service.inventory.items) == 0:
                print("Nothing to plunder here!\n")
                return

            print("What do we plunder?")

            k = '?'
            cursor = 0
            indexes_to_plunder = []
            cols, lines = shutil.get_terminal_size()

            while ord(k) != 13 and k != 'q' and ord(k) != 27:
                for index,name in enumerate(service.inventory.items):

                    if index in indexes_to_plunder:
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
                elif k == 's' and cursor < len(service.inventory.items) - 1:
                    cursor += 1
                elif k == ' ':
                    if cursor in indexes_to_plunder:
                        indexes_to_plunder.remove(cursor)
                    else:
                        indexes_to_plunder.append(cursor)
                
                print(ui.pos(1, lines - 2 - len(service.inventory.items)))

            print(ui.pos(25, lines), end='')

            if k == 'q' or ord(k) == 27:
                print("Ah, too bad :(\n")
                return
            
            names_to_plunder = []
            for index,name in enumerate(service.inventory.items):
                if index in indexes_to_plunder:
                    names_to_plunder.append(name)
            
            for name in names_to_plunder:
                i = service.inventory.items[name]
                game.player.ship.inventory.add(i.name, i.unit_size, i.quantity)
                service.inventory.remove(i.name, i.quantity)

            print("Yarr! The Merry Band of Pirates strikes again :-)\n")


        elif isinstance(service, station_service.Research):
            print()
            print("Skippy stole everything that could be used to help Earth!\n")

