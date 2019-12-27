import colorama

class News:
    def __init__(self, turn, fleet):
        self.turn = turn
        self.fleet = fleet
        self.star = self.fleet.home.star

        if self.fleet.destination.owner:
            destinationColor = self.fleet.destination.owner.color
        else:
            destinationColor = colorama.Fore.WHITE
        
        self.text = "New " + \
                    self.fleet.race.color + \
                    self.fleet.name + \
                    colorama.Fore.WHITE + \
                    " from " + \
                    self.fleet.home.star.owner.color + \
                    self.fleet.home.star.name + \
                    colorama.Fore.WHITE + \
                    " going to " + \
                    destinationColor + \
                    self.fleet.destination.name

