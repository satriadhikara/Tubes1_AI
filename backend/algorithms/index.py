from .cube import Cube
import time


def solve_cube(algorithm):
    cube = Cube()
    initial_state = cube.grid
    initial_obj_value = cube.evaluate_cube()
    start_time = time.time()
    frequency = None
    population = None
    if algorithm == "hc":
        grid, deviation, iterations, message, iterations_history = (
            cube.steepest_ascent_hill_climb()
        )

    elif algorithm == "hc-sideways":
        grid, deviation, iterations, message, iterations_history = cube.sideways()
    elif algorithm == "sa":
        grid, deviation, iterations, frequency, message, iterations_history = (
            cube.simulated_annealing()
        )
    end_time = time.time()

    return (
        message,
        deviation,
        iterations,
        end_time - start_time,
        grid,
        frequency,
        population,
        initial_state,
        initial_obj_value,
        iterations_history,
    )
