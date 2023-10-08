import tkinter as tk
from tkinter import ttk
import subprocess
import os

# Function to launch the selected game
def launch_game(choice):
    if choice == 1:
        subprocess.run(["python", "ticrunner.py"])
    elif choice == 2:
        subprocess.run(["python", "minesweeperrunner.py"])
    elif choice == 3:
        subprocess.run(["python", "nimrunner.py"])
    else:
        status_label.config(text="Invalid choice!")

# Check for dependencies
def check_dependencies():
    try:
        subprocess.run(["python", "-m", "pip", "show", "pygame"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Create the main window
root = tk.Tk()
root.title("AI Arena Game Launcher")
root.geometry("600x400")  # Set the window size

# Style configuration
style = ttk.Style()
style.configure("TButton", padding=(10, 5), font=("Helvetica", 12), width=60)
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TFrame", relief="groove")
style.configure("Game.TButton", width=20, relief="flat", background="white")  # Fix the width and remove the button relief

# Add a custom style for the selected button
style.map("Game.TButton", background=[("selected", "red")], foreground=[("selected", "black")])

# Check dependencies
if not check_dependencies():
    status_label = ttk.Label(root, text="Pygame not installed. Please install it and relaunch the app.")
    status_label.pack(pady=20)
    root.mainloop()
    exit()

# Welcome message
welcome_label = ttk.Label(root, text="Welcome to The AI Arena!!!")
welcome_label.pack(pady=20)

# Game selection label
game_label = ttk.Label(root, text="Select a game to play:")
game_label.pack()

# Create a variable for the selected game
selected_game = tk.IntVar()
selected_game.set(1)  # Default choice

# Function to update the selected game
def update_selected_game(value):
    selected_game.set(value)

# Selectable buttons for game selection
choices = [("Tic Tac Toe", 1), ("Minesweeper", 2), ("NIM", 3)]

for text, value in choices:
    radio_button = ttk.Radiobutton(root, text=text, variable=selected_game, value=value, command=lambda value=value: update_selected_game(value))
    radio_button.configure(style="Game.TButton")  # Apply a custom style
    radio_button.pack(pady=10, padx=20, fill=tk.X)

# Play button
play_button = ttk.Button(root, text="Play", command=lambda: launch_game(selected_game.get()))
play_button.configure(style="Game.TButton")  # Apply the custom style
play_button.pack(pady=20)

# Status label
status_label = ttk.Label(root, text="")
status_label.pack()

# Start the GUI main loop
root.mainloop()
