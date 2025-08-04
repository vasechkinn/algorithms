def count_ones(n: int) -> int:
    """
    принимает одно целое число n в десятичном представлении 
    и возвращает количество единиц в его 
    двоичном представлении
    :param n: число, которое переводится в двоичную
    :return: int
    """
    if not isinstance(n, int):
        raise TypeError('ne int')
    
    if n < 0:
        raise ValueError('должно быть больше 0')
    
    elem = n
    count = 0
    while elem != 0:
        ost = elem % 2

        if ost == 1:
            count += 1
            
        elem = elem // 2
    
    return count
    

n = 1
print(count_ones(n))