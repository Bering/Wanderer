
class SubSystem:
    def __init__(self, ship, name, status_green, status_yellow, status_red, power):
        self.ship = ship
        self.name = name
        self.green = status_green
        self.yellow = status_yellow
        self.red = status_red
        self.status = self.green
        self.ship.power -= power    


class Reactor(SubSystem):
    def __init__(self, ship):
        super().__init__(
            ship,
            "Reactor",
            "Online",
            "Damaged",
            "Critical",
            -1000
        )
        self.ship.power_max += 1000

class Sensors(SubSystem):
    def __init__(self, ship):
        super().__init__(
            ship,
            "Sensors",
            "Online",
            "Offline",
            "Damaged",
            100
        )

class JumpDrive(SubSystem):
    def __init__(self, ship):
        super().__init__(
            ship,
            "JumpDrive",
            "Ready",
            "Loading",
            "Offline",
            100
        )
        
class ShieldEmitter(SubSystem):
    def __init__(self, ship):
        super().__init__(
            ship,
            "Shields",
            "Up",
            "Down",
            "Damaged",
            500
        )
        self.ship.shields_max += 100
        
class StealthField(SubSystem):
    def __init__(self, ship):
        super().__init__(
            ship,
            "Stealth",
            "Engaged",
            "Offline",
            "Damaged",
            100
        )
        
class DampeningField(SubSystem):
    def __init__(self, ship):
        super().__init__(
            ship,
            "Dampening",
            "Online",
            "Offline",
            "Damaged",
            250
        )
        