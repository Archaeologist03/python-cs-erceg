# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
favColor = input('Enter favorite color:\n')
petName = input("Enter pet's name:\n")
num = input('Enter a number:\n')

print('You entered:', favColor, petName, num)


# FIXME (2): Output two password options
password1 = (favColor + '_' + petName)
password2 = (num + favColor + num)

print('\nFirst password:', password1)
print('Second password:', password2)


# FIXME (3): Output the length of the two password options
print('\nNumber of characters in', password1 + ':', len(password1))
print('Number of characters in', password2 + ':', len(password2))