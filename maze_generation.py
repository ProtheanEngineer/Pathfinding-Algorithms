import tkinter as tk
from tkinter import simpledialog, Canvas
import random
from depth_first_search import dfs, get_neighbors

def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def depth_first_search(x, y):
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[y + dy // 2][x + dx // 2] = 0
                maze[ny][nx] = 0
                depth_first_search(nx, ny)

    start_x, start_y = random.randrange(width // 2) * 2, random.randrange(height // 2) * 2
    goal_x, goal_y = random.randrange(width // 2) * 2, random.randrange(height // 2) * 2

    # Mark the border cells as walls
    for i in range(width):
        maze[0][i] = maze[height - 1][i] = 1
    for i in range(height):
        maze[i][0] = maze[i][width - 1] = 1

    maze[start_y][start_x] = 2  # Mark the start cell
    maze[goal_y][goal_x] = 3  # Mark the goal cell

    # Ensure there is a clear path from start to goal
    maze[start_y + 1][start_x] = maze[goal_y - 1][goal_x] = 0

    depth_first_search(start_x, start_y)

    return maze, (start_x, start_y), (goal_x, goal_y)