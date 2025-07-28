import random # gets the random function

def generate_random_number():  #generates a random number
    number = random.randint(1,100)
    return number

def get_user_guess():
    while True:
        try:
            guess = int(input("Guess a number from 1 to 100: ")) # asks for a number from 1 - 100
            if 1 <= guess <= 100: #checks if number is within 1 - 100
                return guess
            else:
                print("invalid input, enter valid input") # if number is not 1 - 100, print this
        except:
            print("Invalid input")


def play_guessing_game():
    secret_number = int(generate_random_number()) # sets the secret number as the number we generated before
    attempts = 0

    while True:
        user_guess = int(get_user_guess()) #sets the variable user_guess as the guess entered earlier
        attempts += 1
        
        if user_guess == secret_number: # checks if guess is the secret number
            print(f"Number guessed: {user_guess}")
            print("Correct Number")
            print(f"attempts needed: {attempts}\n")
            break
        elif user_guess < secret_number: # checks if the guess is lower than the secret number
            print(f"Number guessed: {user_guess}")
            print(f"current attempts: {attempts}")
            print("Too low\n")
        else: # checks if the guess is higher than the secret number
            print(f"Number guessed: {user_guess}")
            print(f"current attempts: {attempts}")
            print("Too High\n")


def game_loop():
    while True:
        play_guessing_game()

if __name__ == "__main__":  # run the game
    game_loop()
