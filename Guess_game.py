#Guessing game
import os

os.system('cls')
print('Guessing Game but Among SuS')
print('Do you want to play!!!')

Player = input("Type 'Yes' for start the game 'No' for Quit\n")

if Player == 'Yes' or 'yes':
    print('Among Sus')

else :
    quit()

print('And the First Question is')
# Question1
Question = input('What is CPU stands for\n')
Answer = ['Central Processing Unit','central processing unit']
if Question in Answer :
    print('Correct!!! You are straight')
else:
    print('You are gay')
    quit()
# Question2
Question = input('What is the best hentai\n')
Answer = ['overflow','boku no pico']
if Question.lower() in Answer :
    print('Correct!!! You are straight')
else:
    print('You are gay')
    quit()
# Question3
Question = input('What is the best copulation position\n')
Answer = ['doggystyle','69']
if Question.lower() in Answer :
    print('Correct!!! You are straight')
else:
    print('You are gay')
    quit()
# Question4
Question = input('What is the best harem anime\n')
Answer = ['high school dxd']
if Question.lower() in Answer :
    print('Correct!!! You are straight')
else:
    print('You are gay')
    quit()
# Question5
Question = input('What is \n')
Answer = ['Central Processing Unit','central processing unit']
if Question.isalpha() :
    print('Correct!!! You are straight')
else:
    print('You are gay')
    quit()

