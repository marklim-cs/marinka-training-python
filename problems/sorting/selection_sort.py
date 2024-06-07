def selection_sort(arr: list):
    for i, value in enumerate(arr):
        min_idx = i
        for j, other_value in enumerate(arr[i+1:], i + 1):
            if other_value < arr[min_idx]:
                print("minimum index =",arr[min_idx], "other_value =", other_value)
                min_idx = j
        temp = value
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
        print(arr)

selection_sort([8, -10, 7, 55, 45, 3, -100, 0, 0])


def selection_sort2(arr: list):
    for i, value in enumerate(arr):
        min_idx, min_value = i, value
        for j, other_value in enumerate(arr[i+1:], i + 1):
            if other_value < min_value:
                min_idx, min_value = j, other_value
        arr[i], arr[min_idx] = min_value, value
