import random

# 1. We define a function called rock_paper_scissors.
# 2. We print out a message to the user.
# 3. We define a variable called rock, paper, and scissors.
# 4. We ask the user to enter a choice.
# 5. We define a variable called user and assign it to the user’s choice.
# 6. We define a variable called computer and assign it to a random choice from the tuple all_choices.
# 7. We print out the user’s choice and the computer’s choice.
# 8. We check if the user’s choice and the computer’s choice are the same.
# 9. If they are, we print out TIE!.
# 10. If the user’s choice is rock and the computer’s choice is scissors, or the user’s choice is scissors and the computer’s choice is paper, or the user’s choice is paper and the computer’s choice is rock, we print out YOU WIN!!!
# 11. Otherwise, we print out YOU LOSE!!!
# 12. We return from the function.


# Time Complexity: O(1)


# The code is a game that asks the user to enter either rock, paper, or scissors.
# If the user enters anything other than rock, paper, or scissors, the program prints "Choice not valid" and then asks the user to enter a choice again.
# The program then randomly chooses rock, paper, or scissors.
# The program then prints the user's choice and the computer's choice.
# If the user and the computer make the same choice, the program prints "TIE!"
# If the user wins, the program prints "YOU WIN!!!"
# If the user
# 
# Args:
#   None
# Returns:
#   Nothing is being returned.


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