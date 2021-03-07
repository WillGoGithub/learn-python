print("Hello, Themyscira!")
# Associate the variable diana with the value "WONDER WOMAN 1984"
diana = "WONDER WOMAN 1984"

# Print a message with the true identity of Diana
print("I believe Diana is actually " + diana)

# Define a power (function) to chant a phrase


def chant(phrase):
    # Glue three copies together and print it as a message
    print(phrase * 3)


chant('WONDER WOMAN 1984! ')


def lassoLetter(letter, shiftAmount):
    letterCode = ord(letter.lower())
    aAscii = ord('a')
    alphabetSize = 26

    shiftedCode = aAscii + \
        (((letterCode - aAscii) + shiftAmount) % alphabetSize)
    decodedLetter = chr(shiftedCode)

    return decodedLetter


def lassoWord(word, shiftAmount):

    decodedWord = ''

    for letter in word:
        decodedLetter = lassoLetter(letter, shiftAmount)
        decodedWord = decodedWord + decodedLetter

    return decodedWord


print("Shifting WHY by 13 gives: \n" + lassoWord("WHY", 13))
print("Shifting oskza by -18 gives: \n" + lassoWord("oskza", -18))
print("Shifting ohupo by -1 gives: \n" + lassoWord("ohupo", -1))
print("Shifting ED by 25 gives: \n" + lassoWord("ED", 25))
