# race.py
import random

class Race:
    def __init__(self, num_laps):
        self.num_laps = num_laps
        self.drivers = []

    def add_driver(self, driver):
        tyre_colors = ["red", "yellow", "white"]
        random_tyre_color = random.choice(tyre_colors)
        driver.change_tyre(random_tyre_color)
        self.drivers.append(driver)

    def perform_lap(self):
        for driver in self.drivers:
            driver.tyre.decrease_durability()
            self.check_pit_stops()

    def check_pit_stops(self):
        for driver in self.drivers:
            if driver.tyre.needs_pit_stop():
                driver.perform_pit_stop()
                print(f"{driver.name} provedl pit stop.")

    def get_race_results(self):
        race_results = []
        for driver in self.drivers:
            total_time = sum(driver.tyre.get_speed_per_lap() for _ in range(self.num_laps))
            total_time += driver.time_penalty
            race_results.append((driver.name, total_time, driver.tyre.color, self.num_laps, driver.stints))
        return sorted(race_results, key=lambda x: x[1])

    def format_time(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        if hours > 0:
            return f"{hours}:{minutes}:{seconds}".lstrip('0').replace(':0', ':')
        else:
            return f"{minutes}:{seconds}".lstrip('0').replace(':0', ':')

    def simulate_race(self):
        for lap in range(self.num_laps):
            print(f"Kolo č. {lap + 1}")
            self.perform_lap()
            self.check_pit_stops()
            print("Stav jezdců:")
            for driver in self.drivers:
                lap_time_seconds = driver.tyre.get_speed_per_lap()
                lap_time_formatted = self.format_time(lap_time_seconds)
                print(f"{driver.name}: Rychlost: {lap_time_formatted}, Pneumatiky: {driver.tyre.color}, Výdrž: {driver.tyre.current_durability}")
            print()
        print("\nZávod skončil!\n")
        race_results = self.get_race_results()
        print("Výsledek závodu:")
        for position, result in enumerate(race_results, start=1):
            total_time_formatted = self.format_time(result[1])
            print(f"{position}. místo: {result[0]} - Celkový čas: {total_time_formatted}")
            print("Historie stintů:")
            for stint_num, stint_info in enumerate(result[4], start=1):
                stint_time_formatted = self.format_time(stint_info[1])
                print(f"Stint {stint_num}: Pneumatiky: {stint_info[0]}, Ujetá kola: {stint_time_formatted}")
            print()