import random

user_number = int(input('Enter a number of your choice between [0 and 9]: '))
system_number = random.randint(0, 9)
if system_number != user_number:
	print('CrorePati')
else:
	print('RoadPati')