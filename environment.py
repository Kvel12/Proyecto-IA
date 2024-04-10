class Environment:
    def __init__(self, file_path):
        self.grid = self.load_world(file_path)
        self.start = self.find_start()
        self.goal = self.find_goal()
    
    def load_world(self, file_path):
        with open(file_path, 'r') as file:
            grid = [[int(num) for num in line.split()] for line in file]
        return grid
    
    def find_start(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 2:
                    return (i, j)
    
    def find_goal(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 5:
                    return (i, j)
    
    def is_valid_move(self, position):
        x, y = position
        if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] != 1:
            return True
        return False
    
    def get_neighbors(self, position):
        x, y = position
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        valid_neighbors = [(nx, ny) for nx, ny in neighbors if self.is_valid_move((nx, ny))]
        return valid_neighbors
