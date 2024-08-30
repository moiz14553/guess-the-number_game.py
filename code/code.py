import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0
    guessed_correctly = False

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed_correctly:
        try:
            # Prompt the user to guess the number
            user_guess = int(input("Enter your guess: "))
            number_of_guesses += 1

            if user_guess < number_to_guess:
                print("Higher number please.")
            elif user_guess > number_to_guess:
                print("Lower number please.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number in {number_of_guesses} guesses.")
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()
