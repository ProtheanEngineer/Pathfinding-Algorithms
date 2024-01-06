import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import heapq
from tkinter import simpledialog
import tkinter as tk
from breadth_first_search import bfs
from depth_first_search import dfs
from dijkstra_algorithm import dijkstra
from a_algorithm import heuristic, astar

def visualize_pathfinding_algorithm(canvas, maze, start, goal, algorithm):
    cell_size = 20
    
    # Display the maze on the canvas
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 1:
                color = "black"  # Walls
            elif cell == 2:
                color = "green"  # Start
            elif cell == 3:
                color = "yellow"  # Goal
            else:
                color = "white"  # Open paths
            canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill=color, outline=color)

    # Call the algorithm to get the path
    path = algorithm(maze, start, goal)
    if path:
        # Plot the path on the canvas
        for x, y in path:
            canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill="blue", outline="blue")

    # Update the Tkinter window
    canvas.update_idletasks()
            
# Additional helper function for running the algorithm
def run_algorithm(algorithm, maze, start, goal, canvas, root):
    visualize_pathfinding_algorithm(canvas, maze, start, goal, algorithm, root)
