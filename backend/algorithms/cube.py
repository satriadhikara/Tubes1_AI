import random


class Cube:
    def __init__(self):
        self.size = 5  # Ukuran kubus
        self.grid = self.generate_grid() # 3 Dimensional Array
        self.magic_number = self.calculate_magic_number()
        self.value = self.evaluate_cube()
        self.pastGrid = [] # possibly 4 Dimensional array

    def generate_grid(self):
        numbers = list(
            range(1, self.size**3 + 1)
        )  # Mengisi list dengan angka 1 sampai size^3 yaitu 125 kemudian diacak
        random.shuffle(numbers)
        grid = [
            [[0 for _ in range(self.size)] for _ in range(self.size)]
            for _ in range(self.size)
        ]
        index = 0
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    grid[x][y][z] = numbers[index]
                    index += 1
        return grid

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

    def switch(self,x1,y1,z1,x2,y2,z2):
        temp = self.grid[x1][y1][z1]
        self.grid[x1][y1][z1] = self.grid[x2][y2][z2]
        self.grid[x2][y2][z2] = temp

    def getNeighbour(self):
        import copy
        neighbour = None
        max_value = None
        for z1 in range(5):
            for y1 in range(5):
                for x1 in range(5):
                    for z2 in range(5):
                        for y2 in range(5):
                            for x2 in range(5):
                                self.switch(x1,y1,z1,x2,y2,z2)
                                value = self.evaluate_cube()
                                if self.grid not in self.pastGrid:
                                    if max_value is None or value < max_value:
                                        neighbour = copy.deepcopy(self.grid)
                                        max_value = value
                                self.switch(x1,y1,z1,x2,y2,z2)
        print(f"value : {max_value}")
        return neighbour,max_value
    
    def steepestAscent(self):
        import time
        start_time = time.time()
        iterations = 0
        neighbour,neighbour_value = self.getNeighbour()
        # print("first get neighbour")
        while (neighbour_value < self.value) and (neighbour_value is not None):
            iterations += 1
            self.pastGrid.append(self.grid)
            self.grid = neighbour
            self.value = neighbour_value
            neighbour,neighbour_value = self.getNeighbour()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Steepest Ascent ran for {iterations} iterations and {elapsed_time} seconds, final value : {self.value}")

    def steepestSideways(self):
        import time
        start_time = time.time()
        iterations = 0
        neighbour,neighbour_value = self.getNeighbour()
        # print("first get neighbour")
        while neighbour_value <= self.value and (neighbour_value is not None):
            iterations += 1
            self.pastGrid.append(self.grid)
            self.grid = neighbour
            self.value = neighbour_value
            neighbour,neighbour_value = self.getNeighbour()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Steepest Sideways ran for {iterations} iterations and {elapsed_time} seconds, final value : {self.value}")


def main():
    cube = Cube()
    # print(cube.evaluate_cube())
    # cube.steepestAscent()
    cube.steepestSideways()
    cube.print_grid()


if __name__ == "__main__":
    main()