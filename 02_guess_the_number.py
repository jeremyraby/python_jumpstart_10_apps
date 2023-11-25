import random

print('-' * 15)
print('   GUESS THE NUMBER')
print('-' * 15)

user_guess = int(input(f"I'm thinking of a number between 1 and 10. Can you guess it? "))

number_choices = [1,2,3,4,5,6,7,8,9,10]
secret_number = random.choice(number_choices)

while user_guess != secret_number:
    if user_guess < secret_number:
        print(f"Sorry, {user_guess} is too low. Try again.")
    elif user_guess > secret_number:
        print(f"Sorry, {user_guess} is too high. Try again.")
    else:
        print(f"Great guess! {user_guess} is right on the money!")