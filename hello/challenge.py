print("Today's date?")
date = input()

print("Breakfast calories?")
breakfast_calories = int(input())

print("Lunch calories?")
lunch_calories = int(input())

print("Dinner calories?")
dinner_calories = int(input())

print("Snack calories?")
snack_calories = int(input())

sumCalories = breakfast_calories + \
    lunch_calories + dinner_calories + snack_calories

print("Calorie content for " + date + ": " + str(sumCalories))
