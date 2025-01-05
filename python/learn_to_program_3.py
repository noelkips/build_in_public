
# Learn to program 2 tutorial
# Author: Noel Langat
# 100days of code day - 5

# Guess Game, user is allowed to make a maximu of 3 trials

secret_number = 5
maximum_trials = 3

while maximum_trials:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("Please Enter a number only")
    except:
        print("Un expected error occured")
    if guess == secret_number:
          print("You guess it ")
          break
    else:
         maximum_trials -= 1
         print(f"Make a guess again, you remain with {maximum_trials} trials")
         continue
      