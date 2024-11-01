from .cube import Cube
import time


def solve_cube(initial_state, algorithm):
    cube = Cube()
    cube.grid = cube.generate_grid_from_input(initial_state)
    start_time = time.time()
    if algorithm == "hc":
        grid, deviation, iterations = cube.steepest_ascent_hill_climb()
    # elif algorithm == "sa":
    #     grid, deviation, iterations, frequency =
    # elif algorithm == "ga":
    #     grid, deviation, iterations, population =
    end_time = time.time()
    frequency = None  # temp
    population = None  # temp
    return (
        "Success",
        deviation,
        iterations,
        end_time - start_time,
        grid,
        frequency,
        population,
    )
