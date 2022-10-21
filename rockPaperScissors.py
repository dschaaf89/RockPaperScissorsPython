import random

def rock_paper_scissors():
    print("Time to Play Rock Paper Scissors \n")
    
    
    rock = "rock"
    paper = "paper"
    scissors ="scissors"
    all_choices = (rock,paper,scissors)
    
    user = input(f"enter a choice ({rock}, {paper},{scissors}):")
    
    if user not in all_choices:
      print("\Choice not valid:\n")
      return
    
    computer = random.choice(all_choices)
    print(f"you chose{user}, Computer chose{computer}.")
    
    
    if user == computer:
      print ("TIE! \n")
      
    elif(
      (user == rock and computer == scissors)
      or (user == scissors and computer == paper)
      or (user == paper and computer == rock)
      
    ):
      print ("YOU WIN !!!")
    else: 
      print("YOU LOSE!!!")