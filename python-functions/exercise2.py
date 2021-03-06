# Array
# Arbitrary arguments lists
def printArgs(*args):
    print(args, type(args))
    for arg in args:
        print(f'arg = {arg}')


printArgs('a')
printArgs('a', 'b')
printArgs('a', 'b', 'c')

# Object
# Keyword arguments aka. Named arguments


def printKeywordArgs(**kwargs):
    print('\n')
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f'{key} = {value}')

    third = kwargs.get('third', None)

    if third != None:
        print(f'third arg = {third}')


printKeywordArgs(first='a')
printKeywordArgs(first='a', second='c')
printKeywordArgs(first='a', second='c', third='f')
