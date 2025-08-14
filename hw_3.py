def check_arr(arr):
    if not isinstance(arr, list):  raise TypeError('ne list')

# 1 **********************************************************
def bubble_sort(arr: list, sorting_attribute: lambda x, y: x > y) -> list:
    check_arr(arr)

    length = len(arr) - 1
    
    for i in range(length):
        for j in range(length - i):

            if sorting_attribute(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return  arr

# 2 **********************************************************

def sorting_choice(arr: list, sorting_attribute = lambda x, y: x > y):
    check_arr(arr)
    
    length = len(arr)

    count_comparison = 0
    count_permutation = 0

    for i in range(length):
        jtarget = i

        for j in range(i+1, length):
            if sorting_attribute(arr[jtarget], arr[j]):
                jtarget = j
                count_comparison += 1

        arr[i], arr[jtarget] = arr[jtarget], arr[i]
        count_permutation += 1

    return arr, (count_comparison, count_permutation)

# 3 **********************************************************

def recursive_sum(arr: list[int | float], len_arr: int) -> int | float:
    
    check_arr(arr)

    if len(arr) == 0:
        return 0

    if len_arr == 0:
        return arr[0]
    
    return arr[len_arr] + recursive_sum(arr, len_arr - 1)

# 4 **********************************************************

def recursive_max(arr: list, length: int):

    check_arr(arr)

    if len(arr) == 0:
        return 0

    if length == 0:
        return arr[0]
    
    second_elem = recursive_max(arr, length-1)

    if arr[length] >= second_elem:
        return arr[length]
    
    return second_elem

# 5 **********************************************************

def recursive_sum_even(arr: list, length: int):
    check_arr(arr)
    if len(arr) == 0:
        return 0
    
    if length == 0 and arr[0] % 2 == 0:
        return arr[0]
    
    if length == 0 and arr[0] % 2 != 0:
        return 0
    
    elem = recursive_sum_even(arr, length - 1)

    if arr[length] %2 == 0:
        return arr[length] + recursive_sum_even(arr, length - 1)
    
    return 0 + recursive_sum_even(arr, length - 1)


# 6 **********************************************************
def reverse_string(word: str, len_word: int, arr = []):
    if len_word == 0:
        return word[0]
    
    return word[len_word] + reverse_string(word, len_word - 1)

def reverse_string_arr(word: str, len_word: int, arr = []):
    if len_word == 0:
        return ''.join(arr) + word[0] 
    
    arr.append(word[len_word])
    
    return reverse_string(word, len_word - 1, arr)

# 7 **********************************************************
def is_palindrome(word: str, len_word: int, arr = []):
    if len_word == 0:
        new_word = ''.join(arr) + word[0]

        if new_word == word:  
            return True
        return False
    
    arr.append(word[len_word])
    return is_palindrome(word, len_word - 1, arr)

# 9 **********************************************************
def sum_of_digits(number: int):
    if number // 10 == 0:
        return number % 10

    return number % 10 + sum_of_digits(number // 10)

a = 1234
print(sum_of_digits(a))