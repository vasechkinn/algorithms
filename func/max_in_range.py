def max_in_range(arr: list[int | float],
                 start: int,
                 end: int):
    
    if not isinstance(arr, list):
        raise TypeError('ne to (')
    
    if not isinstance(start, int):
        raise ValueError('ne int')
    
    if not isinstance(end, int):
        raise ValueError('ne int')
    
    if start > end or start < 0 or end > (len(arr) - 1) or end < 0:
        raise ValueError('начальная координата должна быть меньше конечной')
    
    imax_abs = start
    imax_otn = 0
    max_elem = arr[start]
    
    for i in range(start + 1, end + 1):
        if arr[i] > max_elem:
            max_elem = arr[i]
            imax_otn = i - start
            imax_abs = i

    return imax_otn, imax_abs


arr = [5, 4, 3, 2, 4, 8]
print(max_in_range(arr, 2, 2))