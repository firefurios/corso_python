from typing import List
import numpy as np

G = 6.67e-11


class SolarSystem:
    pass


class Planet:

    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.__r0 = np.array(position)
        self.__v0 = np.array(velocity)

    def start_orbit(self):
        self.position: List[np.ndarray] = [self.__r0]
        self.velocity: List[np.ndarray] = [self.__v0]
        self.acceleration: List[np.ndarray] = []

    def get_kinetic_energy(self, t: int) -> float:
        return 0.5*self.mass * np.linalg.norm(self.velocity[t])**2

    def get_potential_energy(self, system: SolarSystem, t: int) -> float:
        potential_energy = 0
        for planet_j in system.get_planets():
            if(self != planet_j):
                rij = self.position[t] - planet_j.position[t]
                potential_energy -= (G * planet_j.mass) / np.linalg.norm(rij)
        return potential_energy * self.mass


class SolarSystem:

    def __init__(self, planets: List[Planet]):
        self.__planets = planets

    def get_planets(self) -> List[Planet]:
        return self.__planets

    def calculate_orbits(self, dt: float, t: int):
        N = int(t/dt)
        self.__start_orbit()
        self.__calculate_next_planets_acceleration(dt)
        for t in range(N-1):
            self.__calculate_next_planets_position(dt)
            self.__calculate_next_planets_acceleration(dt)
            self.__calculate_next_planets_velocity(dt)

    def __start_orbit(self):
        for planet in self.__planets:
            planet.start_orbit()

    def __calculate_next_planets_position(self, dt):
        for planet in self.__planets:
            next_position = planet.position[-1] + planet.velocity[-1] * dt + \
                planet.acceleration[-1] * (0.5*dt*dt)

            planet.position.append(next_position)

    def __calculate_next_planets_velocity(self, dt):
        for planet in self.__planets:
            next_velocity = planet.velocity[-1] + \
                0.5 * (planet.acceleration[-2] + planet.acceleration[-1]) * dt

            planet.velocity.append(next_velocity)

    def __calculate_next_planets_acceleration(self, dt):
        for planet_i in self.__planets:
            next_acceleration_i = np.zeros(3)

            for planet_j in self.__planets:
                if(planet_i != planet_j):
                    next_acceleration_i += self.__get_gravity_field(
                        planet_i, planet_j, -1)

            planet_i.acceleration.append(next_acceleration_i)

    def __get_gravity_field(self, planet_i: Planet, planet_j: Planet, t: int):
        rij = planet_i.position[t] - planet_j.position[t]
        return -G * planet_j.mass * rij / (np.linalg.norm(rij)**3)

    def get_energy(self, t: int):
        return sum(planet.get_kinetic_energy(t) + planet.get_potential_energy(self, t)
                   for planet in self.__planets)
