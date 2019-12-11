
class Body:

    def __init__(self, star, name, x, y, color, symbol):
        self.star = star
        self.name = name
        self.body_x = x # bodies have coordinates around the star (0,0 is the star)
        self.body_y = y
        self.color = color
        self.symbol = symbol
