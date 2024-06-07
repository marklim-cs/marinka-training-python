def binary_search_recursive(arr: list, x: int):
    if len(arr) == 0:
        return None

    def low_high_pointers(low: int, high: int):
        if low > high:
            return None

        mid = (low + high) // 2
        if x == arr[mid]:
            return arr[mid]
        if x > arr[mid]:
            return low_high_pointers(mid+1, high)
        if x < arr[mid]:
            return low_high_pointers(low, mid-1)

    return low_high_pointers(0, len(arr)-1)