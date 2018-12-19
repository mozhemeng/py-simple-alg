def find_smallest(arr):
    min_num = arr[0]
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
            min_idx = i
    return min_idx


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr
