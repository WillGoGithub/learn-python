# Raw string
raw_string = r'A literal string with a \n new line character printed raw'
print(raw_string)

# Multi-line
multi_line_string = '''A literal string
on more than one line
sometimes known as a verbatim string.

    tab test
'''
print(multi_line_string)

# Concatenate strings
first = 'Conrad'
second = 'Grant'
third = 'Bob'

print(first, second, third)
print(first, second, third, sep='-')
print(first, second, third, sep='-', end='.')
