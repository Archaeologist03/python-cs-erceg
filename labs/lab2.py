




# # FIXME (1): Finish reading item price and quantity, then output a receipt
# itemName = input('Enter food item name:\n')
# itemPrice = float(input('Enter item price:\n'))
# itemQnty = int(input('Enter item quantity:\n'))

# print('\nRECEIPT')
# print(itemQnty, itemName, '@ $', itemPrice,'= $', itemQnty * itemPrice)
# print('Total cost: $' ,itemQnty * itemPrice)  
   
# # FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt
# itemName2 = input('\n\nEnter second food item name:\n')
# itemPrice2 = float(input('Enter item price:\n'))
# itemQnty2 = int(input('Enter item quantity:\n'))
# totalCost = itemQnty * itemPrice + itemQnty2 * itemPrice2

# print('\nRECEIPT')
# print(itemQnty, itemName, '@ $', itemPrice, '= $', (itemQnty * itemPrice))
# print(itemQnty2, itemName2,'@ $', itemPrice2, '= $', (itemQnty2 * itemPrice2))
# print('Total cost: $', totalCost)   

# # FIXME (3): Add a gratuity and total with tip to the second receipt
# tip = (0.15 * (itemQnty * itemPrice + itemQnty2 * itemPrice2))
# totalWithTip = (tip + (itemQnty * itemPrice + itemQnty2 * itemPrice2))








# ======================================== #



# # (1) Prompt the user for the number of cups of lemon juice, water, and sugar needed to make lemonade. Prompt the user to specify the number of servings the recipe yields. Output the ingredients and serving size. (Submit for 2 points). 

# # Enter amount of lemon juice (in cups):
# # 2
# # Enter amount of water (in cups):
# # 16
# # Enter amount of agave nectar (in cups):
# # 2.5
# # How many servings does this make?
# # 6

# # Lemonade ingredients - yields 6.0 servings
# # 2.0 cup(s) lemon juice
# # 16.0 cup(s) water
# # 2.5 cup(s) agave nectar


# # How many servings would you like to make?
# # 48

# # Lemonade ingredients - yields 48.0 servings
# # 16.0 cup(s) lemon juice
# # 128.0 cup(s) water
# # 20.0 cup(s) agave nectar


# # Lemonade ingredients - yields 48.0 servings
# # 1.0 gallon(s) lemon juice
# # 8.0 gallon(s) water
# # 1.25 gallon(s) agave nectar





# # FIXME (1): Finish reading other items into variables, then output the three ingrdients
# lemonJuiceCups = float(input('Enter amount of lemon juice (in cups):\n'))
# waterInCups = float(input('Enter amount of water (in cups):\n'))
# nectarInCups = float(input('Enter amount of agave nectar (in cups):\n'))
# servings = float(input('How many servings does this make?\n'))

# print('Lemonade ingredients - yields ' + str(servings) +  ' servings')
# print(str(lemonJuiceCups) + ' cup(s) lemon juice')
# print(str(waterInCups) + ' cup(s) water')
# print(str(nectarInCups) + ' cup(s) agave nectar\n\n')


# # FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
# desiredServings = float(input('How many servings would you like to make?\n'))
# calcServings = (desiredServings / servings)
# calcLemonCups = (calcServings * lemonJuiceCups)
# calcWaterCups = (calcServings * waterInCups)
# calcNectarCups = (calcServings * nectarInCups)

# print('Lemonade ingredients - yields ' + str(desiredServings) + ' servings')
# print(str(calcLemonCups) + ' cup(s) lemon juice')
# print(str(calcWaterCups) + ' cup(s) water')
# print(str(calcNectarCups) +' cup(s) agave nectar\n')



# # FIXME (3): Convert and output the ingredients from (2) to gallons
# gallon = 16
# lemonGallon = calcLemonCups / gallon
# waterGallon = calcWaterCups / gallon
# nectarGallon = nectarInCups / gallon

# print('Lemonade ingredients - yields ' + str(desiredServings) + ' servings')
# print(str(lemonGallon) + ' gallon(s) lemon juice')
# print(str(waterGallon) + ' gallon(s) water')
# print(str(nectarGallon) + ' gallon(s) agave nectar')
   









# ==================================== #







# (1) Prompt the user to input an integer between 0 and 155, a float, a character, and a string, storing each into separate variables. Then, output those four values on a single line separated by a space. (Submit for 2 points). 

# Note: This zyLab outputs a newline after each user-input prompt. For convenience in the examples below, the user's input value is shown on the next line, but such values don't actually appear as output when the program runs.

# (2) Extend to also output in reverse. (Submit for 1 point, so 3 points total).

# (3) Extend to convert the integer to a character by using the 'chr()' function, and output that character. (Submit for 2 points, so 5 points total).


# Enter integer (0 - 155):
# 99
# Enter float:
# 3.77
# Enter character:
# z
# Enter string:
# Howdy
# 99 3.77 z Howdy
# Howdy z 3.77 99
# 99 converted to a character is c



# userInt = int(input('Enter integer (0 - 155):\n'))
# # FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
# userFloat = float(input('Enter float:\n'))
# userChar = input('Enter character:')
# userStr = str(input('Enter string:'))

# print(userInt, userFloat, userChar, userStr)


# # FIXME (2): Output the four values in reverse
# print(userStr, userChar, userFloat, userInt)

# # FIXME (3): Convert the integer to a characer, and output that character
# intToChar = chr(userInt)
# print(str(userInt) + ' converted to a character is ' + intToChar)