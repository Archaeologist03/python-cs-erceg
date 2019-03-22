# # LAB 4

# # ======================================== #

# # services = {
# #   "Oil change": 35,
# #   "Tire rotation": 19,
# #   "Car wash": 7
# # }

# # auto_service = input('Enter desired auto service:')
# # print('\nYou entered:', auto_service)
# # if auto_service in services:
# #   print('Cost of', str(auto_service).lower() + ':',  '$' + str(services[auto_service]))
# # else: 
# #   print('Error: Requested service is not recognized')



# # ======================================== #





# dav_auto_shop = {
#   'Oil change': 35,
#   'Tire rotation': 19,
#   'Car wash': 7,
#   'Car wax': 12,
# }

# print('Davy\'s auto shop services')
# print('Oil change --', '$' + str(dav_auto_shop['Oil change']))
# print('Tire rotation --', '$' + str(dav_auto_shop['Tire rotation']))
# print('Car wash --', '$' + str(dav_auto_shop['Car wash']))
# print('Car wax --', '$' + str(dav_auto_shop['Car wax']))

# first_service = input('\nSelect first service:')
# second_service = input('\nSelect second service:')

# print('\n\nDavy\'s auto shop invoice')



# if second_service == '-' and first_service == '-':
#   print('\n\nTotal:', '$' + '0')
# elif second_service == '-':
#   print('\nService 1:', str(first_service) + ',', '$' + str(dav_auto_shop[first_service]))
#   print('Service 2:', 'No service')
#   print('\nTotal:', '$' + str(dav_auto_shop[first_service]))
# elif first_service == '-':
#   print('\nService 1:', 'No service')
#   print('Service 2:', str(second_service) + ',', '$' + str(dav_auto_shop[second_service]))
#   print('\nTotal:', '$' + str(dav_auto_shop[second_service]))
# else:
#   print('\nService 1:', str(first_service) + ',', '$' + str(dav_auto_shop[first_service]))
#   print('Service 2:', str(second_service) + ',', '$' + str(dav_auto_shop[second_service]))
#   print('\nTotal:', '$' + str((dav_auto_shop[first_service]) + dav_auto_shop[second_service]))


# # ======================================== #