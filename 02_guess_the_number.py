import random

print('-' * 15)
print('   GUESS THE NUMBER')
print('-' * 15)

secret_num = [1,2,3,4,5,6,7,8,9,10]

message = f"I'm thinking of a number between 1 and 10. Can you guess it? "
print(input(message))

if message > random.choice(secret_num):
    print("Sorry. That's too low.")