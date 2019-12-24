from enum import Enum
import random

from body import Body
from sol import Sol

class Orders(Enum):
    RANDOM = 0
    RETREAT = 1
    DEFEND = 2
    PATROL = 3
    ATTACK = 4
    EXPLORE = 5
    INVESTIGATE = 6


class Fleet(Body):
    def __init__(self, world, home, orders):
        self.world = world
        self.race = home.star.owner
        self.home = home

        self.orders = orders
        while self.orders == Orders.RANDOM:
            self.orders = random.choice(list(Orders))

        self.star = home.star
        self.destination = self.set_destination()
        

    def set_destination(self):
        if self.orders == Orders.RETREAT:
            return self.find_nearest_allied_system()
        elif self.orders == Orders.DEFEND:
            return self.star
        elif self.orders == Orders.PATROL:
            return self.find_nearest_system_to_patrol_to()
        elif self.orders == Orders.ATTACK:
            return self.find_nearest_enemy_system()
        elif self.orders == Orders.EXPLORE:
            return self.find_nearest_system_to_explore()
        elif self.orders == Orders.INVESTIGATE:
            return self.find_sol()   
        else:
            raise IndexError()


    def find_nearest_allied_system(self):
        nearest_star = None
        nearest_distance = 9999999
        for s in self.world.stars:
            if self.world.areAllied(self.star.owner, s.owner):
                distanceSqr = (self.star.world_x - s.world_x) * (self.star.world_x - s.world_x)
                distanceSqr += (self.star.world_y - s.world_y) * (self.star.world_y - s.world_y)
                if distanceSqr < nearest_distance:
                        nearest_distance = distanceSqr
                        nearest_star = s

        return nearest_star


    def find_nearest_enemy_system(self):
        nearest_star = None
        nearest_distance = 9999999
        for s in self.world.stars:
            if self.world.areEnemies(self.star.owner, s.owner):
                distanceSqr = (self.star.world_x - s.world_x) * (self.star.world_x - s.world_x)
                distanceSqr += (self.star.world_y - s.world_y) * (self.star.world_y - s.world_y)
                if distanceSqr < nearest_distance:
                        nearest_distance = distanceSqr
                        nearest_star = s

        return nearest_star


    def find_nearest_system_to_patrol_to(self):
        nearest_star = None
        nearest_distance = 9999999
        for s in self.world.stars:
            if s != self.star and s != self.home.star:
                distanceSqr = (self.star.world_x - s.world_x) * (self.star.world_x - s.world_x)
                distanceSqr += (self.star.world_y - s.world_y) * (self.star.world_y - s.world_y)
                if distanceSqr < nearest_distance:
                    nearest_distance = distanceSqr
                    nearest_star = s

        return nearest_star


    def find_nearest_system_to_explore(self):
        nearest_star = None
        nearest_distance = 9999999
        for s in self.world.stars:
            if not s.owner:
                distanceSqr = (self.star.world_x - s.world_x) * (self.star.world_x - s.world_x)
                distanceSqr += (self.star.world_y - s.world_y) * (self.star.world_y - s.world_y)
                if distanceSqr < nearest_distance:
                    nearest_distance = distanceSqr
                    nearest_star = s

        return nearest_star


    def find_sol(self):
        for s in self.world.stars:
            if isinstance(s, Sol):
                return s
        
        return None # Uh?


    def tick(self):
        # if orders == Orders.RETREAT:
        # elif orders == Orders.DEFEND:
        # elif orders == Orders.PATROL:
        # elif orders == Orders.ATTACK:
        # elif orders == Orders.EXPLORE:
        # elif orders == Orders.INVESTIGATE:
        pass

