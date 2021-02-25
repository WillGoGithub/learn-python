medicine = 'Coughussin'
dosage = 5
duration = 4.5

instructions = f'{medicine} - Take {dosage} ML by mouth every {duration} hours.'
print(instructions)

width = 5
height = 10

print(
    f'The perimeter is {(2 * width) + (2 * height)} and the area is {width * height}.')

value = 'hi'
print(
    f'.{value:<25}.',
    f'.{value:>25}.',
    f'.{value:^25}.',
    f'.{value:=^25}.',
    sep='\n',
    end='\n\n'
)

# https://docs.python.org/3/library/string.html#formatspec?azure-portal=true
