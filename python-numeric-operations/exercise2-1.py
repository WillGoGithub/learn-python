numeric_value = '7'
print(numeric_value.isnumeric())

string_value = 'Bob'
print(string_value.isnumeric())


is_alnum = 'HasNoSpecialCharacters10'
is_not_alnum = 'Has no special characters, such as %, $, #, @, or !.'
print(
    is_alnum.isalnum(),
    is_not_alnum.isalnum()
)

is_alpha = 'ContainsOnlyLettersOfTheAlphabet'
is_not_alpha = 'Contains only letters of the alphabet.10'
print(
    is_alpha.isalpha(),
    is_not_alpha.isalpha()
)

is_decimal = '1234567890'
is_not_decimal = '123456.123'
print(
    is_decimal.isdecimal(),
    is_not_decimal.isdecimal()
)

is_title = 'Follows The Rules Of Capitalization'
is_not_title = "not follows"
print(
    is_title.istitle(),
    is_not_title.istitle()
)

is_upper = "ONLY UPPERCASE LETTERS."
is_lower = "only lowercase letters."
print(
    is_upper.isupper(),
    is_lower.islower()
)
