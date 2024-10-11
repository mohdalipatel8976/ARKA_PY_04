import tkinter as tk
from tkinter import messagebox
import random

def computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'Rock' and computer == 'Scissors') or \
         (user == 'Paper' and computer == 'Rock') or \
         (user == 'Scissors' and computer == 'Paper'):
        return "You win!"
    else:
        return "You lose!"

def play(choice):
    comp_choice = computer_choice()
    result = determine_winner(choice, comp_choice)
    result_label.config(text=f"You chose: {choice}\nComputer chose: {comp_choice}\n{result}")
    ask_replay()

def ask_replay():
    response = messagebox.askyesno("Play Again?", "Do you want to play again?")
    if response:
        replay_game()
    else:
        window.quit()

def replay_game():
    result_label.config(text="Choose Rock, Paper, or Scissors")

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x300")
window.resizable(False, False)

instruction_label = tk.Label(window, text="Choose Rock, Paper, or Scissors", font=('Helvetica', 14))
instruction_label.pack(pady=10)

result_label = tk.Label(window, text="", font=('Helvetica', 12))
result_label.pack(pady=10)

rock_button = tk.Button(window, text="Rock", width=12, height=2, command=lambda: play('Rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", width=12, height=2, command=lambda: play('Paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", width=12, height=2, command=lambda: play('Scissors'))
scissors_button.pack(pady=5)

window.mainloop()
