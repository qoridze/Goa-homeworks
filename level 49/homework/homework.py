# 1)https://www.codewars.com/kata/5963c18ecb97be020b0000a2/train/python
def derive(coefficient, exponent): 
    new_coefficient = coefficient * exponent
    
    new_exponent = exponent - 1

    return f"{new_coefficient}x^{new_exponent}"

# 2)https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/python
def whatday(num):
    return {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}.get(num, "Wrong, please enter a number between 1 and 7")
# 3)https://www.codewars.com/kata/55c28f7304e3eaebef0000da/train/python
def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i += 1 
    return res

# 4)https://www.codewars.com/kata/526c7363236867513f0005ca/train/python
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False