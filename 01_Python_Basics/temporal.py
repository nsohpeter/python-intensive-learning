## WORKING WITH STRINGS IN PYTHON

name = "peter"
greeting = "heyyy, good morning"

# different ways of printing strings on the console

# print(name)
# print(greeting)
# print("hello, {} {}".format(name, greeting))
# print(f"{greeting} {name}")

# we can loop throngh a string and do something
# for ch in name:
#     print(ch)  # normally this gives you the values not index

# for ch in range(len(name)):  # if you need index, do this
#     print(ch, name[ch])  # name[ch] = values and ch =index

# for index, ch in enumerate(name):  # much cleaner
#     print(index, ch)


# string are arrays so therefore can
# be accessed it characters using []
# print(name[0])
# print(name[-1])
# print(name[1:3])
# count the number of characters in a word or word in a sentense
# print(name.count("e"))
# print(greeting.count("good"))  # et

# we cna find(): find the first occurrence
# of the specified value and returns the position ,-1 if not found

# print(name.find("p"))
# print(name.startswith("p"))

# print(name.replace("p", "B"))
# new_name = []
# for ch in name:
#     if ch == "p":
#         new_name.append("B")
#     else:
#         new_name.append(ch)
# # my_new_word = "".join(new_name)
# print("".join(new_name))


list_items = [3, 4, 6, 7, 9]
print(list_items)
list_items[3:3] = [5]
# list_items.insert(2, 5)
print(list_items)
