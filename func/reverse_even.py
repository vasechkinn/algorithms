def reverse_even_elements(arr: list) -> list:
    if not isinstance(arr, list):
        raise TypeError('ne list')
    
    if len(arr) == 0:
        raise ValueError('net ^_^')

    even_elems_i = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_elems_i.append(i)

    new_arr = []
    for i in even_elems_i:
        new_arr.append(arr[i])

    arr_reverse = []
    for i in range(len(new_arr)-1, -1, -1):
        arr_reverse.append(new_arr[i])

    for i in range(len(even_elems_i)):
        arr[even_elems_i[i]] = arr_reverse[i]

    return arr

arr = [1, 2, 3, 4]
print(reverse_even_elements(arr))