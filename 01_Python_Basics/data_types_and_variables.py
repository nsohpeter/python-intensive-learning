print("Variables in python")

print("*****************************")
# VARIABLES ION PYTHON
name = "peter"
# print(name)

greeting = "good morning"
print("hello," + greeting + " " + name.title())

# checking the type of of a variable

name = "peter"
index_num = 202524090121
checked = True
decimal = 1.24568
another_number = 1.5
print("\n")
print(type(name))
print(type(index_num))
print(type(checked))
print(type(decimal))
print(type(another_number))
print("\n")

# TYPECASTING IN VARIABLES

age = "20"
print(type(age))
new_age = int(age)
add_number = new_age + 1
print(add_number)
print(type(new_age))


"""
Simple program to change a 
letter in a word string
"""
name = "peter"
new_word = []
for ch in name:
    if ch == "p":
        new_word.append("B")
    else:
        new_word.append(ch)
my_new_word = "".join(new_word)
print(my_new_word)

"""
simple program that verify whether a person
is qualify to dirve
"""
age = int(input("what is your age?: "))
have_license = True
have_license_1 = input("Do you have a license? (yes/no): ")

if age >= 18 and have_license_1.lower() == "yes":
    print("you ar qualify to drive")
else:
    print("sorry, you are not qualified")
