import random

count = 0
answerNum = random.randint(1, 5)
guessNum = 0

while guessNum != answerNum:
    count += 1
    guessNum = input(f'Guess a number between 1 and 5: ')

    if guessNum.isnumeric():
        guessNum = int(guessNum)
else:
    print(f'You guessed it in {count} tries!')
