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


## WORKING WITH STRINGS IN PYTHON

name = "peter"
greeting = "heyyy, good morning"

# different ways of printing strings on the console

print(name)
print(greeting)
print("hello, {} {}".format(name, greeting))
print(f"{greeting} {name}")

# we can loop throngh a string and do something
for ch in name:
    print(ch)  # normally this gives you the values not index

for ch in range(len(name)):  # if you need index, do this
    print(ch, name[ch])  # name[ch] = values and ch =index

for index, ch in enumerate(name):  # much cleaner
    print(index, ch)


# string are arrays so therefore can
# be accessed it characters using []
print(name[0])
print(name[-1])
print(name[1:3])
# count the number of characters in a word or word in a sentense
print(name.count("e"))
print(greeting.count("good"))  # et

# we cna find(): find the first occurrence
# of the specified value and returns the position ,-1 if not found

print(name.find("p"))
print(name.startswith("p"))

print(name.replace("p", "B"))
new_name = []
for ch in name:
    if ch == "p":
        new_name.append("B")
    else:
        new_name.append(ch)
# my_new_word = "".join(new_name)
print("".join(new_name))


list_items = [3, 4, 6, 7, 9]
print(list_items)
list_items[3:3] = [5]
# list_items.insert(2, 5)
print(list_items)
