import random
import time
import matplotlib.pyplot as plt
from cube import Cube

class GeneticAlgorithm:
    def __init__(self, population_size, iterations):
        self.population_size = population_size
        self.iterations = iterations
        self.best_objective_values = []
        self.avg_objective_values = []

    def objective_function(self, cube):
        magic_number = cube.magic_number
        total_error = 0
        
        # Evaluasi diagonal dari kubus dan normalisasi error
        for diag_pair in cube.get_diagonals():
            for diag in diag_pair:
                # Hitung error per diagonal dan skalakan agar setiap error maksimal menjadi sekitar 10
                diagonal_error = abs(sum(diag) - magic_number)
                normalized_error = (diagonal_error / magic_number) * 10  # Normalisasi dalam skala 0-10
                total_error += normalized_error
        
        # Penalti untuk angka yang berulang, skalakan agar tetap dalam batas 0-10
        flattened_grid = [num for layer in cube.grid for row in layer for num in row]
        duplicate_count = len(flattened_grid) - len(set(flattened_grid))
        total_error += duplicate_count * 2  # Penalti kecil untuk setiap angka duplikat
        
        # Skala total error agar berada dalam rentang 0-100
        scaled_total_error = min(total_error, 100)  # Batasi nilai maksimum menjadi 100
        
        return scaled_total_error

    def initialize_population(self):
        return [Cube() for _ in range(self.population_size)]

    def select_parents(self, population):
        population.sort(key=self.objective_function)
        return population[:2]

    def crossover(self, parent1, parent2):
        child = Cube()
        for _ in range(random.randint(1, 5)):
            x1, y1, z1 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
            x2, y2, z2 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
            child.grid[x1][y1][z1], child.grid[x2][y2][z2] = parent1.grid[x1][y1][z1], parent2.grid[x2][y2][z2]
        return child

    def mutate(self, cube):
        # Kurangi jumlah mutasi agar lebih terarah
        num_mutations = random.randint(1, 3)  # Hanya melakukan 1 hingga 3 mutasi per iterasi
        for _ in range(num_mutations):
            x1, y1, z1 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
            x2, y2, z2 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
            cube.grid[x1][y1][z1], cube.grid[x2][y2][z2] = cube.grid[x2][y2][z2], cube.grid[x1][y1][z1]

    def run(self):
        start_time = time.time()
        population = self.initialize_population()
        initial_state = [row[:] for row in population[0].grid]  # Save the initial state

        for iteration in range(self.iterations):
            objective_values = [self.objective_function(cube) for cube in population]
            avg_objective = sum(objective_values) / self.population_size
            best_objective = min(objective_values)
            self.avg_objective_values.append(avg_objective)
            self.best_objective_values.append(best_objective)

            parents = self.select_parents(population)
            new_population = []
            for _ in range(self.population_size):
                child = self.crossover(parents[0], parents[1])
                if random.random() < 0.1:
                    self.mutate(child)
                new_population.append(child)
            population = new_population

        end_time = time.time()
        duration = end_time - start_time
        best_cube = min(population, key=self.objective_function)

        result = {
            "initial_state": initial_state,
            "final_state": [row[:] for row in best_cube.grid],
            "objective_value": self.objective_function(best_cube),
            "population_size": self.population_size,
            "iterations": self.iterations,
            "duration": duration,
        }

        return result

    def plot_objective_values(self):
        plt.plot(self.best_objective_values, label="Max Objective Function")
        plt.plot(self.avg_objective_values, label="Average Objective Function")
        plt.xlabel("Iteration")
        plt.ylabel("Objective Value")
        plt.legend()
        plt.show()

# Fungsi Input dan Output
def get_user_input():
    population_size = int(input("Enter the population size: "))
    iterations = int(input("Enter the number of iterations: "))
    return population_size, iterations

def print_output(result):
    print("\nInitial state:")
    for row in result["initial_state"]:
            print(row)
    print("\nFinal state:")
    for row in result["final_state"]:
            print(row)
    print("\nObjective function value achieved:", result["objective_value"])
    print("Population size:", result["population_size"])
    print("Iterations:", result["iterations"])
    print("Duration of the search process:", result["duration"], "seconds")

# Menjalankan algoritma dengan input pengguna
def main():
    population_size, iterations = get_user_input()
    ga = GeneticAlgorithm(population_size, iterations)
    result = ga.run()
    print_output(result)
    ga.plot_objective_values()


if __name__ == "__main__":
    main()