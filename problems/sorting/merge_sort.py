def merge_sort(array):
    if len(array) > 1:
        middle_point = len(array) // 2
        left_array = array[:middle_point]
        right_array = array[middle_point:]

        merge_sort(left_array)
        merge_sort(right_array)

        l = r = c = 0

        while l < len(left_array) and r < len(right_array):
            if left_array[l] < right_array[r]:
                array[c] = left_array[l]
                l += 1
            else:
                array[c] = left_array[l]
                r += 1
            c += 1

        while l < len(left_array):
            array[c] = left_array[l]
            c += 1
            l += 1

        while r < len(right_array):
            array[c] = right_array[r]
            c += 1
            l += 1