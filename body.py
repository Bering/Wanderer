import math

# NOTE: bodies have coordinates around the star (0,0 is the star)

class Body:

    def __init__(self, star, name, angle, distance, color, symbol):
        self.star = star
        self.name = name
        self.body_x = round(distance * math.cos(math.radians(angle)))
        self.body_y = round(distance * math.sin(math.radians(angle)))
        self.color = color
        self.symbol = symbol
