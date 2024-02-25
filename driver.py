# driver.py
from tyre import Tyre
import random

class Driver:
    def __init__(self, name, tyre_color):
        self.name = name
        self.tyre = Tyre(tyre_color)
        self.time_penalty = 0
        self.stints = []


    def change_tyre(self, new_tyre_color):
        self.tyre = Tyre(new_tyre_color)


    def perform_pit_stop(self):
        # Časová penalizace za pit stop
        pit_stop_penalty = 10  # Předpokládaná časová penalizace za pit stop (například 10 sekund)
        self.time_penalty += pit_stop_penalty
        # Přiřazení nové sady pneumatik
        # self.tyre = Tyre(self.tyre.color)
        self.change_tyre(random.choice(["red", "yellow", "white"]))
        self.stints.append((self.tyre.color, self.tyre.durability[self.tyre.color] ))

    def get_total_time(self, race_duration):
        return race_duration + self.time_penalty

    def perform_lap(self):
        self.tyre.decrease_durability()
        if self.tyre.needs_pit_stop():
            self.perform_pit_stop()
            print(f"{self.name} provedl pit stop.")