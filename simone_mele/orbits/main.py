from typing import List
import numpy as np
import matplotlib.pyplot as plt
from columnar import columnar
import json

from solarsystem import *
from solarsystemplotter import *


def get_planets_from_json(planets: dict) -> List[Planet]:
    return [Planet(p['mass'],
                   p['position'] if 'position' in p else [0, 0, 0],
                   p['velocity'] if 'velocity' in p else [0, 0, 0]) for p in planets]


def open_json_file(file: str) -> dict:
    with open(file) as json_file:
        return json.load(json_file)


if __name__ == "__main__":
    example = {
        't': 365,
        'dt': 0.01,
        'objects': [{
            'mass': 5.972e24,
            'position': [1.496e8, 0, 0],
            'velocity': [107208, 0, 0]
        }, {
            'mass': 1.989e30,
        }, {
            'mass': 6.4185e23,
            'position': [2.28e8, 0, 0],
            'velocity': [86677.2, 0, 0]
        }]
    }
    example_json = json.dumps(example)

    print('Each planet must have the mass and can have the initial point and the initial velocity.')
    print('t: time duration of orbits [h]')
    print('dt: time distance between two calculus [h]')
    print('mass: mass of celestial object [Kg]')
    print('position: initial position of celestial object [Km]')
    print('velocity: initial velocity of celestial object [Km/h]')
    print(example_json)
    json_data = open_json_file(input('Insert json file: '))
    planets = get_planets_from_json(json_data['objects'])
    t = int(json_data['t'])
    dt = float(json_data['dt'])

    solar_system = SolarSystem(planets)
    solar_system.calculate_orbits(dt, t)

    initial_energy = solar_system.get_energy(0)
    final_energy = solar_system.get_energy(-1)
    print(columnar([[initial_energy, final_energy, final_energy - initial_energy]],
                   ['Initial energy', 'Final energy', 'Energy difference']))
    fig = plt.figure()
    sysem_plotter = SolarSystemPlotter(solar_system)
    sysem_plotter.plot_orbits(fig, dt, t)
    plt.show()
