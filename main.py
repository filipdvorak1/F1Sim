# main.py
from season import Season
from driver import Driver
from race import Race
import random

def main():
    num_races = 2  # Počet závodů
    num_laps_per_race = 50  # Počet kol na závod
    f1_season = Season(num_races, num_laps_per_race)

    for _ in range(num_races):
        race = Race(num_laps_per_race)
        drivers = [
            Driver("HAM", random.choice(["red", "yellow", "white"])),
            Driver("VER", random.choice(["red", "yellow", "white"])),
            Driver("BOT", random.choice(["red", "yellow", "white"])),
            Driver("LEC", random.choice(["red", "yellow", "white"])),
            Driver("RIC", random.choice(["red", "yellow", "white"]))
        ]
        for driver in drivers:
            race.add_driver(driver)
        f1_season.add_race(race)

    f1_season.simulate_season()

if __name__ == "__main__":
    main()