import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Function to display the maze
def load_maze(maze_file):
    with open(maze_file, 'r') as file:
        maze_data = file.readlines()
    
    # Clear the canvas first
    canvas.delete("all")
    
    # Create a text-based representation of the maze
    for y, line in enumerate(maze_data):
        for x, char in enumerate(line):
            color = "white"
            if char == '#':
                color = "black"
            elif char == 'A':
                color = "green"
            elif char == 'B':
                color = "red"
            canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill=color, outline="gray")

# Function to select the maze file
def select_maze():
    maze_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if maze_file:
        load_maze(maze_file)
    else:
        messagebox.showerror("Error", "No maze file selected.")

# Initialize the main window
root = tk.Tk()
root.title("Maze Solver")
root.geometry("600x400")

# Create a frame for the radio buttons
frame = tk.Frame(root)
frame.pack(side=tk.LEFT, padx=20)

# Add radio buttons to select the algorithm
algorithm_var = tk.StringVar(value="BFS")
algorithms = ["BFS", "DFS", "Heuristic Search", "Optimal Path"]
for alg in algorithms:
    tk.Radiobutton(frame, text=alg, variable=algorithm_var, value=alg).pack(anchor=tk.W)

# Add a button to load the maze
select_button = tk.Button(frame, text="Select Maze", command=select_maze)
select_button.pack(pady=10)

# Create a canvas to draw the maze
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(side=tk.RIGHT)

root.mainloop()
