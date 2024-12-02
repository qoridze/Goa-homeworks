# 1)შექმენით სია რომელშიც იქნება 5 სახელი შემდეგ, ამოიღეთ სიიდან პირველი და ბოლო ელემენტი

list = ["nika", "barbare", "saba","mariami","luka"]
list.pop(0,"vano")
list.pop(-1,"genadi")
# 2)კომეტარებით ახსენით რას აკეთებს თითოეული ფუნქცია:

# .insert() gvibrunebs stringis da siis element 
# .append() siis bolos amtebs axal elements 
# .pop() irebs element siidan
# .len() konkretul siis elementze amatebs element

# 3) შექმენით სია რომელიც შედგება 5 სახელისგან შემდეგ insert მეთოდით დაამატეთ ახალი სახელი სიის მეორე ინდექსზე
name = ["saba","sandro","dato","elene","demetre"]
name.insert(3,"ilia")
print(name)