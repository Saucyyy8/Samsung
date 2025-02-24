# Sum of Odd placed Even Digits
import sys

def sum_of_odd_placed_even_digits(number):
    sum1 = 0
    sum2 = 0
    flip = True
    while number > 0:
        digit = number % 10
        number = number // 10
        if digit % 2 == 0:
            if flip:
                sum1 += digit
            else:
                sum2 += digit
        flip = not flip
    if flip:
        return sum2
    return sum1

input_number = int(sys.argv[1])
sum_of_digits = sum_of_odd_placed_even_digits(input_number)

print(f'Sum of Odd placed Even digits of {input_number} is {sum_of_digits}')
