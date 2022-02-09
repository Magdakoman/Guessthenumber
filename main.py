#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
print("Welcome to the: ")
print(logo)
print("Im thinking of a number between 1 to 100")
difficulty = input("Choose a difficulty.Type 'easy' or 'hard': ")
attempts = 10
game_end = False
numbers = [number for number in range(1, 101)]
number = int(random.choice(numbers))
print(f"Psst the correct answer is {number}")
guess = int(input("Make a guess: "))


if difficulty == "easy":
  attempts = 10
elif difficulty == "hard":
  attempts -= 5
else:
  print("Invalid entry")


while attempts > 0 and game_end == False:
  if guess == number:
    print(f"You got it! The answer is {number}.")
    game_end = True
    
  elif guess > number:
    attempts -= 1
    print("Too high")
    if attempts > 0:
      print("Guess again")
      print(f"You have {attempts} attempts remaining to guess the number")
      guess = int(input("Make a guess: "))
    else:
        print("You lose. Game over")
        break
  elif guess < number:
    print("Too low")
    attempts -= 1 
    if attempts > 0:
      print("Guess again")
      print(f"You have {attempts} attempts remaining to guess the number")
      guess = int(input("Make a guess: "))
    else:
      print("You lose. Game over")
      break

