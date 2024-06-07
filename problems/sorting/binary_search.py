def binary_search(arr: list, x: int):
    if len(arr) == 0:
        return None

    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if x == arr[mid]:
            return arr[mid]
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if arr[mid] != x:
        return None
    return arr[mid]
