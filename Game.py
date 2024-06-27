import tkinter as tk
from tkinter import messagebox
import random

# Main application class
class RockPaperScissorsApp:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Rock, Paper, Scissors Game")

        # Initialize scores
        self.player_score = 0
        self.cpu_score = 0

        # Create widgets
        self.setup_widgets()

    def setup_widgets(self):
        # Instructions label
        self.label_instructions = tk.Label(self.main_window, text="Choose Rock, Paper, or Scissors:")
        self.label_instructions.pack()

        # Buttons for user choices
        self.button_rock = tk.Button(self.main_window, text="Rock", command=lambda: self.play_round("rock"))
        self.button_rock.pack(side=tk.LEFT, padx=10)

        self.button_paper = tk.Button(self.main_window, text="Paper", command=lambda: self.play_round("paper"))
        self.button_paper.pack(side=tk.LEFT, padx=10)

        self.button_scissors = tk.Button(self.main_window, text="Scissors", command=lambda: self.play_round("scissors"))
        self.button_scissors.pack(side=tk.LEFT, padx=10)

        # Labels to display choices and results
        self.label_result = tk.Label(self.main_window, text="")
        self.label_result.pack()

        self.label_score = tk.Label(self.main_window, text=f"User: {self.player_score}  Computer: {self.cpu_score}")
        self.label_score.pack()

    def play_round(self, player_choice):
        # Computer makes a random choice
        cpu_choice = random.choice(["rock", "paper", "scissors"])
        result = self.determine_winner(player_choice, cpu_choice)
        self.update_scores(result)
        self.display_results(player_choice, cpu_choice, result)

    def determine_winner(self, player_choice, cpu_choice):
        # Determine the winner
        if player_choice == cpu_choice:
            return "tie"
        elif (player_choice == "rock" and cpu_choice == "scissors") or \
             (player_choice == "paper" and cpu_choice == "rock") or \
             (player_choice == "scissors" and cpu_choice == "paper"):
            return "player"
        else:
            return "computer"

    def update_scores(self, result):
        # Update scores based on the result
        if result == "player":
            self.player_score += 1
        elif result == "computer":
            self.cpu_score += 1

    def display_results(self, player_choice, cpu_choice, result):
        # Display the result and choices
        if result == "tie":
            result_text = "It's a tie!"
        elif result == "player":
            result_text = "You win!"
        else:
            result_text = "Computer wins!"

        self.label_result.config(text=f"You chose {player_choice}, computer chose {cpu_choice}. {result_text}")
        self.label_score.config(text=f"User: {self.player_score}  Computer: {self.cpu_score}")
        self.ask_play_again()

    def ask_play_again(self):
        # Ask if the player wants to play again
        if messagebox.askyesno("Play Again?", "Do you want to play another round?"):
            self.label_result.config(text="")
        else:
            self.main_window.quit()

# Create the main window
main_window = tk.Tk()
app = RockPaperScissorsApp(main_window)

# Run the main loop
main_window.mainloop()
