import colorama
import shutil
import math

class TestBody:
    def __init__(self, name, angle, distance):
        self.body_x = round(distance * math.cos(math.radians(angle)))
        self.body_y = round(distance * math.sin(math.radians(angle)))


bodies = []
distance = 10
for angle in range(0, 359):
    bodies.append(TestBody(angle, angle, distance))

cols, lines = shutil.get_terminal_size()
star_x = cols // 2
star_y = lines // 2

# clear screen
print('\x1b[2J')

for b in bodies:
    col = star_x + b.body_x
    line = star_y + b.body_y

    if b.body_y < 0:
        color = colorama.Fore.BLUE
    else:
        color = colorama.Fore.WHITE

    print('\x1b[' + str(line + 1) + ';' + str(col) + 'H' + color + '.', end='')

print('\x1b[' + str(lines) + ';0H')
