
class Race:
    def __init__(self, name, parent, letter, color):
        self.name = name
        self.parent = parent
        self.letter = letter
        self.color = color
        self.clients = []

        if parent:
            parent.clients.append(self)
