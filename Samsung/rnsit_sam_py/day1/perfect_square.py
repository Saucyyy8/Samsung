import math as mt

input_number = int(input('Enter a number to check if it is Perfect Square: '))

root_number = int(mt.sqrt(input_number))
if root_number * root_number == input_number:
    print(input_number, 'is a Perfect Square')
else:
    print(f'{input_number} is not a Perfect Square')