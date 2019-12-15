import random

class TradeItem:
    def __init__(self, name, size, rarity, price):
        self.name = name
        self.size = size
        self.rarity = rarity
        self.price = price

class TradeItemsStack:
    def __init__(self):
        f = open("trade_items.txt", "r")
        lines = f.readlines()
        f.close()

        self.items = []
        for line in lines:
            parts = line.strip().split("\t")
            #if len(parts) < 4:
            #    continue
            name = parts[0]
            #size = parts[1]
            #rarity = parts[2]
            #price = parts[3]
            #self.items.append(TradeItem(name, size, rarity, price))
            self.items.append(TradeItem(name, 1, 100, 1))
