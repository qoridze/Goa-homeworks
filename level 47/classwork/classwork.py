# https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python
def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]
# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
def square_sum(numbers):
    return sum(num ** 2 for num in numbers)
# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python
def find_smallest_int(arr):
    return min(arr)
# https://www.codewars.com/kata/544675c6f971f7399a000e79/train/python
def string_to_number(s):
    return int(s)
# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
def summation(num):
    return num * (num + 1) // 2
# https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
def count_sheeps(sheep):
    return sum(1 for s in sheep if s)
# https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
def no_space(x):
    return x.replace(" ", "")
# https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python
def greet(name):
    return f"Hello, {name} how are you doing today?"
# https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
def boolean_to_string(b):
    return str(b)