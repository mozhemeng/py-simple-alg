import random


def random_fast_sort(arr):
    if len(arr) < 2:
        return arr
    num = arr.pop(random.randint(0, len(arr)-1))
    smaller = [i for i in arr if i <= num]
    bigger = [i for i in arr if i > num]
    return random_fast_sort(smaller) + [num] + random_fast_sort(bigger)
