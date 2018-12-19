def fast_sort(arr):
    if len(arr) < 2:
        return arr
    num = arr[0]
    smaller = [i for i in arr[1:] if i <= num]
    bigger = [i for i in arr[1:] if i > num]
    return fast_sort(smaller) + [num] + fast_sort(bigger)
