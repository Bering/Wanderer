import subsystem

class Ship:
    def __init__(self, name, crew, hull, reactors, fuel, jump, shields, stealth, dampening, railguns, masers, missiles, nukes):
        self.name = name
        self.crew_max = crew
        self.hull_max = hull
        self.fuel_max = fuel
        self.subsystems = []

        for n in range(reactors):
            self.subsystems.append(subsystem.Reactor())

        self.subsystems.append(subsystem.Sensors())

        if jump:
            self.subsystems.append(subsystem.JumpDrive())
        
        if shields:
            self.subsystems.append(subsystem.ShieldEmitter())
        
        if stealth:
            self.subsystems.append(subsystem.StealthField())
        
        if dampening:
            self.subsystems,append(subsystem.DampeningField())
        
        self.railguns = railguns
        self.masers = masers
        self.missiles_max = missiles
        self.nukes_max = nukes

        self.crew = self.crew_max
        self.hull = self.hull_max
        self.fuel = self.fuel_max
        self.missiles = self.missiles_max
        self.nukes = self.nukes_max
