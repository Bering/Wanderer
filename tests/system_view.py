import colorama
import shutil
import math

system_width = 80
system_height = 24
max_distance = min(system_width, system_height) // 2

def clear_screen():
    return '\x1b[2J'
def clear_line():
    return '\x1b[0J'
def pos(x, y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'

cols, lines = shutil.get_terminal_size()

# System coordinates are centered around the star, hence + star_x and + star_y all over the place
star_x = cols // 2
star_y = lines // 2

view_left = -(cols // 2)
view_right = (cols // 2)

view_top = -(lines // 2) + 2        # +1 for // 2 flooring the value instead of rounding, +1 for header
view_bottom = (lines // 2) - 1      # -1 for footer

print(clear_screen() + pos(1,1), end='')
print(str(system_width) + "x" + str(system_height))
print("max distance = " + str(max_distance))
print("Viewing: (" + str(view_left) + "," + str(view_top) + ") - (" + str(view_right) + "," + str(view_bottom) + ")")

bodies = []

color = 30
for distance in range(3, max_distance+1, 3):
    color += 1
    if color == 38:
        color = 91
    elif color == 97:
        color = 31
    
    for angle in range(0, 360):
        x = round(distance * math.cos(math.radians(angle)))
        y = round(distance * math.sin(math.radians(angle)))
        
        if x < view_left or x > view_right or y < view_top or y > view_bottom:
            continue

        col = star_x + x
        line = star_y + y
        print(pos(col, line) + "\x1b[" + str(color) + 'mO', end='')

    print(pos(1,lines), end='')
# k = '?'
# while(ord(k) != 13 and k != ' ' and ord(k) != 27):

#     cursor_x = col - star_x
#     cursor_y = line - star_y

#     target = self.player.star.get_body_at(cursor_x, cursor_y)
#     if target == None:
#         target_text = '(' + str(cursor_x) + ',' + str(cursor_y) + ')'
#     else:
#         target_text = target.name

#     for f in self.player.star.fleets:
#         if f.body_x == cursor_x and f.body_y == cursor_y:
#             target_text += ' (' + \
#                         f.race.color + \
#                         f.name + \
#                         colorama.Fore.WHITE + \
#                         ')'

#     print(
#         pos(1, lines) + 
#         colorama.Fore.LIGHTWHITE_EX + 
#         '(w,a,s,d,space,enter,esc) ' + 
#         colorama.Fore.WHITE + 
#         'Jump to: ' + 
#         clear_line() + 
#         target_text,
#         end='', flush=True)
#     print(pos(col, line + 1), end='', flush=True)
    
#     k = getch.getch()
#     if k == 'w':
#         if line > 1:
#             line -= 1
#     elif k == 'a':
#         if col > 1:
#             col -= 1
#     elif k == 'd':
#         if col < cols:
#             col += 1
#     elif k == 's':
#         if line < lines - 2:
#             line += 1
