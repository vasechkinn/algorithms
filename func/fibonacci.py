def fibonacci(n: int) -> list[int]:
    """
    0, 1, 1, 2, 3, 5, 8, 13
    """
    if not isinstance(n, int):
        raise TypeError('ne int')
    
    if n < 0:
        raise ValueError('net :3')
    
    if n == 0:
        elems = [0]
    else:
        elems = [0, 1]
        i = 1

        while i != n:
            i = elems[-1] + elems[-2]
            elems.append(i)
    
    return elems