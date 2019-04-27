# usr_inp = input('Enter a sentence or phrase:')
# print()
# print()
# print('You entered:', usr_inp)
# print()

# def get_num_of_characters(inputStr):
#     count = 0
#     length = len(inputStr)
#     for i in range(0, length):
#         count = count + 1
#     output = 'Number of characters: ' + str(count)
#     return output

# def output_without_whitespace(inputStr):
#     output = 'String with no whitespace: ' + inputStr.replace(' ', '')
#     print(output)
#     return output

# if __name__ == '__main__':
#     # Type your code here
#     num = get_num_of_characters(usr_inp)
#     print(num)
#     output_without_whitespace(usr_inp)






# ======================================== #








# # Type all other functions here


# # GET NUMBER OF NON WHITESPACE CHARS
# def get_num_of_non_WS_characters(inputStr):
#     whitespace = 0
#     for char in inputStr:
#         if (char == ' ' or char == '\t'):
#             whitespace += 1
#     return (len(inputStr) - whitespace)


# def get_num_of_words(inputStr):
#     words = inputStr.split()
#     return len(words)


# # FIX CAPITALIZATION
# def fix_capitalization(inputStr):
#     letterCapped = 0
#     charArr = []
#     for char in inputStr:
#         charArr.append(char)
#     # Check if first word is capitalized..
#     if (charArr[0].islower()):
#         charArr[0] = inputStr[0].upper()
#         letterCapped += 1

#     # Check whole text
#     x = 0
#     capNext = 'false'
#     for char in charArr:
#         if (capNext == 'true' and char != ' ' and char != '\t'):
#             charArr[x] = inputStr[x].upper()
#             letterCapped += 1
#             capNext = 'false'
#         if (char == '.' or char == '!' or char == '?'):
#             capNext = 'true'
#         x += 1

#     # Reformant text(string)
#     newStr = ''
#     for char in charArr:
#         newStr = newStr + char

#     print('Number of letters capitalized:', letterCapped, end='\n')
#     print('Edited text:', newStr, end='\n\n')
#     return newStr, letterCapped


# # REPLACE PUNCTATION
# def replace_punctuation(inputStr, exclamationCount, semicolonCount):
#     exclamationCount = 0
#     semicolonCount = 0
#     charArr = []
#     for character in inputStr:
#         charArr.append(character)
#     # Check over array for ! or ;
#     x = 0
#     for char in charArr:
#         if (char == '!'):
#             charArr[x] = '.'
#             exclamationCount += 1
#         elif (char == ';'):
#             charArr[x] = ','
#             semicolonCount += 1
#         x += 1

#     # Reformat string
#     newStr = ''
#     for char in charArr:
#         newStr = newStr + char

#     # Print Output
#     print('Punctuation replaced', end='\n')
#     print('exclamationCount:', exclamationCount, end='\n')
#     print('semicolonCount:', semicolonCount, end='\n')
#     print('Edited text:', newStr, end='\n\n')
#     return newStr


# # SHORTEN SPACE
# def shorten_space(inputStr):
#     words = inputStr.split()
#     newStr = ''
#     for word in words:
#         if newStr == '':
#             newStr = word
#         elif (newStr != ''):
#             newStr = newStr + ' ' + word
#     print('Edited text:', newStr, end='\n\n')
#     return newStr


# # PRINT MENU FUNCTION..
# def print_menu():
#     print(
#         'MENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Fix capitalization\nr - Replace punctuation\ns - Shorten spaces\nq - Quit\n'
#     )
#     menuOp = input('Choose an option:\n')
#     while (menuOp != 'c' and menuOp != 'w' and menuOp != 'f' and menuOp != 'r'
#            and menuOp != 's' and menuOp != 'q'):
#         menuOp = input('Choose an option:\n')
#     return menuOp


# # COMANDS - FINAL OUTPUT
# if __name__ == '__main__':
#     # Complete main section of code
#     inputStr = str(input('Enter a sample text:'))
#     print('\n\nYou entered:', inputStr, end='\n\n')
#     command = ''
#     # q = Go on until q
#     while (command != 'q'):
#         command = print_menu()
#         # c = Number of non-whitespace characters
#         if (command == 'c'):
#             print(
#                 'Number of non-whitespace characters:',
#                 get_num_of_non_WS_characters(inputStr),
#                 end='\n\n')
#         # w = Number of words
#         elif (command == 'w'):
#             print('Number of words:', get_num_of_words(inputStr), end='\n\n')
#         # f = Fix capitalization
#         elif (command == 'f'):
#             fix_capitalization(inputStr)
#         # r = Replace punctuation
#         elif (command == 'r'):
#             replace_punctuation(inputStr, 0, 0)
#         # s = Shorten spaces
#         elif (command == 's'):
#             shorten_space(inputStr)
