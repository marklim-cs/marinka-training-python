def minimum(arr: list) -> int:
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    return min(arr[-1], minimum(arr[:-1]))

def minimum_index(arr: list) -> int:
    if len(arr) == 0:
        return None
    minimum_value = arr[0]
    minimum_idx = 0
    for i, value in enumerate(arr):
        if value < minimum_value:
            minimum_value = value
            minimum_idx = i
    return minimum_idx

def minimum_index_rec(arr: list) -> int:
    if len(arr) == 0:
        return None

    def index(arr: list, index: int):
        index = 0
        if len(arr) == 1:
            return index

        return 











def minimum_faster(arr: list) -> int:
    if len(arr) == 0:
        return None

    def rec(arr: list, length: int):
        if length == 1:
            return arr[0]
        last_element = arr[length-1]
        return min(last_element, rec(arr, length-1))

    return rec(arr, len(arr))

#if __name__ == "__main__":
    #import random
    #import timeit
    #arr = [random.randint(0, 1000) for _ in range(500)]
    #min_time = timeit.timeit(lambda: minimum(arr), number=10000)
    #min_time_faster = timeit.timeit(lambda: minimum_faster(arr), number=10000)

    #print(f"{min_time} vs {min_time_faster}")
