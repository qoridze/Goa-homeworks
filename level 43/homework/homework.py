# https://www.codewars.com/kata/5933a1f8552bc2750a0000ed/train/python
def nth_even(n):
    return 2 * (n - 1)
# https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python
def add_length(str_):
    strArr = str_.split(" ")
    result = []
    
    for i in strArr:
        result.append(f"{i} {len(i)}")
    return result
# https://www.codewars.com/kata/57f6ad55cca6e045d2000627/train/python
def square_or_square_root(arr):
    import math

    return [int(math.sqrt(x)) if math.sqrt(x).is_integer() else x**2 for x in arr]

# https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python
def find_difference(a, b):
    return abs(a[0] * a[1] * a[2] - b[0] * b[1] * b[2])
