import tkinter as tk
from tkinter import ttk, Canvas, simpledialog
from maze_generation import generate_maze
from visualization import visualize_pathfinding_algorithm, dijkstra, astar, bfs, dfs

def run_algorithm(algorithm, maze, start, goal, canvas):
    visualize_pathfinding_algorithm(canvas, maze, start, goal, algorithm)

def main():
    # Ask the user for maze dimensions
    maze_size = simpledialog.askinteger("Maze Dimensions", "Enter the size of the maze:")
    if maze_size is None or maze_size <= 0:
        return  # User canceled or provided invalid input

    # Generate the maze
    maze, start_position, goal_position = generate_maze(maze_size, maze_size)

    # Create a window
    window = tk.Tk()
    window.title("Pathfinding Algorithm Visualization")

    # Create a canvas to display the maze
    canvas = Canvas(window, width=maze_size * 20, height=maze_size * 20)  # Adjust the size as needed
    canvas.pack()

    # Display the maze on the canvas
    visualize_pathfinding_algorithm(canvas, maze, start_position, goal_position, dijkstra)

    # Dropdown menu for selecting pathfinding algorithm
    algorithm_var = tk.StringVar()
    algorithm_var.set("Dijkstra")  # Default algorithm
    algorithm_menu = ttk.Combobox(window, textvariable=algorithm_var, values=["Dijkstra", "A*", "BFS", "DFS"])
    algorithm_menu.pack()

    def run_selected_algorithm():
        selected_algorithm = algorithm_var.get()
        if selected_algorithm == "Dijkstra":
            run_algorithm(dijkstra, maze, start_position, goal_position, canvas)
        elif selected_algorithm == "A*":
            run_algorithm(astar, maze, start_position, goal_position, canvas)
        elif selected_algorithm == "BFS":
            run_algorithm(bfs, maze, start_position, goal_position, canvas)
        elif selected_algorithm == "DFS":
            run_algorithm(dfs, maze, start_position, goal_position, canvas)            

    # Button to run the selected algorithm
    run_button = tk.Button(window, text="Run Algorithm", command=run_selected_algorithm)
    run_button.pack()

    # Run the GUI event loop
    window.mainloop()

if __name__ == "__main__":
    main()
