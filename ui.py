import colorama


def clear_screen():
    return '\x1b[2J'


def clear_line():
    return '\x1b[0J'


def pos(x, y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'


def progress_bar(value, maximum):
    ret = colorama.Fore.WHITE + str(value) + ' ['

    percent = value * 100 // maximum
    if (percent <= 20):
        ret += colorama.Fore.RED + '■  '
    elif percent <= 50:
        ret += colorama.Fore.YELLOW + '■■ '
    else:
        ret += colorama.Fore.GREEN + '■■■'
    
    ret += colorama.Fore.WHITE + ']'

    return ret

