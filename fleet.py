from enum import Enum
import random

import config
from body import Body
import jump

class Orders(Enum):
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
        self.home.star.fleets.append(self)
        self.world_x = self.home.star.world_x
        self.world_y = self.home.star.world_y
        self.body_x = home.body_x
        self.body_y = home.body_y

        self.orders = orders
        if not self.orders:
            while not self.orders \
                or self.orders == Orders.RETREAT \
                or self.orders == Orders.INVESTIGATE:
                self.orders = random.choice(list(Orders))

        self.name = self.race.name + ' '
        if self.orders == Orders.DEFEND:
            self.name += "Defense"
        elif self.orders == Orders.PATROL:
            self.name += "Patrol"
        elif self.orders == Orders.ATTACK:
            self.name += "Attack"
        elif self.orders == Orders.EXPLORE:
            self.name += "Exploration"
        elif self.orders == Orders.INVESTIGATE: # can't choose this at random but can be set deliberately
            self.name += "Earth Investigation"
        self.name += " Fleet"

        self.star = home.star
        self.destination = self.set_destination()
        
        self.wait = 0

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
            return self.world.find_sol()   
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
            if s.name == "Sol":
                continue
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
            if s != self.star and s != self.home.star and s.name != "Sol":
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


    def tick(self, player):

        # special case: investigation fleets take 20 turns to organise
        if self.orders == Orders.INVESTIGATE and self.star == self.home.star and self.wait < 20:
            self.wait += 1
            return

        # Jump towards destination system
        if self.star != self.destination:
            if self.star:
                self.star.fleets.remove(self)
                self.star = None
                self.body = None
                self.body_x = 0
                self.body_y = 0
            
            self.world_x, self.world_y = jump.towards(self.world_x, self.world_y, self.destination.world_x, self.destination.world_y)

            if self.world_x == self.destination.world_x and self.world_y == self.destination.world_y:
                self.star = self.destination
                self.star.fleets.append(self)
                self.body = self.star
                self.wait = 0

        # Wait 3 turns for repairs then Attack again (possibly a different system)
        elif self.orders == Orders.RETREAT:
            if self.wait < 3:
                self.wait += 1
            else:
                self.orders = Orders.ATTACK
                self.set_destination()
        
        # Wait for 3 turns then go patrol another system
        elif self.orders == Orders.PATROL:
            if self.wait < 1:
                self.wait += 1
            else:
                self.set_destination()
        
        # Attack for 3 turns then retreat to an allied system
        elif self.orders == Orders.ATTACK:
            if self.wait < 2:
                self.wait += 1
            else:
                self.orders = Orders.RETREAT
                self.set_destination()

        # conduct research for 10 turns then find another system to explore
        elif self.orders == Orders.EXPLORE:
            if self.wait < 10:
                self.wait += 1
            else:
                self.set_destination()
        
        # Game over!
        elif self.orders == Orders.INVESTIGATE:
            print("\n" + self.name + " reached Earth! GAME OVER!\n")

