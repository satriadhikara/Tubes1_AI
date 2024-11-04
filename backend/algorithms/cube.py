import random
import copy
import math
from .list import CustomList as cl

class Cube:
    def __init__(self):
        self.size = 5  # Ukuran kubus
        self.magic_number = self.calculate_magic_number()
        self.grid = self.generate_grid()

    def generate_grid(self):
        numbers = list(
            range(1, self.size**3 + 1)
        )  # Mengisi list dengan angka 1 sampai size^3 yaitu 125 kemudian diacak
        random.shuffle(numbers)
        grid = [
            [[0 for _ in range(self.size)] for _ in range(self.size)]
            for _ in range(self.size)
        ]
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    grid[x][y][z] = numbers.pop(0)
        return grid

    def generate_grid_from_input(self, input_grid):
        grid = [
            [[0 for _ in range(self.size)] for _ in range(self.size)]
            for _ in range(self.size)
        ]
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    grid[x][y][z] = input_grid[x][y][z]
        return grid

    def perfect_magic_cube(self):
        # Kubus yang sudah optimal (dari web https://mathworld.wolfram.com/PerfectMagicCube.html)
        magic_cube = [
            [
                [25, 16, 80, 104, 90],
                [115, 98, 4, 1, 97],
                [42, 111, 85, 2, 75],
                [66, 72, 27, 102, 48],
                [67, 18, 119, 106, 5],
            ],
            [
                [91, 77, 71, 6, 70],
                [52, 64, 117, 69, 13],
                [30, 118, 21, 123, 23],
                [26, 39, 92, 44, 114],
                [116, 17, 14, 73, 95],
            ],
            [
                [47, 61, 45, 76, 86],
                [107, 43, 38, 33, 94],
                [89, 68, 63, 58, 37],
                [32, 93, 88, 83, 19],
                [40, 50, 81, 65, 79],
            ],
            [
                [31, 53, 112, 109, 10],
                [12, 82, 34, 87, 100],
                [103, 3, 105, 8, 96],
                [113, 57, 9, 62, 74],
                [56, 120, 55, 49, 35],
            ],
            [
                [121, 108, 7, 20, 59],
                [29, 28, 122, 125, 11],
                [51, 15, 41, 124, 84],
                [78, 54, 99, 24, 60],
                [36, 110, 46, 22, 101],
            ],
        ]

        return magic_cube

    def calculate_magic_number(self):
        return self.size * (self.size**3 + 1) // 2

    def print_grid(self):
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    print(self.grid[x][y][z], end=" ")
                print()
            print()

    def get_row(self, x, y):
        return self.grid[x][y]

    def get_column(self, x, z):
        return [self.grid[i][x][z] for i in range(self.size)]

    def get_pillar(self, y, z):
        return [self.grid[y][i][z] for i in range(self.size)]

    def get_diagonals(self):
        diagonals = []

        for z in range(self.size):
            diag1 = [self.grid[i][i][z] for i in range(self.size)]
            diag2 = [self.grid[i][self.size - 1 - i][z] for i in range(self.size)]
            diagonals.append((diag1, diag2))

        for y in range(self.size):
            diag1 = [self.grid[i][y][i] for i in range(self.size)]
            diag2 = [self.grid[self.size - 1 - i][y][i] for i in range(self.size)]
            diagonals.append((diag1, diag2))

        for x in range(self.size):
            diag1 = [self.grid[x][i][i] for i in range(self.size)]
            diag2 = [self.grid[x][self.size - 1 - i][i] for i in range(self.size)]
            diagonals.append((diag1, diag2))

        return diagonals

    def evaluate_cube(self):
        total_deviation = 0
        magic_number = self.magic_number

        # Menghitung penyimpangan untuk setiap baris
        for x in range(self.size):
            for y in range(self.size):
                row = self.get_row(x, y)
                sum_row = sum(row)
                deviation = abs(sum_row - magic_number)
                total_deviation += deviation

        # Menghitung penyimpangan untuk setiap kolom
        for y in range(self.size):
            for z in range(self.size):
                column = self.get_column(y, z)
                sum_column = sum(column)
                deviation = abs(sum_column - magic_number)
                total_deviation += deviation

        # Menghitung penyimpangan untuk setiap tiang
        for x in range(self.size):
            for z in range(self.size):
                pillar = self.get_pillar(x, z)
                sum_pillar = sum(pillar)
                deviation = abs(sum_pillar - magic_number)
                total_deviation += deviation

        # Menghitung penyimpangan untuk setiap diagonal
        diagonals = self.get_diagonals()
        for diag_pair in diagonals:
            diag1, diag2 = diag_pair
            sum_diag1 = sum(diag1)
            deviation1 = abs(sum_diag1 - magic_number)
            total_deviation += deviation1
            if diag2:
                sum_diag2 = sum(diag2)
                deviation2 = abs(sum_diag2 - magic_number)
                total_deviation += deviation2
        return total_deviation

    def evaluate_cube_on_grid(self, grid):
        total_deviation = 0
        magic_number = self.magic_number
        # Check rows
        for x in range(self.size):
            for y in range(self.size):
                row = grid[x][y]
                total_deviation += abs(sum(row) - magic_number)

        # Check columns
        for y in range(self.size):
            for z in range(self.size):
                column = [grid[i][y][z] for i in range(self.size)]
                total_deviation += abs(sum(column) - magic_number)

        # Check pillars
        for x in range(self.size):
            for z in range(self.size):
                pillar = [grid[x][i][z] for i in range(self.size)]
                total_deviation += abs(sum(pillar) - magic_number)

        # Check diagonals
        for z in range(self.size):
            diag1 = [grid[i][i][z] for i in range(self.size)]
            diag2 = [grid[i][self.size - 1 - i][z] for i in range(self.size)]
            total_deviation += abs(sum(diag1) - magic_number)
            total_deviation += abs(sum(diag2) - magic_number)

        for y in range(self.size):
            diag1 = [grid[i][y][i] for i in range(self.size)]
            diag2 = [grid[self.size - 1 - i][y][i] for i in range(self.size)]
            total_deviation += abs(sum(diag1) - magic_number)
            total_deviation += abs(sum(diag2) - magic_number)

        for x in range(self.size):
            diag1 = [grid[x][i][i] for i in range(self.size)]
            diag2 = [grid[x][self.size - 1 - i][i] for i in range(self.size)]
            total_deviation += abs(sum(diag1) - magic_number)
            total_deviation += abs(sum(diag2) - magic_number)

        # space_diag1 = [grid[i][i][i] for i in range(self.size)]
        # space_diag2 = [grid[i][i][self.size - 1 - i] for i in range(self.size)]
        # space_diag3 = [grid[i][self.size - 1 - i][i] for i in range(self.size)]
        # space_diag4 = [grid[self.size - 1 - i][i][i] for i in range(self.size)]

        # # Calculate and add their deviations
        # total_deviation += abs(sum(space_diag1) - magic_number)
        # total_deviation += abs(sum(space_diag2) - magic_number)
        # total_deviation += abs(sum(space_diag3) - magic_number)
        # total_deviation += abs(sum(space_diag4) - magic_number)

        return total_deviation

    def steepest_ascent_hill_climb(self, max_iterations=1000):
        current_deviation = self.evaluate_cube()
        best_grid = copy.deepcopy(self.grid)
        message = ""
        iterations_history = [{"iteration": 0, "obj_value": current_deviation}]

        if current_deviation == 0:
            message = "Already at global optimum"
            return (self.grid, current_deviation, 0, message, iterations_history)

        for iteration in range(max_iterations):
            best_deviation = current_deviation
            found_improvement = False

            # Generate all unique neighbors by swapping each unique pair of elements
            for x1 in range(self.size):
                for y1 in range(self.size):
                    for z1 in range(self.size):
                        for x2 in range(self.size):
                            for y2 in range(self.size):
                                for z2 in range(self.size):
                                    if (x1, y1, z1) >= (x2, y2, z2):
                                        continue

                                    neighbor = copy.deepcopy(self.grid)
                                    neighbor[x1][y1][z1], neighbor[x2][y2][z2] = (
                                        neighbor[x2][y2][z2],
                                        neighbor[x1][y1][z1],
                                    )

                                    deviation = self.evaluate_cube_on_grid(neighbor)

                                    if deviation < best_deviation:
                                        best_deviation = deviation
                                        best_grid = neighbor
                                        found_improvement = True

            if found_improvement and best_deviation < current_deviation:
                self.grid = best_grid
                current_deviation = best_deviation
                print(f"Iteration {iteration + 1}: Deviation = {current_deviation}")
                iterations_history.append(
                    {"iteration": iteration + 1, "obj_value": current_deviation}
                )
            else:
                if current_deviation == 0:
                    message = "Reached global optimum"
                else:
                    message = "Reached local optimum"
                break

        return (
            self.grid,
            current_deviation,
            (iteration + 1),
            message,
            iterations_history,
        )

    def sideways(self, max_iterations=1000):
        past_cubes = cl()
        current_deviation = self.evaluate_cube()
        best_grid = copy.deepcopy(self.grid)
        message = ""
        iterations_history = [{"iteration": 0, "obj_value": current_deviation}]
        if current_deviation == 0:
            print("Already at global optimum")
            return self.grid, current_deviation, 0

        for iteration in range(max_iterations):
            best_deviation = current_deviation
            found_improvement = False
            past_cubes.add(self.grid)
            # Generate all unique neighbors by swapping each unique pair of elements
            for x1 in range(self.size):
                for y1 in range(self.size):
                    for z1 in range(self.size):
                        for x2 in range(self.size):
                            for y2 in range(self.size):
                                for z2 in range(self.size):
                                    if (x1, y1, z1) >= (
                                        x2,
                                        y2,
                                        z2,
                                    ):  # Avoid duplicate and self-swaps
                                        continue

                                    # Create a copy of the grid and perform the swap
                                    neighbor = copy.deepcopy(self.grid)
                                    neighbor[x1][y1][z1], neighbor[x2][y2][z2] = (
                                        neighbor[x2][y2][z2],
                                        neighbor[x1][y1][z1],
                                    )

                                    # Evaluate the neighbor
                                    deviation = self.evaluate_cube_on_grid(neighbor)

                                    # Update the best neighbor found
                                    if (
                                        deviation <= best_deviation
                                        and not past_cubes.isIn(neighbor)
                                    ):
                                        best_deviation = deviation
                                        best_grid = neighbor
                                        found_improvement = True

            # Move to the best neighbor if it's better than the current
            if found_improvement and best_deviation <= current_deviation:
                if best_deviation < current_deviation:
                    past_cubes.reset()
                self.grid = best_grid
                current_deviation = best_deviation
                print(
                    f"Iteration {iteration + 1}: Deviation = {current_deviation}, Visited Cubes : {past_cubes.size}"
                )
                iterations_history.append(
                    {"iteration": iteration + 1, "obj_value": current_deviation}
                )
            else:
                if current_deviation == 0:
                    message = "Reached global optimum"
                else:
                    message = "Reached local optimum"
                break

        print(self.grid, current_deviation, iteration + 1)
        return (
            self.grid,
            current_deviation,
            (iteration + 1),
            message,
            iterations_history,
        )
    
    def stochastic_hill_climb(self, max_iterations=1000, max_attempts=100):
        current_deviation = self.evaluate_cube()
        best_grid = copy.deepcopy(self.grid)

        if current_deviation == 0:
            print("Already at global optimum")
            return self.grid, current_deviation, 0

        for iteration in range(max_iterations):
            found_improvement = False

            for attempt in range(max_attempts):
                # Pilih dua titik acak dalam grid untuk melakukan swap
                x1, y1, z1 = random.randint(0, self.size - 1), random.randint(0, self.size - 1), random.randint(0, self.size - 1)
                x2, y2, z2 = random.randint(0, self.size - 1), random.randint(0, self.size - 1), random.randint(0, self.size - 1)

                # Hindari swap dengan elemen yang sama
                while (x1, y1, z1) == (x2, y2, z2):
                    x2, y2, z2 = random.randint(0, self.size - 1), random.randint(0, self.size - 1), random.randint(0, self.size - 1)

                # Lakukan swap di grid baru
                neighbor = copy.deepcopy(self.grid)
                neighbor[x1][y1][z1], neighbor[x2][y2][z2] = neighbor[x2][y2][z2], neighbor[x1][y1][z1]

                # Evaluasi tetangga
                deviation = self.evaluate_cube_on_grid(neighbor)

                # Jika tetangga lebih baik, pindah ke tetangga tersebut
                if deviation < current_deviation:
                    self.grid = neighbor
                    current_deviation = deviation
                    found_improvement = True
                    print(f"Iteration {iteration + 1}, Attempt {attempt + 1}: Deviation = {current_deviation}")
                    break  # Lanjut ke iterasi berikutnya

            # Jika tidak ada perbaikan ditemukan, maka berhenti
            if not found_improvement:
                print("Reached local optimum")
                break

            # Jika mencapai global optimum, hentikan
            if current_deviation == 0:
                print("Reached global optimum")
                break

        print(self.grid, current_deviation, iteration + 1)
        return self.grid, current_deviation, (iteration + 1)

    def genetic_algorithm(self, population_size, iterations):
        # Generate initial population
        population = [self.generate_grid() for _ in range(population_size)]
        
        # Evaluate initial state (first individual in population)
        initial_state = copy.deepcopy(population[0])
        initial_fitness = self.evaluate_cube_on_grid(initial_state)

        best_fitness = float("inf")
        best_individual = None

        for iteration in range(iterations):
            # Evaluate fitness of each individual
            fitness_scores = [(self.evaluate_cube_on_grid(individual), individual) for individual in population]
            fitness_scores.sort(key=lambda x: x[0])  # Sort by fitness (lower is better)

            # Keep track of the best solution
            if fitness_scores[0][0] < best_fitness:
                best_fitness, best_individual = fitness_scores[0]

            # Selection: Take the top half of the population
            selected_population = [individual for _, individual in fitness_scores[:population_size // 2]]

            # Crossover and mutation to produce the next generation
            next_population = []
            while len(next_population) < population_size:
                parent1 = random.choice(selected_population)
                parent2 = random.choice(selected_population)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                next_population.append(child)

            # Update population
            population = next_population

        # Final output
        final_state = best_individual
        final_fitness = best_fitness

        # Print initial and final states and fitness values
        print("Initial State:")
        self.output_grid(initial_state)
        print("Initial Fitness (Objective Function):", initial_fitness)
        print("\nFinal State:")
        self.output_grid(final_state)
        print("Final Fitness (Objective Function):", final_fitness)

        # Return outputs as requested
        return initial_state, final_state, final_fitness

    def crossover(self, parent1, parent2):
        child = [[[0 for _ in range(self.size)] for _ in range(self.size)] for _ in range(self.size)]
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    child[x][y][z] = parent1[x][y][z] if random.random() < 0.5 else parent2[x][y][z]
        return child

    def mutate(self, grid, mutation_rate=0.01):
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    if random.random() < mutation_rate:
                        a, b, c = random.randint(0, self.size - 1), random.randint(0, self.size - 1), random.randint(0, self.size - 1)
                        grid[x][y][z], grid[a][b][c] = grid[a][b][c], grid[x][y][z]
        return grid

    def output_grid(self, grid):
        for x in range(self.size):
            print(f"Layer {x + 1}:")
            for y in range(self.size):
                print(" ".join(f"{grid[x][y][z]:3}" for z in range(self.size)))
            print()

# def get_user_input():
#     population_size = int(input("Enter the population size: "))
#     iterations = int(input("Enter the number of iterations: "))
#     return population_size, iterations
    

# def main():
#     cube = Cube()
#     print("Initial Deviation:", cube.evaluate_cube())

#     start_time = time.time()
#     cube.stochastic_hill_climb()
#     end_time = time.time()

#     print(f"Time taken: {end_time - start_time} seconds")

# def main():
#     # Get user input
#     population_size, iterations = get_user_input()

#     # Create an instance of Cube
#     cube = Cube()

#     # Run the genetic algorithm
#     initial_state, final_state, final_fitness = cube.genetic_algorithm(population_size, iterations)

# if __name__ == "__main__":
#     main()

    def random_restart_hill_climb(self, max_restarts=2, max_iterations=1000):
        best_grid = None
        best_deviation = float("inf")
        restart_count = 0
        message = ""
        best_iterations_history = []
        iterations_per_restart = []
        best_iterations = 0
        best_initial_obj_value = 0  # Track initial obj value of best restart

        while restart_count < max_restarts:
            self.grid = self.generate_grid()
            print(f"\nRestart {restart_count + 1}/{max_restarts}")
            restart_count += 1

            current_deviation = self.evaluate_cube()
            print(f"Initial Deviation for this run: {current_deviation}")

            final_grid, final_deviation, iterations, _, step_history = (
                self.steepest_ascent_hill_climb(max_iterations)
            )

            print(f"iterations: {iterations}")
            iterations_per_restart.append(iterations)

            if final_deviation < best_deviation:
                best_deviation = final_deviation
                best_iterations = iterations
                best_grid = copy.deepcopy(final_grid)
                best_iterations_history = step_history
                best_initial_obj_value = current_deviation  # Save initial obj value
                print(
                    f"New best deviation found: {best_deviation} after {restart_count} restarts"
                )

            if best_deviation == 0:
                message = "Found global optimum"
                print("Global optimum found!")
                break

            stuck_in_local_optimum = final_deviation == current_deviation

            if stuck_in_local_optimum:
                print("Stuck in local optimum, restarting...")

        if best_deviation > 0:
            message = f"Reached max restarts ({max_restarts})"

        print(f"\nBest Deviation after {restart_count} restarts: {best_deviation}")
        self.grid = best_grid

        return (
            self.grid,
            best_deviation,
            best_iterations,
            message,
            best_iterations_history,
            restart_count,
            iterations_per_restart,
            best_initial_obj_value,  # Add to return tuple
        )

    def simulated_annealing(self, initial_temp=10000, min_temp=1, cooling_rate=0.9995):
        current_grid = copy.deepcopy(self.grid)
        current_deviation = self.evaluate_cube()
        temperature = initial_temp
        iteration = 0
        frequency = 0
        message = ""
        iterations_history = []

        while temperature > min_temp:
            if current_deviation == 0:
                break
            # Generate a neighbor by swapping two random elements
            neighbor_grid = copy.deepcopy(current_grid)
            x1, y1, z1 = (
                random.randint(0, self.size - 1),
                random.randint(0, self.size - 1),
                random.randint(0, self.size - 1),
            )
            x2, y2, z2 = (
                random.randint(0, self.size - 1),
                random.randint(0, self.size - 1),
                random.randint(0, self.size - 1),
            )

            # Swap two values in the neighbor grid
            neighbor_grid[x1][y1][z1], neighbor_grid[x2][y2][z2] = (
                neighbor_grid[x2][y2][z2],
                neighbor_grid[x1][y1][z1],
            )

            # Evaluate the neighbor's deviation
            self.grid = neighbor_grid
            neighbor_deviation = self.evaluate_cube()
            self.grid = current_grid

            # Calculate the change in deviation (energy difference)
            delta = neighbor_deviation - current_deviation

            # Decide whether to accept the neighbor
            if delta < 0:
                current_grid = neighbor_grid
                current_deviation = neighbor_deviation
                iterations_history.append({"iteration": iteration + 1, "eET": 1})
            else:
                frequency += 1
                acceptance_probability = math.exp(-delta / temperature)
                if random.random() < acceptance_probability:
                    current_grid = neighbor_grid
                    current_deviation = neighbor_deviation
                iterations_history.append(
                    {
                        "iteration": iteration + 1,
                        "eET": round(acceptance_probability, 5),
                    }
                )

            temperature *= cooling_rate

            print(
                f"Iteration {iteration + 1}, Temperature = {temperature:.2f}, "
                f"Deviation = {current_deviation}"
            )

            iteration += 1

        if current_deviation == 0:
            message = "Reached global optimum"
        else:
            message = "Reached minimum temperature"

        # Update the grid to the best configuration found
        self.grid = current_grid

        return (
            copy.deepcopy(current_grid),
            current_deviation,
            iteration,
            frequency,
            message,
            iterations_history,
        )


# def main():
#     cube = Cube()
#     # print(cube.evaluate_cube())
#     print("Initial Deviation:", cube.evaluate_cube())
#     start_time = time.time()
#     # cube.steepest_ascent_hill_climb()
#     cube.sideways()
#     end_time = time.time()
#     print(f"Time taken: {end_time - start_time} seconds")


# if __name__ == "__main__":
#     main()