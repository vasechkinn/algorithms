def rotate_and_reverse(arr: list, k: int) -> list:
    if not isinstance(arr, list):
        raise TypeError('ne to (')
    
    if not isinstance(k, int):
        raise TypeError('ne int')
    
    if k < 0:
        raise ValueError('net :3')

    count = 0
    while count != k:
        elem = arr[len(arr)-1]
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i-1]

        arr[0] = elem
        count += 1

    length = len(arr) - 1
    for i in range(length //2):
        buff = arr[i]
        arr[i] = arr[length - i]
        arr[length - i] = buff

    return arr

arr = [1, 2, 3, 4, 5]
print(rotate_and_reverse(arr, 0))