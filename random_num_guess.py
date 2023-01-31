import random 
import os
# guess= input("Guess the number")
# for i in range(1, 15):
#     if guess == i :
#         print('You Win')
#     else :
#         continue
os.system('cls')
MAX_LIMIT = 10
rounds = 10
n = 1 
# guess= input("Guess the number\n")

random_number = random.randint(0,MAX_LIMIT)

print("Random number guessing...")
print("You have 9 guesses in total")
while True :
    n += 1
    guess= input("Guess the number\n")
    if n >= rounds :
        break
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please enter a number")
    if guess != random_number :
        print(f'Retrying!!!\nTimes left: {rounds-n}')
        
    else :
        print("You Win")
        break

    