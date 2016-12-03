def medians(a, b):
    """return the medians of two sorted array of the same size 
    >>> medians([1, 2, 4, 6, 10], [4, 5, 6, 9, 12])
    11
    """
    assert len(a) == len(b)
    if len(a) <= 1:
        return a[0] + b[0]
    n = len(a)
    if a[n // 2] == b[n // 2]:
        if n % 2 == 0:
            return max(a[n // 2 - 1], b[n // 2 - 1]) + a[n // 2]
        else:
            return 2 * a[n // 2] 
    elif a[n // 2] > b[n // 2]:
        return medians(a[:n // 2 + 1], b[n // 2 :])
    else:
        return medians(a[n // 2 :], b[: n // 2 + 1])
        
