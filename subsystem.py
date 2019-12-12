
class SubSystem:
    def __init__(self, name, status_green, status_yellow, status_red, power):
        self.name = name
        self.green = status_green
        self.yellow = status_yellow
        self.red = status_red
        self.power_max = power

        self.status = self.green
        self.power = self.power_max


class Reactor(SubSystem):
    def __init__(self):
        super().__init__(
            "Reactor",
            "Online",
            "Damaged",
            "Critical",
            100
        )

class Sensors(SubSystem):
    def __init__(self):
        super().__init__(
            "Sensors",
            "Online",
            "Offline",
            "Damaged",
            100
        )

class JumpDrive(SubSystem):
    def __init__(self):
        super().__init__(
            "JumpDrv",
            "Ready",
            "Loading",
            "Offline",
            100
        )
        
class ShieldEmitter(SubSystem):
    def __init__(self):
        super().__init__(
            "Shields",
            "Up",
            "Down",
            "Damaged",
            100
        )
        
class StealthField(SubSystem):
    def __init__(self):
        super().__init__(
            "Stealth",
            "Engaged",
            "Offline",
            "Damaged",
            100
        )
        
class DampeningField(SubSystem):
    def __init__(self):
        super().__init__(
            "Dampnng",
            "Online",
            "Offline",
            "Damaged",
            100
        )
        