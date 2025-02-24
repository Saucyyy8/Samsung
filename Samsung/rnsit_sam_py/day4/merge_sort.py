def merge(numbers, low, mid, high):
    array1 = numbers[low : mid+1]
    array2 = numbers[mid+1 : high+1]

    i = 0
    j = 0
    k = low
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            numbers[k] = array1[i]
            i += 1
        else:
            numbers[k] = array2[j]
            j += 1
        k += 1
    numbers[k:high+1] = array1[i:] + array2[j:]
    # numbers[k:high+1] = array2[j:]

def merge_sort(numbers, low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort(numbers, low, mid)
        merge_sort(numbers, mid+1, high)
        merge(numbers, low, mid, high)

print('Enter the input numbers: ')
numbers = [int(num) for num in input().split()]

merge_sort(numbers, 0, len(numbers)-1)
print('Sorted Numbers are \n', numbers)
