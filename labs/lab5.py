# # LAB 5

# ======================================== #



# # 18.15 Ch 5 Program: Drawing a half arrow (Python 3)

# arrow_base_height = int(input('Enter arrow base height:\n'))

# arrow_base_width = int(input('Enter arrow base width:\n'))

# arrow_head_width = int(input('Enter arrow head width:\n'))

# while arrow_head_width <= arrow_base_width: 
#     arrow_head_width = int(input('Enter arrow head width:\n'))
#     continue

# print()

# for i in range(arrow_base_height):
#   for j in range(arrow_base_width):
#     print('*', end="")
#   print()

# while arrow_head_width != 0:
#   for i in range(arrow_head_width):
#     print('*', end='')
#   print()
#   arrow_head_width = arrow_head_width - 1



# ======================================== #


# # 18.14 Ch 5 Warm up: Drawing a right triangle (Python 3)

# triangle_char = input('Enter a character:\n')
# triangle_height = int(input('Enter triangle height:\n'))
# print('')

# # print ('* ')
# # print ('* * ')
# # print ('* * * ')


# for i in range(triangle_height + 1):
#     for j in range(i):
#         print(triangle_char, end="")
#     print('')
