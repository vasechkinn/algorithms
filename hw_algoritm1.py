# ***************num_2
def frequent_elem(array: list[int]) -> int:
    arr_count = []

    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                count += 1
        arr_count.append([array[i], count])

    max_elem = arr_count[0][1]
    elem = arr_count[0][0]

    for i in range(len(arr_count)):
        if arr_count[i][1] > max_elem:
            max_elem = arr_count[i][1]
            elem = (arr_count[i][0])
        elif arr_count[i][1] == max_elem:
            if arr_count[i][0] < elem:
                elem = arr_count[i][0]

    return elem

array = [1, 1, 1, 2, 3, 3, 3]
print(frequent_elem(array))

# num3 *******************************
def nums_target(array: list[int], target: int):
    elems = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                elems.append([array[i], array[j]])

    return elems

array = [1, 2, 3, 4, 0]
target = 3
print(nums_target(array, target))