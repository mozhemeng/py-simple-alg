def binary_search(l, v):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (high + low) // 2
        if l[mid] == v:
            return mid
        if l[mid] < v:
            low = mid + 1
        if l[mid] > v:
            high = mid - 1
    return None
