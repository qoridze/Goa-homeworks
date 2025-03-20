
car = {
    "brand": "Tesla",
    "model": "Model S",
    "year": 2022
}


for key, value in car.items():
    print(f"{key}: {value}")


print("Keys:", car.keys())
print("Values:", car.values())


car_details = {
    "brand": "Tesla",
    "model": "Model X",
    "year": 2021,
    "color": "black"
}

for value in car_details.values():
    print(value)

# დიქშენერი car - შეიცავს მანქანის ბრენდს, მოდელს და წელს.
# მაგალითად, "brand" = "Tesla", "model" = "Model S", "year" = 2022
# ცალ-ცალკე გასაღები და მნიშვნელობები შეგიძლიათ მიიღოთ .keys() და .values() მეთოდებით

# სეტები:
# set1 - {1, 2, 3, 4, 5}
# set2 - {4, 5, 6, 7, 8}
# .union() საშუალებას იძლევა დაამატოთ ორივე სეტი, .intersection() - გამოიტანს საერთო ელემენტებს, ხოლო .difference() - გამოიტანს განსხვავებებს.

person_info = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


info_list = []


for key, value in person_info.items():
    info_list.append((key, value))

print(info_list)

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}

key_input = input("Please enter a key: ")
value_input = input("Please enter a value: ")


if key_input not in my_dict:
    my_dict[key_input] = value_input
    print(f"New key-value pair added: {key_input}: {value_input}")
else:
    print("Key already exists!")


print("Updated dictionary:", my_dict)
