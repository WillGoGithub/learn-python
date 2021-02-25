# Uppercase first character in a string
message = str.capitalize('first message')
print(message)

message = 'second message'.capitalize()
print(message)

message = 'third message'
print(message.capitalize())

message = 'hello world'
print(message.lower())
print(message.upper())
print(message.title())
print(message.swapcase(), end='\n\n')

print(f'count o in {message}: is {message.count("o")}')
print(len('How many letters in this string?'))

message = 'racecar'
print(
    message.startswith('r'),
    message.startswith('a'),
    message.startswith('ra'),

    message.endswith('r'),
    message.endswith('a'),
    message.endswith('ar'),
    sep=', '
)

message = 'The quick brown fox jumps over the lazy dog'
print(
    message.find('q'),
    message.find('t'),
    message.find('T')
)

message = '   trim test    '
print(
    message.lstrip(),
    message.rstrip(),
    message.strip(),
    sep='.\n',
    end='.\n\n'
)

message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)

message = 'howdy'
print(
    message.rjust(20),
    message.rjust(20, '-'),
    message.ljust(20),
    message.ljust(20, '-'),
    sep='\n',
    end='\n\n'
)
