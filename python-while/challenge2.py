import random

minValue = 1
maxValue = 10
count = 0
guessNum = 0
answerNum = random.randint(minValue, maxValue)

print(f'Guess a number between {minValue} and {maxValue}:')

while guessNum != answerNum:
    count += 1
    guessNum = input(f'Enter guess #{count}: ')

    if guessNum.isnumeric() == False:
        print('Numbers only, please!')
        continue

    guessNum = int(guessNum)

    if guessNum < answerNum:
        print('Your guess is too low, try again!')
    elif guessNum > answerNum:
        print('Your guess is too high, try again!')

else:
    print(f'You guessed it in {count} tries!')
