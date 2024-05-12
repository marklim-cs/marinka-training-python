'''shifting instead of swapping'''
def insertion_sort(arr: list):
    '''kek'''
    for i, key in enumerate(arr[1:], 1)
        previous_index = i - 1

        while previous_index >=0 and key < arr[previous_index]:
            arr[previous_index+1] = arr[previous_index]
            previous_index -= 1

        arr[previous_index+1] = key
