def binary_search_pointer(array:list[int], target:int):
    upper_bound = len(array) - 1
    lower_bound = 0

    while lower_bound <= upper_bound:
        # Find the middle index
        middle_index = (upper_bound + lower_bound) // 2


        # Same some time by returning value if bound happens to land on target
        if target == array[middle_index]:
            return middle_index
        if array[upper_bound] == target:
            return upper_bound
        elif array[lower_bound] == target:
            return lower_bound
        
        if target > array[middle_index]:
            lower_bound = middle_index + 1
        elif target < array[middle_index]:
            upper_bound = middle_index - 1

def binary_search_splicing(array:list[int], target):
    eliminated_elements = 0
    while True:
        middle_index = (len(array) - 1) // 2
        if len(array) == 1 and array[0] != target:
            return -1
        else:
            if array[middle_index] == target:
                if len(array) == 1:
                    return eliminated_elements
                else:
                    return eliminated_elements + middle_index
            elif target < array[middle_index]:
                buffer = array.copy()
                array.clear()
                for i in range(middle_index):
                    array.append(buffer[i])

            elif target > array[middle_index]:
                eliminated_elements = eliminated_elements + middle_index + 1
                buffer = array.copy()
                array.clear()
                for i in range(middle_index+1, len(buffer)):
                    array.append(buffer[i])



test_array = [5, 15, 25, 35, 45, 55]
print(binary_search_pointer(test_array,35))