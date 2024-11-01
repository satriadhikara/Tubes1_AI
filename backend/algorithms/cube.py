import random
import copy
import time


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

        return total_deviation

    def steepest_ascent_hill_climb(self, max_iterations=1000):
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
                                    if deviation < best_deviation:
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


def main():
    cube = Cube()
    print("Initial Deviation:", cube.evaluate_cube())

    start_time = time.time()
    cube.steepest_ascent_hill_climb()
    end_time = time.time()

    print(f"Time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
