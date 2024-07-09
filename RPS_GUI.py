from tkinter import *
import random

root = Tk()
root.geometry("300x200")
root.title("Rock-Paper-Scissors Game")

def play(user_choice):
    computer_choices = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(computer_choices)

    if user_choice == computer_choice:
        result = "It's a draw!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissor")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissor" and computer_choice == "Paper")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"
        
    result_label.config(text=result)
rock_button = Button(root, text="Rock", command=lambda: play("Rock"))
paper_button = Button(root, text="Paper", command=lambda: play("Paper"))
scissor_button = Button(root, text="Scissor", command=lambda: play("Scissor"))
result_label = Label(root, text="")
rock_button.pack()
paper_button.pack()
scissor_button.pack()
result_label.pack()
root.mainloop()