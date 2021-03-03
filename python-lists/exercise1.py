colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

print(colors)
print(type(colors))

sundry = ['John', 3.14, 7, False]
print(sundry)
print(type(sundry))

emptyList = []

print(colors[0])
print(colors[1])
print(colors[-1])
print(colors[-2])

print('\nPrint a SLICE, starting at index 2 and excluding index 5:')
print(colors[2:5])
print(type(colors[2:5]))

print('\nPrint a slice, starting at index 0 to index 3:')
print(colors[0:3])

print('\nPrint a slice, starting a index 4 to the end of the list:')
print(colors[4:])

print('\nPrint a slice, from the 4th from the end (but not the last item):')
print(colors[-4:-1])

colors.reverse()
print(colors)

colors.sort()
print(colors)

color = colors.pop()
print(color, colors)

color = colors.pop(0)
print(color, colors)

colors.append('black')
colors.remove('red')
print(colors)

newColors = ['lime', 'grey']
colors.extend(newColors)
print(colors)

colors.clear()
print(colors)
