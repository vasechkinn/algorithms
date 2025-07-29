def factorial(n: int) -> int:
    """
    принимает одно целое число n 
    и возвращает факториал этого числа
    :param n: число, из которого надо найти факториал
    :return: int
    """
    if not isinstance(n, int):
        raise TypeError('ne int')
    
    if n > 20 or n < 0:
        raise ValueError('net :3')
    
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result