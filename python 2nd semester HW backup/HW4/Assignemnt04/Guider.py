from Wizard import *


class Guider(Wizard):
    def __init__(self, name, house, potions, charms, play_quidditch, in_dorm=False):
        # Initializing the upper class first.
        Wizard.__init__(self, name, house, potions, charms, in_dorm)
        # The subclass unique field.
        self.play_quidditch = play_quidditch

    def __repr__(self):
        return f"Guider ({self.name}, {self.house.name}, {self.get_avg()})"
