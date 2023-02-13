from random import randint

min_num = 1
max_num = 100
answer = randint(min_num, max_num)

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def difficulty():
  difficulty = input("Choose a difficulty. Type 'e' for easy or 'h' for hard. ")
  if difficulty == "e":
    return EASY_ATTEMPTS
  else:
    return HARD_ATTEMPTS

def check_answer(guess, answer, turns):
  """Checks answer against guess.  Returns the number of turns remaining."""
  if guess == answer:
    print(f"You got it.  The answer was {answer}.")
  elif guess > answer:
    print("Too high.  Guess Again.")
    return turns -1
  else:
    print("Too low.  Guess again.")
    return turns -1

def game():
  print(answer)
  print("Welcome to Number Guessing Game!")
  print(f"I'm thinking of a number between {min_num} and {max_num}.")
  turns = difficulty()
  guess = 0
  while guess != answer:
    print(f"Your have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess. "))
    turns = check_answer(guess, answer, turns) 
    if turns == 0:
      print("You've run out of guesses.  You lose.")
      return
    elif guess != answer:
      print("Guess again.")
game()