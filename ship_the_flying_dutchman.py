from ship import Ship

class TheFlyingDutchman(Ship):
    def __init__(self):
        super().__init__(
            "The Flying Dutchman",
            200,    # crew
            100,    # hull
            1,      # reactors
            100,    # fuel
            1,      # jump drive
            1,      # shield emiters
            1,      # stealth field
            0,      # dampening field
            0,      # railguns
            1,      # masers
            20,     # missiles
            10      # nukes
        )
        