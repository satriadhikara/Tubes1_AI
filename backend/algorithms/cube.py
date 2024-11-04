import random
import copy
import time
import math


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
                [72, 48, 91, 35, 74],
                [93, 57, 39, 92, 16],
                [109, 103, 46, 18, 121],
                [27, 8, 112, 104, 75],
                [43, 58, 56, 99, 45],
            ],
            [
                [66, 24, 80, 106, 29],
                [111, 38, 23, 84, 59],
                [88, 5, 124, 49, 64],
                [90, 125, 60, 17, 47],
                [1, 82, 14, 67, 123],
            ],
            [
                [34, 110, 41, 6, 52],
                [11, 113, 78, 115, 3],
                [95, 42, 31, 116, 53],
                [114, 4, 69, 20, 117],
                [79, 19, 87, 68, 76],
            ],
            [
                [102, 40, 9, 107, 105],
                [15, 44, 122, 2, 108],
                [25, 70, 97, 50, 54],
                [33, 85, 51, 94, 30],
                [83, 62, 37, 96, 13],
            ],
            [
                [71, 55, 100, 28, 86],
                [77, 32, 81, 7, 119],
                [12, 65, 36, 98, 63],
                [26, 118, 10, 120, 22],
                [73, 101, 89, 21, 61],
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

        return total_deviation

    def steepest_ascent_hill_climb(self, max_iterations=1000):
        current_deviation = self.evaluate_cube()
        best_grid = copy.deepcopy(self.grid)
        message = ""
        iterations_history = [{"iteration": 0, "obj_value": current_deviation}]

        if current_deviation == 0:
            message = "Already at global optimum"
            return self.grid, current_deviation, 0, message, iterations_history

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
        current_deviation = self.evaluate_cube()
        best_grid = copy.deepcopy(self.grid)  # Keep track of the best grid found

        if current_deviation == 0:
            print("Already at global optimum")
            return self.grid, current_deviation, 0

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
                                    if deviation <= best_deviation:
                                        best_deviation = deviation
                                        best_grid = neighbor
                                        found_improvement = True

            # Move to the best neighbor if it's better than the current
            if found_improvement and best_deviation < current_deviation:
                self.grid = best_grid
                current_deviation = best_deviation
                print(f"Iteration {iteration + 1}: Deviation = {current_deviation}")
            else:
                # No improvement found, we may have reached a local optimum
                if current_deviation == 0:
                    print("Reached global optimum")
                else:
                    print("Reached local optimum")
                break

        print(self.grid, current_deviation, iteration + 1)
        return self.grid, current_deviation, (iteration + 1)

    def simulated_annealing(
        self,
        initial_temp=10000,
        min_temp=0.1,
        cooling_rate=0.99995,
    ):
        current_grid = copy.deepcopy(self.grid)
        current_deviation = self.evaluate_cube()
        temperature = initial_temp
        iteration = 0
        frequency = 0
        message = ""
        iterations_history = []

        while temperature > min_temp:
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
                        "eET": round(acceptance_probability, 2),
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
