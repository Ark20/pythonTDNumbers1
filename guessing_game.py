"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
  print("""
  Welcome to the Number Guessing Game
  """)
  guesses = 0 
  guess = ""
  randomNum = random.randrange(10)

  while(guess != randomNum):
    guesses +=1
    
    try: 
      guess = int(input("Pick a number between one and 10 "))
    except ValueError:
      print("Make sure to provide a number as an answer")
    if guess not in range(0,11):
      print("Sorry that guess is not in the correct range.")
      continue
    if guess > randomNum:
      print("Your guess was a little too high")
      continue
    if guess < randomNum: 
      print("Your guess was a little too low")
      continue
    print("Great work guessing! It took you {} guesses. Would you like to play again? ".format(guesses))

start_game()