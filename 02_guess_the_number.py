import random

print('-' * 18)
print('   GUESS THE NUMBER')
print('-' * 18)

secret_number = random.randint(1, 10)


while user_guess != secret_number:
    user_guess = int(input(f"I'm thinking of a number between 1 and 10. Can you guess it? "))
    if user_guess < secret_number:
        print(f"Sorry, {user_guess} is too low.")
    elif user_guess > secret_number:
        print(f"Sorry, {user_guess} is too high.")
    else:
        print(f"Great guess! {user_guess} is right on the money!")