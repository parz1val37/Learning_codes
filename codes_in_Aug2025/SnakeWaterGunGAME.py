# Snake Water Gun Game
import random

g = {1: 'Snake', 2: 'Water', 3: 'Gun'}

print('To choose Snake enter: 1\nTo choose Water enter: 2\nTo choose Gun enter: 3')
n = int(input('Enter your choice: '))
print(f'Yours choice: {g[n]}')
computer = random.randint(1, 3)
print(f'Computers choice: {g[computer]}')

if n == computer:
    print('It\'s a tie!')
elif (n == 1 and computer == 3) or (n == 2 and computer == 1) or (n == 3 and computer == 2):
    print('You lose!\nBetter luck next time!')  
else:
    print('You won!\nHurray!')
