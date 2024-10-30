import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I've selected a random number between 1 and 100.")
    print("You have 10 attempts to guess it.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        print("\nAttempts left:", attempts)
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You've guessed the correct number:", secret_number)
            break
        elif guess < secret_number:
            print("Try again! The secret number is higher.")
        else:
            print("Try again! The secret number is lower.")

        attempts -= 1

    if attempts == 0:
        print("\nSorry, you've run out of attempts! The secret number was:", secret_number)

# Run the game
guessing_game()
