import random

roll = 0
count = 0

while roll != 5:
    name = input('Enter a name, or \'q\' to quit: ')
    name = name.strip()

    if name == '':
        continue

    if name == 'q':
        break

    count += 1
    roll = random.randint(1, 6)
    print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins!!!')

print(f'You rolled the dice {count} times.')
