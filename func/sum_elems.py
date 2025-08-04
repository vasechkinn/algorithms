def amount_plus_1(digits: list[int]) -> list:
    if not isinstance(digits, list):
        raise TypeError('ne list :()')
    
    if len(digits) < 1 or len(digits) > 100:
        raise ValueError('net')

    elem = 0
    count = len(digits) - 1
    for i in range(len(digits)): 
        elem += digits[i] *10**count
        count -= 1

    elem += 1
    str_elem = str(elem)
    new_digits = []

    for i in range(len(str_elem)):
        new_digits.append(int(str_elem[i]))

    return new_digits

digits = [9, 0, 9]
print(amount_plus_1(digits))
