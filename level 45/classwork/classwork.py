# https://www.codewars.com/kata/55902c5eaa8069a5b4000083/train/python
def format_money(amount):
    return f"${amount:.2f}"
# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python
def same_case(a,b):
    
    if not (a.isalpha() and b.isalpha()):
        return -1
    
    
    if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
        return 1
    
    return 0
# https://www.codewars.com/kata/5388f0e00b24c5635e000fc6/train/python
def swap_values(args): 
    if len(args) == 2:
        
        args[0], args[1] = args[1], args[0]
    else:
        print("Array must have exactly two elements.")
# https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python
def sum_mul(n, m):
    
    if n <= 0 or m <= 0:
        return "INVALID"
    
    
    total_sum = 0
    for i in range(n, m, n):
        total_sum += i
    
    return total_sum
