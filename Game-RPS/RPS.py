# Importing the Python library for random number generating
import random

# The main function of the game we use here. 
# To simplify ease of use, Instead of having the user write out the whole word 
# (potentially resulting) in errors, instead we have them use the shortened version (ex: 'p')
def play():
    user = input("Instructions on how to play: Press 'r' for rock 'p' for paper and 's' for scissors ")
    computer = random.choice(['r','p','s'])


    # Everything below here is within the function play(), meaning that the scenarios will run in order 
    # First scenario is a tie (meaning both the user's choice and the number generated by the computer will be the same)
    if user == computer:
            return 'tie'
   
   # The second scenario is that the user won [in which case the whole program will stop]
    if is_win(user, computer):
      return 'You won!'
    
    # If none of the previous scenarios apply, the program will stop 
    return 'You lost!'

   # Here are the rules of the game to help write out the next function:
    # r > s, s > p, p > r

    # And here's the function to determine who wins. There's only 3 scenarios in which the player wins
def is_win (player, opponent):
      if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
           return True
     

print (play())