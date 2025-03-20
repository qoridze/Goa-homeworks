
my_dict = {
    'name': 'Giorgi',
    'age': 25,
    'city': 'Tbilisi'
}


keys_list = []
values_list = []


for key, value in my_dict.items():
    keys_list.append(key)
    values_list.append(value)


print("Keys:", keys_list)
print("Values:", values_list)


result = [10, 43, 12, 11, 94, 10, 55, 7, 11]


unique_result = []
for item in result:
    if item not in unique_result:
        unique_result.append(item)

print("Unique List:", unique_result)

student = {}
student['name'] = 'Levan'
student['age'] = 30
student['city'] = 'Batumi'
print(student)

numbers = [1, 2, 3, 4, 5]

numbers.append(6)

ა
numbers.remove(3)


numbers.reverse()

print(numbers)


my_tuple = (1, 2, 3, 4)


print(my_tuple.index(3))


print(len(my_tuple))


my_set = {1, 2, 3, 4}


my_set.add(5)

my_set.remove(3)

print(my_set)


my_string = "Hello, world!"


my_string = my_string.replace("world", "Python")


print(len(my_string))


user_dict = {}


key = input("შეიყვანეთ key: ")
value = input("შეიყვანეთ value: ")


user_dict[key] = value

old_value = user_dict[key]
new_value = input(f"ძველი value: {old_value}. შეიყვანეთ ახალი value: ")

user_dict[key] = new_value


print("საბოლოო dictionary:", user_dict)

def remove_duplicates(input_list):
    result_list = []
    for item in input_list:
        if item not in result_list:
            result_list.append(item)
    return result_list

sample_list = [10, 20, 20, 30, 40, 10, 50]
unique_list = remove_duplicates(sample_list)


print("Unique List:", unique_list)
