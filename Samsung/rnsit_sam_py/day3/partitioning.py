def partionArray(numbers):
    j = 0
    pivot = numbers[-1]
    for i in range(len(numbers)):
        if numbers[i] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i] # move the smaller element to the left
            j += 1
    numbers[j], numbers[-1] = numbers[-1], numbers[j] # place the pivot element in its final position

print('Enter the input numbers')
numbers = list(map(int, input().split()))

print(f'Input Array is: {numbers}')
partionArray(numbers)
print(f'Partitioned Array is: {numbers}')