import random
import os 
def gamble():
    question = random.randint(0,1)
    os.system('clear')
    guess = input("Heads(h) or Tails(t)? ")
    if question == 1:
        print(" ")
        print("Heads")
        if guess == "h":
            print(" ")
            print("You win!")
            gamba = input("Would you like to gamble it? (y/n): ")
            if gamba == "y": 
                gamble()
            if gamba == "n":
                print("alright then.")
        if guess == "t":
            print(" ")
            print("You lose!")
    if question == 0:
        print(" ")
        print("Tails")
        if guess == "t":
            print(" ")
            print("You win!")
            gamba = input("Would you like to gamble it? (y/n): ")
            if gamba == "y": 
                gamble()
            if gamba == "n":
                print("alright then.")
        if guess == "h":
            print(" ")
            print("You lose!")
gamble()
