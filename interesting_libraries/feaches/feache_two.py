import random
import heapq

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


class CityGrid:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.grid = [[0 for _ in range(M)] for _ in range(N)]
        self.tower_range = 0
        self.towers= {}

    def place_obstructed_blocks(self, coverage_threshold=0.3):
        target_coverage = self.N * self.M * coverage_threshold
        obstructed_count = 0

        while obstructed_count < target_coverage:
            row = random.randint(0, self.N - 1)
            col = random.randint(0, self.M - 1)

            if self.grid[row][col] == 0:
                self.grid[row][col] = 1
                obstructed_count += 1
        return self.grid

    def place_tower(self, row, col, tower_range):
        self.tower_range = tower_range
        tower_id = len(self.towers) + 3
        self.towers[tower_id] = (row, col)
        for i in range(max(0, row - self.tower_range), min(self.N, row + self.tower_range + 1)):
            for j in range(max(0, col - self.tower_range), min(self.M, col + self.tower_range + 1)):
                self.grid[i][j] = 2
        self.grid[row][col] = tower_id

    def place_minimum_towers(self, range_R):
        uncovered_blocks = set((row, col) for row in range(self.N) for col in range(self.M) if self.grid[row][col] == 0)
        towers_placed = 0

        while uncovered_blocks:
            row, col = uncovered_blocks.pop()
            self.place_tower(row, col, range_R)
            towers_placed += 1

            for i in range(max(0, row - range_R), min(self.N, row + range_R + 1)):
                for j in range(max(0, col - range_R), min(self.M, col + range_R + 1)):
                    if (i, j) in uncovered_blocks:
                        uncovered_blocks.remove((i, j))

        return towers_placed
    def find_most_reliable_path(self, start_tower, end_tower):
        start_row, start_col = self.towers[start_tower]
        end_row, end_col = self.towers[end_tower]
        distances = {(r, c): float('inf') for r in range(self.N) for c in range(self.M)}
        distances[(start_row, start_col)] = 0
        visited = set()
        previous_nodes = {}

        pq = [(0, (start_row, start_col))]
        while pq:
            current_distance, (row, col) = heapq.heappop(pq)

            def get_key(d, value):
                for k, v in d.items():
                    if v == value:
                        return k

            current_tower = get_key(self.towers, (row, col))

            if (row, col) == (end_row, end_col):
                path = [(row, col)]
                while (row, col) in previous_nodes:
                    row, col = previous_nodes[(row, col)]
                    path.append((row, col))
                return path[::-1]

            if (row, col) not in visited:
                visited.add((row, col))

                # Explore neighbors within tower range
                for i in range(max(0, row - self.tower_range - 1), min(self.N, row + self.tower_range + 2)):
                    for j in range(max(0, col - self.tower_range - 1), min(self.M, col + self.tower_range + 2)):
                        if self.grid[i][j] >= 3 and self.grid[i][j] != current_tower:
                            neighbor_distance = current_distance + 1
                            if neighbor_distance < distances[(i, j)]:
                                distances[(i, j)] = neighbor_distance
                                heapq.heappush(pq, (neighbor_distance, (i, j)))
                                previous_nodes[(i, j)] = (row, col)
        print("Не удалось проложить путь")
        return []



    def visualize_grid(self, base_grid):
        plt.figure(figsize=(self.M, self.N))

        cmap = ListedColormap([(0.4, 0.1, 0.8),
                               (0.7, 0.1, 0.5),
                               (0.1, 0.8, 0.8, 0.5),
                               (0.0, 0.9, 0.3)])
        bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
        norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

        plt.imshow(self.grid, interpolation='none', cmap=cmap, norm=norm)

        plt.colorbar(ticks=[0, 1, 2, 3], boundaries=bounds, format='%1i', 
                     orientation='vertical')

        plt.xticks(np.arange(-0.5, self.M, 1), [])
        plt.yticks(np.arange(-0.5, self.N, 1), [])
        plt.grid(color='black', linewidth=1)

        plt.show()

    def visualize_path(self, path):
        plt.figure(figsize=(self.M, self.N))

        cmap = ListedColormap([(0.4, 0.1, 0.8),
                               (0.7, 0.1, 0.5),
                               (0.1, 0.8, 0.8, 0.5),
                               (0.0, 0.9, 0.3)])
        bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
        norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

        plt.imshow(self.grid, interpolation='none', cmap=cmap, norm=norm)

        for step, (i, j) in enumerate(path, start=1):
            plt.plot(j, i, marker='o', markersize=30, color='red')
            plt.text(j, i, str(step), ha='center', va='center', color='white', fontsize=30)

        plt.colorbar(ticks=[0, 1, 2, 3], boundaries=bounds, format='%1i', orientation='vertical')

        plt.xticks(np.arange(-0.5, self.M, 1), [])
        plt.yticks(np.arange(-0.5, self.N, 1), [])
        plt.grid(color='black', linewidth=1)
        plt.show()

    def print_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))


if __name__ == "__main__":
    N, M = 10, 10
    city = CityGrid(N, M)
    base_grid = city.place_obstructed_blocks()
    city.visualize_grid(base_grid)
    tower_range = 1
    city.place_minimum_towers(tower_range)
    city.visualize_grid(base_grid)

    path = city.find_most_reliable_path(4, 7)
    city.print_grid()
    print(city.towers)
    print(path)

    city.visualize_path(path)
    