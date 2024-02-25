class Tyre:
    def __init__(self, color):
        self.color = color
        self.base_speed = {"red": 89, "yellow": 90, "white": 91}  # Základní rychlost pneumatik v sekundách na kolo
        self.degradation_rate = {"red": 0.01, "yellow": 0.008, "white": 0.005}  # Míra opotřebení na kolo
        self.durability = {"red": 10, "yellow": 20, "white": 30}  # Kolik kol pneumatika vydrží
        self.current_durability = self.durability[color]  # Aktuální opotřebení, na začátku stejné jako durability
        self.halfway_point = self.durability[color] // 2  # Polovina durability

    def get_speed_per_lap(self):
        if self.current_durability > self.halfway_point:
            # Normální chování pneumatik v první polovině životního cyklu
            degraded_speed = self.base_speed[self.color]
        else:
            # Začíná degradace pneumatik po dosažení poloviny životního cyklu
            degraded_speed = self.base_speed[self.color] * (1 + self.degradation_rate[self.color] * (self.durability[self.color] - self.current_durability))
        return degraded_speed

    def decrease_durability(self):
        # Při každém kole se snižuje durability
        self.current_durability -= 1

    def needs_pit_stop(self):
        # Podmínka pro nutnost pit stopu
        return self.current_durability <= 0