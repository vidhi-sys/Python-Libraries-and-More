import random

def number_guessing_game():
    """
    A simple number guessing game in Python.
    The user tries to guess a randomly generated number.
    """
    # Generate a random number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    # Loop until the user guesses the correct number
    while guess != secret_number:
        try:
            # Get user input and convert it to an integer
            guess_input = input("Enter your guess: ")
            guess = int(guess_input)
            attempts += 1

            # Provide feedback on the guess
            if guess < secret_number:
                print("Too low, try a higher number.\n")
            elif guess > secret_number:
                print("Too high, try a lower number.\n")
        except ValueError:
            # Handle cases where the user enters non-integer input
            print("Invalid input. Please enter a valid integer number.")

    # This code executes once the while loop breaks (i.e., the guess is correct)
    print(f"Congratulations! You guessed the number {secret_number} correctly!")
    print(f"It took you {attempts} attempts.")

def computer_guesses_number():
    """
    A game where the computer tries to guess your number.
    The user thinks of a number and the computer guesses it.
    """
    print("\n" + "="*50)
    print("Welcome to Computer Guessing Game!")
    print("Think of a number between 1 and 100.")
    print("I will try to guess it!")
    print("="*50)
    
    low = 1
    high = 100
    feedback = ''
    attempts = 0
    
    while feedback != 'c':
        if low > high:
            print("Hmm, something doesn't add up. Let's start over.")
            low, high = 1, 100
            attempts = 0
        
        # Computer makes a guess
        guess = random.randint(low, high)
        attempts += 1
        
        # Get feedback from user
        feedback = input(f"\nMy guess {attempts}: Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        # Process feedback
        if feedback == 'h':
            high = guess - 1
            print("I'll guess lower next time!")
        elif feedback == 'l':
            low = guess + 1
            print("I'll guess higher next time!")
        elif feedback == 'c':
            print(f"\n🎉 Yay! I guessed your number {guess} in {attempts} attempts!")
        else:
            print("Please enter H, L, or C only.")
            attempts -= 1  # Don't count invalid feedback as an attempt

def main_menu():
    """
    Main menu to choose which game to play.
    """
    while True:
        print("\n" + "="*50)
        print("NUMBER GUESSING GAMES")
        print("="*50)
        print("1. You guess the computer's number")
        print("2. Computer guesses your number")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            computer_guesses_number()
        elif choice == '3':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
