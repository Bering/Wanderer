import subsystem
from inventory import Inventory

class Ship:
    def __init__(self, name, crew, hull, fuel, reactors, jump, shields, stealth, dampening, railguns, masers, missiles, nukes, inventory):
        self.name = name
        self.crew_max = crew
        self.hull_max = hull
        self.fuel_max = fuel
        self.power_max = 0
        self.power = 0
        self.shields_max = 0
        self.subsystems = []
        self.inventory = Inventory(inventory)

        for n in range(reactors):
            self.subsystems.append(subsystem.Reactor(self))

        self.subsystems.append(subsystem.Sensors(self))

        if jump:
            self.subsystems.append(subsystem.JumpDrive(self))
        
        if shields:
            self.subsystems.append(subsystem.ShieldEmitter(self))
        
        if stealth:
            self.subsystems.append(subsystem.StealthField(self))
        
        if dampening:
            self.subsystems,append(subsystem.DampeningField(self))
        
        self.railguns = railguns
        self.masers = masers
        self.missiles_max = missiles
        self.nukes_max = nukes

        self.crew = self.crew_max
        self.hull = self.hull_max
        self.fuel = self.fuel_max
        self.shields = self.shields_max
        self.missiles = self.missiles_max
        self.nukes = self.nukes_max
