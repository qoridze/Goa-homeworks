# https://www.codewars.com/kata/58649884a1659ed6cb000072/train/python
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "Invalid state"   
# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]
# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python
def abbrev_name(name):
    first_name, last_name = name.split()
    return f"{first_name[0].upper()}.{last_name[0].upper()}"
# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
def count_positives_sum_negatives(arr):
    if not arr:  
        return []
    
    positives_count = 0
    negatives_sum = 0
    
    for num in arr:
        if num > 0:
            positives_count += 1
        elif num < 0:
            negatives_sum += num
    
    return [positives_count, negatives_sum]
# https://www.codewars.com/kata/55225023e1be1ec8bc000390/train/python
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, " + name + "!"

