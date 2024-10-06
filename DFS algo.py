import random
import matplotlib.pyplot as plt
import numpy as np

def generate_maze(n, m):
    maze = np.zeros((n, m))
    
    # Depth-first search
    def carve(x, y):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + 2 * dx, y + 2 * dy
            if 1 <= nx < n and 1 <= ny < m and maze[nx, ny] == 0:
                maze[nx - dx, ny - dy] = 1  # Path between
                maze[nx, ny] = 1
                carve(nx, ny)

    maze[1, 1] = 1
    carve(1, 1)
    return maze

def show_maze(maze):
    plt.imshow(maze, cmap='binary')
    plt.xticks([]), plt.yticks([])
    plt.show()

maze = generate_maze(25, 25)
show_maze(maze)
