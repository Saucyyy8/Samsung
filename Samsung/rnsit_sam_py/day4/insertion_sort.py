import sys

def insertion_sort(strings):
    for i in range(1, len(input_list)):
        element = strings[i]
        j = i-1
        while j >= 0 and element.lower() < strings[j].lower():
            strings[j+1] = strings[j]
            j -= 1
        strings[j+1] = element
    return strings

input_list = sys.argv[1:]
print('User given strings are: \n', input_list)

sorted_list = insertion_sort(input_list)
print('Sorted strings are: \n', input_list)
