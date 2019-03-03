# Enter wall height (feet):
# 12
# Enter wall width (feet):
# 15
# Wall area: 180 square feet
# Paint needed: 0.514286 gallons
# Cans needed: 1 can(s)

# Choose a color to paint the wall:
# red
# Cost of purchasing red paint:
# $35




import math

# Dictionary of paint colors and cost per gallon
paintColors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wallH = float(input('Enter wall height (feet):\n'))
wallW = float(input('Enter wall width (feet):\n'))
wallSqr = int(wallH * wallW)
print('Wall area:', wallSqr, 'square feet')
   
# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
galCover = 350
neededPaint = wallSqr / galCover
print('Paint needed: %f' %neededPaint, 'gallons' )


# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
numOfCan = math.ceil(neededPaint)
print('Cans needed:', numOfCan, 'can(s)')

# FIXME (4): Calculate and output the total cost of paint can needed depending on color
paintColor = input('\nChoose a color to paint the wall:\n')
totalCost = paintColors.get(paintColor) * numOfCan
print('Cost of purchasing', paintColor, 'paint:', '$' + str(totalCost))















# # FIXME (1): Finish reading another word and an integer into variables. 
# # Output all the values on a single line
# favColor = input('Enter favorite color:\n')
# petName = input("Enter pet's name:\n")
# num = input('Enter a number:\n')

# print('You entered:', favColor, petName, num)


# # FIXME (2): Output two password options
# password1 = (favColor + '_' + petName)
# password2 = (num + favColor + num)

# print('\nFirst password:', password1)
# print('Second password:', password2)


# # FIXME (3): Output the length of the two password options
# print('\nNumber of characters in', password1 + ':', len(password1))
# print('Number of characters in', password2 + ':', len(password2))


