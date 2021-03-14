# TODO 還沒完成
# create some variables for scoring
# diana, steve, max, barbara
likes = [0, 0, 0, 0]

questions = {
    1: "How would you like to spend your evening?\n(A) Reading a book\n(B) Attending a party\n",
    2: "What's your dream job?\n(A) Curator at the Smithsonian\n(B) Running a business\n",
    3: "What's more important?\n(A) Money\n(B) Love\n",
    4: "What's your favorite decade?\n(A) 1910s\n(B) 1980s\n",
    5: "What's your favorite way to travel?\n(A) Driving\n(B) Flying\n",
}

answers = {
    "1A": "Reading a book, Nice choice!",
    "1B": "Attending a party? Sounds fun!",
    "2A": "Curator, Nice choice!",
    "2B": "Running a business? Sounds fun!",
    "3A": "Money, Nice choice!",
    "3B": "Love? Sounds fun!",
    "4A": "1910s, Nice choice!",
    "4B": "1980s? Sounds fun!",
    "5A": "Driving, Nice choice!",
    "5B": "Flying? Sound fun!",
}

scores = {
    "1A": [1, 0, 0, 1],
    "1B": [0, 1, 1, 0],
    "2A": [2, -1, 0, 2],
    "2B": [0, 0, 2, 0],
    "3A": [-1, 0, 2, 0],
    "3B": [1, 2, 0, 1],
    "4A": [1, 2, 0, 0],
    "4B": [0, 0, 1, 2],
    "5A": [0, 0, 2, -1],
    "5B": [1, 1, 0, 0],
}

user_selected = []


def add_score(step_answer, likes):
    score_table = scores[step_answer]
    for i in range(0, 3):
        likes[i] += score_table[i]
    return likes


# ask the candidate a question
step = 1
while step <= 5:
    user_answer = input(questions[step])
    user_answer = user_answer.upper()

    step_answer = f"{step}{user_answer}"
    show_answer = answers.get(step_answer, None)

    if show_answer == None:
        print("You must type A or B:")
    else:
        print(show_answer)
        user_selected.append(show_answer)
        likes = add_score(step_answer, likes)
        step += 1

# print out their choices
print(
    f"You chose {user_selected[0]}, then {user_selected[1]}, then {user_selected[2]}, then {user_selected[3]}, then {user_selected[4]}.")

# print the results depending on the score
if likes[0] >= 6:
    print("You're most like Wonder Woman!")
elif likes[1] >= 6:
    print("You're most like Steve Trevor!")
elif likes[2] >= 6:
    print("You're most like Barbara Minerva!")
else:
    print("You're most like Max Lord!")
