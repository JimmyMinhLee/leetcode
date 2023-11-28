"""
Given an m x n 2D binary grid grid which represents a map of '1's (land)
and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. 

You may assume all four edges of the grid are all surrounded by water.
"""
class Problem():
    def __init__(self): 
        pass 

"""
DONE: 11/27/23 
Intuition: 
    As a human, I would walk through the array and check if I'm on land or not. 
    If I am, then I should look at all my neighboring squares and see if I'm connected to something. 
    Then, I put it into a mental list that I've explored this island. 
    I will also keep track of any new pieces of land that I've encountered, since that signals that 
        I've found a new island. 
"""
class DFS():
    def __init__(self, graph):
        self.graph = graph 
        self.num_islands = 0
        self.seen = set()
        pass 

    def search(self):
        for row_idx in range(len(self.graph)):
            for col_idx in range(len(self.graph[0])):
                if self.graph[row_idx][col_idx] == 1: 
                    self.traverse(row_idx, col_idx)
                    self.num_islands += 1

        return self.num_islands

    def traverse(self, row_idx, col_idx): 
        if (row_idx, col_idx) in self.seen: 
            return 
        elif self.graph[row_idx][col_idx] == 0:
            return 
        else:
            self.graph[row_idx][col_idx] = 0 
            self.seen.add((row_idx, col_idx))
            neighbors = self.get_neighbors(row_idx, col_idx)
            for neighbor in neighbors: 
                row, col = neighbor[0], neighbor[1]
                self.traverse(row, col)

    def get_neighbors(self, row_idx, col_idx):
        neighbors = []
        num_rows = len(self.graph)
        num_cols = len(self.graph[0])
        if row_idx > 0: 
            neighbors.append((row_idx - 1, col_idx))
        if row_idx < num_rows - 1:
            neighbors.append((row_idx + 1, col_idx))
        if col_idx > 0: 
            neighbors.append((row_idx, col_idx - 1))
        if col_idx < num_cols - 1:
            neighbors.append((row_idx , col_idx + 1))
        return neighbors

dfs_example_one = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1]
]

dfs_solution_one = 2
print(DFS(dfs_example_one).search() == dfs_solution_one)

dfs_example_two = [
        [0]
]
dfs_solution_two = 0 
print(DFS(dfs_example_two).search() == dfs_solution_two)
