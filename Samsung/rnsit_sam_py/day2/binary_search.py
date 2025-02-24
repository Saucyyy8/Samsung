def binary_search(array, search_element):
    high = len(array) - 1 
    low  = 0
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == search_element:
            return mid
        elif search_element < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1 # The value -1 indicates, search element not found