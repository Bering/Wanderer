from ship import Ship

class TheFlyingDutchman(Ship):
    def __init__(self):
        super().__init__(
            "The Flying Dutchman",
            200,    # crew
            100,    # hull
            999,    # fuel
            1,      # reactors
            1,      # jump drive
            1,      # shield emiters
            1,      # stealth field
            0,      # dampening field
            0,      # railguns
            1,      # masers
            20,     # missiles
            10,     # nukes
            99999   # inventory
        )
        self.inventory.add("Food (Rations)", 1, 1000)
        self.inventory.add("Food (Water)", 1, 1000)
        self.inventory.add("Food (Spirits)", 1, 100)
