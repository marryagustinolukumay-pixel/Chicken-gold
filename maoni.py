import tkinter as tk
import random
import time
import math

root = tk.Tk()
root.title("Chicken Gold: Crash")
root.geometry("400x600")
root.configure(bg="#1a1a2e")

canvas = tk.Canvas(root, width=400, height=500, bg="#16213e", highlightthickness=0)
canvas.pack()

# Vitu vya mchezo
multiplier = 1.00
crash_point = random.uniform(1.20, 10.00)
game_running = False
bet_amount = 10
balance = 100
cashed_out = False

# Chora kuku
chicken = canvas.create_oval(180, 450, 220, 490, fill="#ffd700", outline="#ffaa00", width=3)
eye = canvas.create_oval(195, 465, 205, 475, fill="red")

# Maandishi
mult_text = canvas.create_text(200, 100, text="1.00x", fill="#00ff00", font=("Arial", 48, "bold"))
balance_text = canvas.create_text(200, 30, text=f"Balance: ${balance}", fill="white", font=("Arial", 16))
crash_text = canvas.create_text(200, 480, text="", fill="red", font=("Arial", 24, "bold"))

# Kazi za vitufe
def start_game():
    global multiplier, crash_point, game_running, cashed_out
    if balance < bet_amount:
        return
    multiplier = 1.00
    crash_point = random.uniform(1.20, 10.00)
    game_running = True
    cashed_out = False
    canvas.itemconfig(crash_text, text="")
    update_balance(-bet_amount)
    update_multiplier()

def cash_out():
    global game_running, cashed_out
    if game_running and not cashed_out:
        cashed_out = True
        game_running = False
        win = bet_amount * multiplier
        update_balance(win)
        canvas.itemconfig(crash_text, text=f"CASHED OUT! ${win:.2f}", fill="#00ff00")

def update_multiplier():
    global multiplier, game_running
    if not game_running