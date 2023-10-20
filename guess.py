import random 
secret_number = random.randint(1,100)
guess_count = 0
guess_limit = 6
while guess_count < guess_limit:
    print(" ")
    guess = int((input("Guess a number between 1-100 ")))
    guess_count += 1
    if guess != secret_number:
        if guess_count == guess_limit:
            print(" ")
            print("You are an idiot. ")
            break
        elif guess < secret_number:
            print("Higher")
            print("Guesses remaining: " + str(guess_limit - guess_count))
        elif guess > secret_number:
            print("Lower")
            print("Guesses remaining: " + str(guess_limit - guess_count))
        else:
            print("Please input a number in the space provided. ")
    elif guess == secret_number:
        print(" ")
        print("You win!")
        break