def is_palindrome(x: int) -> bool:
    """
    получает на вход число и, если число является палидромом,
    выдает true, иначе false
    :param x: число для проверки
    :raturn: true | false
    """
    if not isinstance(x, int):
        raise TypeError('ne int')
    
    if x < 0:
        return False

    copy_x = x
    arr = []

    while x != 0:
        ost = x % 10
        arr.append(str(ost))
        x = x // 10

    elem_res = ''.join(arr)

    if str(copy_x) == elem_res:
        return True
    return False
   
x = -1
print(is_palindrome(x))