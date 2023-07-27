import tkinter as tk
import random

# Global variables
flip_count = 0
heads_count = 0
tails_count = 0

# Function to flip the coin and update the result
def flip_coin():
    global flip_count, heads_count, tails_count
    
    result = random.choice(["Heads", "Tails"])
    flip_count += 1
    
    if result == "Heads":
        heads_count += 1
    else:
        tails_count += 1
    
    result_label.config(text="Result: " + result)
    stats_label.config(text=f"Flips: {flip_count}  Heads: {heads_count}  Tails: {tails_count}")

# Create the main window
window = tk.Tk()
window.title("Heads or Tails")

# Create the GUI elements
flip_label = tk.Label(window, text="Press Enter to flip the coin")
flip_label.pack()

result_label = tk.Label(window, text="Result: ")
result_label.pack()

stats_label = tk.Label(window, text="Flips: 0  Heads: 0  Tails: 0")
stats_label.pack()

# Function to handle keypress events
def on_keypress(event):
    if event.keysym == 'Return':
        flip_coin()

# Bind keypress event to the window
window.bind("<Key>", on_keypress)

# Start the main event loop
window.mainloop()
