# season.py
from race import Race

class Season:
    def __init__(self, num_races, num_laps_per_race):
        self.num_races = num_races
        self.num_laps_per_race = num_laps_per_race
        self.races = []

    def add_race(self, race):
        self.races.append(race)

    def simulate_season(self):
        for i, race in enumerate(self.races, start=1):
            print(f"Závod č. {i}")
            race.simulate_race()
            print()