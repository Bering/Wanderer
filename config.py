# This is here because it does IO and I want to only have one instance of it. I'm a python n00b maybe there's a better way
from trade_items_stack import TradeItemsStack
trade_items_stack = TradeItemsStack()

# World size (where the stars are)
world_width = 320
world_height = 96

# Star System size (where the planets are)
system_width = 80
system_height = 24

# At a distance x around a star, what are the chances one of these shows up (if the previous one didn't)
probability_planet = 50
probability_asteroids = 20 # this is the probability for a belt to show up, not just one
probability_station = 100 # 100 instead of 20 for development of the interfaces
probability_comet = 20

max_planet_per_system = 24 # If you want more you need to provide more names in the Planet class
max_asteroids_per_belt = 40

# What are the chances a station has these services
# TODO: All 100% for debugging
probability_repair = 100
probability_rearm = 100
probability_refuel = 100
probability_trade = 100
probability_research = 100
