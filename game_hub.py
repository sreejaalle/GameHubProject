import tkinter as tk
import subprocess

# Functions to launch each game
def launch_tic_tac_toe():
    subprocess.Popen(["python", "tic_tac_toe.py"])

def launch_rock_paper_scissors():
    subprocess.Popen(["python", "rock_paper_scissors.py"])

def launch_guess_the_number():
    subprocess.Popen(["python", "guess_the_number.py"])

# Main Game Hub Window
root = tk.Tk()
root.title("Game Hub")
root.geometry("400x250")
root.configure(bg="lightblue")

# Title Label
tk.Label(root, text="Game Hub", font=("Arial", 20), bg="lightblue").pack(pady=10)

# Buttons to launch each game
tk.Button(root, text="Tic-Tac-Toe", command=launch_tic_tac_toe, width=20, height=2).pack(pady=10)
tk.Button(root, text="Rock-Paper-Scissors", command=launch_rock_paper_scissors, width=20, height=2).pack(pady=10)
tk.Button(root, text="Guess the Number", command=launch_guess_the_number, width=20, height=2).pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
