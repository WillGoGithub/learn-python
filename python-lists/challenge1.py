import random

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = ["2", "3", "4", "5", "6", "7", "8",
         "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')


def countTheDeck():
    print(f'There are {len(deck)} cards in the deck.')


countTheDeck()

print('Dealing ...')

random.shuffle(deck)

hand = []

for i in range(5):
    card = deck.pop()
    hand.append(card)

countTheDeck()

print('Player has the following cards in their hand:')
print(hand)
