

# https://www.codewars.com/kata/55a14f75ceda999ced000048/train/python
def temple_strings(obj, feature): 
    return f"{obj} are {feature}"

# https://www.codewars.com/kata/596fba44963025c878000039/train/python
def contamination(text, char):
    if not text or not char:
        return ""
    return char * len(text)

# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python
def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]

# https://www.codewars.com/kata/562d8d4c434582007300004e/train/python
def obfuscate(email):
    email = email.replace('@', ' [at] ') 
    email = email.replace('.', ' [dot] ')  
    return email
