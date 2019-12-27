import colorama

from fleet import Orders

class News:
    def __init__(self, turn, text):
        self.turn = turn
        self.text = text


class LocalNews_NewFleet(News):
    def __init__(self, turn, fleet):
        if fleet.destination.owner:
            destinationColor = fleet.destination.owner.color
        else:
            destinationColor = colorama.Fore.WHITE
        
        text = "New " + \
               fleet.race.color + \
               fleet.name + \
               colorama.Fore.WHITE + \
               " from " + \
               fleet.home.star.owner.color + \
               fleet.home.star.name + \
               colorama.Fore.WHITE

        if fleet.orders != Orders.DEFEND:
            text += " going to " + \
                    destinationColor + \
                    fleet.destination.name + \
                    colorama.Fore.WHITE

        super().__init__(turn, text)

