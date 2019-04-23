# FINAL EXAMS 
#4


# ======================================== #

# services = {
#   'Front yard': 35,
#   'Back yard': 45,
#   'Bushes': 12
# }

# lawn_service = input('Enter desired lawn service:\n')
# print('You entered:', lawn_service)
# if (lawn_service in services):
#     print('Cost of', lawn_service.lower() + ':', '$' + str(services[lawn_service])) 
# else:
#     print('Error: Requested service is not recognized')    


# ======================================== #


# lance_service = {
#   'Front yard': 35,
#   'Back yard': 45,
#   'Full yard': 75,
#   'Bushes': 12,
# }

# print('Lance\'s Lawn Service')
# print('Front yard --', '$' + str(lance_service['Front yard']))
# print('Back yard --', '$' + str(lance_service['Back yard']))
# print('Full yard --', '$' + str(lance_service['Full yard']))
# print('Bushes --', '$' + str(lance_service['Bushes']))

# first_service = input('\nSelect first service:')
# second_service = input('\nSelect second service:')

# print('\n\nLance\'s Lawn Service invoice')



# if second_service == '-' and first_service == '-':
#   print('\n\nTotal:', '$' + '0')
# elif second_service == '-':
#   print('\nService 1:', str(first_service) + ',', '$' + str(lance_service[first_service]))
#   print('Service 2:', 'No service')
#   print('\nTotal:', '$' + str(lance_service[first_service]))
# elif first_service == '-':
#   print('\nService 1:', 'No service')
#   print('Service 2:', str(second_service) + ',', '$' + str(lance_service[second_service]))
#   print('\nTotal:', '$' + str(lance_service[second_service]))
# else:
#   print('\nService 1:', str(first_service) + ',', '$' + str(lance_service[first_service]))
#   print('Service 2:', str(second_service) + ',', '$' + str(lance_service[second_service]))
#   print('\nTotal:', '$' + str((lance_service[first_service]) + lance_service[second_service]))