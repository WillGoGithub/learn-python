def sayHello(name='World', greeting=None):
    if greeting == None:
        print(f'Hello {name}!')
    else:
        print(f'{greeting} {name}!')


sayHello()
sayHello('Bob')
sayHello(greeting='Howdy')
sayHello('Bob', 'Howdy')

print(type(None))


def addTwoNumbers(x, y):
    return x + y


addTwoNumbers(4, 6)
result = addTwoNumbers(5, 7)
print(result)


def createDeck():
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    ranks = ["2", "3", "4", "5", "6", "7", "8",
             "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')

    return deck


myDeck = createDeck()
print(len(myDeck))


# 跟 JS 不同
value = 1


def some_function():
    value = 10
    return value


print(value)
some_function()
print(value)
