from typing import List
import matplotlib.pyplot as plt
from solarsystem import *


class SolarSystemPlotter:
    def __init__(self, solar_system: SolarSystem):
        self.__system = solar_system

    def plot_orbits(self, figure, dt: float, t: int):
        ax = figure.add_subplot(111, projection='3d')

        planets_coords = self.__get_coords()
        self.__set_axis_limits(ax, planets_coords)

        ax.set_title(f'Planets Orbits in {dt} hours')
        for coords in planets_coords:
            self.__plot_planet(ax, coords)

    def __plot_planet(self, ax, coords: List[np.ndarray], markersize=4, color=None):
        if color == None:
            color = np.random.rand(3,)

        px, py, pz = coords[0:3]
        ax.plot3D(px, py, pz, "o", color=color, markersize=0.1)
        ax.plot3D([px[-1]], [py[-1]], [pz[-1]], 'o', color=color,
                  alpha=0.9, markersize=markersize)

    def __set_axis_limits(self, ax, coords):
        ax.set_xlim3d([min([min(p[0]) for p in coords]) - 1,
                       max([max(p[0]) for p in coords]) + 1])
        ax.set_ylim3d([min([min(p[1]) for p in coords]) - 1,
                       max([max(p[1]) for p in coords]) + 1])
        ax.set_zlim3d([min([min(p[2]) for p in coords]) - 1,
                       max([max(p[2]) for p in coords]) + 1])

    def __get_coords(self) -> List[List[np.ndarray]]:
        return [
            [self.__get_xi(planet.position, i) for i in range(0, 3)]
            for planet in self.__system.get_planets()
        ]

    def __get_xi(self, points: np.ndarray, i: int) -> np.ndarray:
        return np.array([point[i] for point in points])
