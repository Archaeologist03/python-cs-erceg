
# MIDTERM LAB 2


# ======================================== #

# userInt = int(input('Enter integer (0 - 155):\n'))
# # FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
# userFloat = float(input('Enter float:\n'))
# userChar = input('Enter character:\n')
# userStr = str(input('Enter string:\n'))

# print(userInt, userFloat, userChar, userStr)


# # FIXME (2): Output the four values in reverse
# print(userStr, userChar, userFloat, userInt)



# # FIXME (3): Convert the integer to a characer, and output that character
# intToChar = chr(userInt)
# print(str(userInt) + ' converted to a character is ' + intToChar)




# ======================================== #




# # FIXME (1): Finish reading other items into variables, then output the three ingrdients
# lemonJuiceCups = float(input('Enter amount of lemon juice (in cups):\n'))
# waterInCups = float(input('Enter amount of water (in cups):\n'))
# nectarInCups = float(input('Enter amount of agave nectar (in cups):\n'))
# servings = float(input('How many servings does this make?\n\n'))

# print('Lemonade ingredients - yields ' + str(servings) +  ' servings')
# print(str(lemonJuiceCups) + ' cup(s) lemon juice')
# print(str(waterInCups) + ' cup(s) water')
# print(str(nectarInCups) + ' cup(s) agave nectar\n')


# # FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
# desiredServings = float(input('How many servings would you like to make?\n\n'))

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
# nectarGallon = calcNectarCups / gallon

# print('Lemonade ingredients - yields ' + str(desiredServings) + ' servings')
# print(str(lemonGallon) + ' gallon(s) lemon juice')
# print(str(waterGallon) + ' gallon(s) water')
# print(str(nectarGallon) + ' gallon(s) agave nectar')
   





# ======================================== #




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

# print('\n15% gratuity: $', tip)
# print('Total with tip: $', totalWithTip)