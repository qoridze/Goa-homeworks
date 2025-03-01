# https://www.codewars.com/kata/59f08f89a5e129c543000069/train/python
# def dup(arry):
#         result = []
#     for string in arry:
#         new_string = []
#         for i in range(len(string)):
            
#             if not new_string or new_string[-1] != string[i]:
#                 new_string.append(string[i])
#         result.append(''.join(new_string))
#     return result
# https://www.codewars.com/kata/57a1ae8c7cb1f31e4e000130/train/python
def get_min_max(seq):
    if len(seq) == 0:
        return None, None  
    return min(seq), max(seq)

