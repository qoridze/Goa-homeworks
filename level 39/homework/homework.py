# https://www.codewars.com/kata/55eca815d0d20962e1000106
def generate_range(start, stop, step):
    return list(range(start, stop + 1, step))


# https://www.codewars.com/kata/576b93db1129fcf2200001e6
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
# https://www.codewars.com/kata/5513795bd3fafb56c200049e
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]