import random
print("welcome to rock paper scisssors\n\n")
print("r is for rock\np is for paper\ns is for scissors")
choices = ['r', 'p', 's']
computer_choice = random.choice(choices)
human_choice= input("enter your letter: ")
print(f"the computer chose: {computer_choice}")

# logic

if computer_choice=='r' and human_choice=='r':
    print("the game is tied motherfuckuhh!")
elif computer_choice=='s' and human_choice=='s':
    print("the game is tied motherfuckuhh!")
elif computer_choice=='p' and human_choice=='p':
    print("the game is tied motherfuckuhh!")
elif computer_choice=='r' and human_choice=='p':
    print("you got lucky!")
elif computer_choice=='r' and human_choice=='s':
    print("computer is smarter than you dumbfuck!")
elif computer_choice=='p' and human_choice=='r':
    print("computer is smarter than you dumbfuck!")
elif computer_choice=='p' and human_choice=='s':
    print("you got lucky!")
elif computer_choice=='s' and human_choice=='r':
    print("you got lucky!")
elif computer_choice=='s' and human_choice=='p':
    print("computer is smarter than you dumbfuck!")
