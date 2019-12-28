import colorama


def clear_screen():
    return '\x1b[2J'


def clear_line():
    return '\x1b[0J'


def pos(x, y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'


"""Progress bar that is green when near 100 and red when near 0"""
def health_bar(value, maximum):
    ret = colorama.Fore.WHITE + '['

    percent = value * 100 // maximum
    if (percent <= 50):
        ret += colorama.Fore.RED
    elif percent <= 80:
        ret += colorama.Fore.YELLOW
    else:
        ret += colorama.Fore.GREEN
    
    for n in range(5):
        if percent // 20 >= n:
            ret += '■'
        else:
            ret += ' '
    
    ret += colorama.Fore.WHITE + ']'

    return ret


"""Progress bar that is green when near 0 and red when near 100"""
def cargo_bar(value, maximum):
    ret = colorama.Fore.WHITE + '['

    percent = value * 100 // maximum
    if (percent <= 50):
        ret += colorama.Fore.GREEN
    elif percent <= 80:
        ret += colorama.Fore.YELLOW
    else:
        ret += colorama.Fore.RED
    
    for n in range(5):
        if percent // 20 >= n:
            ret += '■'
        else:
            ret += ' '
    
    ret += colorama.Fore.WHITE + ']'

    return ret

