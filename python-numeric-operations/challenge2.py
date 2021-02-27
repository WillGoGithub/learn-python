print('Simple calculator!')
firstNumber = input('First number? ')
operation = input('Operation? ')
secondNumber = input('Second number? ')

if (not firstNumber.isnumeric() or
        not secondNumber.isnumeric()):
    print('Please input a number.')
    exit()

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

if operation == '+':
    result = firstNumber + secondNumber
    label = 'sum'
elif operation == '-':
    result = firstNumber - secondNumber
    label = 'difference'
elif operation == '*':
    result = firstNumber * secondNumber
    label = 'product'
elif operation == '/':
    result = firstNumber / secondNumber
    label = 'quotient'
elif operation == '%':
    result = firstNumber % secondNumber
    label = 'modulus'
elif operation == '**':
    result = firstNumber ** secondNumber
    label = 'exponent'
else:
    print('Operation not recognized.')
    exit()

print(f'{label} of {firstNumber} {operation} {secondNumber} equals {result}')
