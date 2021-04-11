# This script is a brief introduction to Python basics

s = "Python is great"

print(s[3:len(s)])
print(s[-3])

# STRINGS ARE IMMUTABLE OBJECTS!!
# s[0] = "H"             ERROR!!!

# Negative index: print from the -3 to the end
# The last element is the element at index = -1
print(s[-3:])

# I can replace strings with 'replace' method
s1 = s.replace("great", "wonderful")
print("before replace: {}".format(s))
print("after replace: {}".format(s1))

# I can find a substring into another string
print("I'm searchin for '{c}' character in {s}. Where is it? {index}".format(c="h", s=s, index=s.find("h")))
print("I'm searchin for '{c}' character in {s}. Where is it? {index}".format(c="T", s=s, index=s.find("T")))

import math as m


def compute_sqrt_and_square(to_square, to_sqrt):
    x1 = to_square ** 2
    x2 = m.sqrt(to_sqrt)
    return x1, x2


# If I do not take each element that the function returns, then I obtain a tuple!
t = compute_sqrt_and_square(36, 36)
print(type(t))
print(t[0])
print(t[1])

square, root = compute_sqrt_and_square(36, 36)
print(type(square))
print(type(root))

# This is the proof that the two options are the same
print(t[0] == square)
print(t[1] == root)

# ========================================================================================

#                                      LIST OBJECTS

# ========================================================================================

# This creates a LIST object (MUTABLE LIST)
fruits = ["apples", "oranges", "bananas", "strawberries"]
print(fruits, type(fruits))

# This creates a TUPLE object (IMMUTABLE LIST)
cars = ("Tesla", "BMW", "Audi", "Ferrari")
print(cars, type(cars))

# I can APPEND new elements to a list
fruits.append("Blueberries")
print(fruits)

# But I cannot append a new car to the cars TUPLE!!!
# cars.append("Wolksvagen")                 ERROR!!!

# I can order my list with sort method
fruits.sort()
print(fruits)

# I can also reverse the order
fruits.sort(reverse=True)
print(fruits)

# I can pop out an element to a LIST object
fruits.pop(2)
print(fruits)

# By default, delete the last element in the list
popped_out = fruits.pop()
print(fruits)
print("Popped out: " + popped_out)

# ========================================================================================

#                                      DICTIONARY OBJECTS

# ========================================================================================

# I can define a dictionary: association 'key: value'
people = {
    "Giorgio": 33333,
    "Samantha": 4537628,
}

try:
    print(people["Giorgio"])
    print(people["Davide"])
except KeyError as missing_key:
    print("Missing key {k}".format(k = missing_key))

# I can use the 'get' method that allows us the get the value associated to a key
print(people.get("Davide"))

if people.get("Davide") is None:
    print("Non c'è nessun Davide")

# But I can avoid the if statement...
print(people.get("Davide", "Missing key"))

# Getting all keys in a dictionary
phone_numbers = list(people.values())
people_names = list(people.keys())

# This returns a LIST of TUPLE objects
key_value = list(people.items())

print(people_names)
print(phone_numbers)
print(key_value)

# ========================================================================================

#                                      LOOPS AND LIST OBJECTS

# ========================================================================================
print("\n ====================== PRINT FRUIT IN A LIST ======================\n")
for fruit in fruits:
    print(fruit)

print("\n ====================== PRINT GENE SEQUENCE IN A STRING ======================\n")
gene = "ATTTGACTATGA"
# Getting all the nucleotide in the string
for nuc in gene:
    print(nuc)

print("\n ====================== CHECK IF GENE SEQUENCE IS VALID ======================\n")
# Check if the gene length is multiple of 3
if len(gene) % 3 == 0:
    print("Valid gene sequence")
else:
    print("Invalid gene sequence")

# I can also cycle through the keys of the dictionary
print("\n ====================== PRINT PEOPLE LIST ======================\n")
for p in people.keys():
    print(p)



# It works!!!
s = "First line\n" \
    "second line\n" \
    "third line"

print(s.split("\n")[1:])
print("".join(s.split("\n")[1:]))

s = "ATGTTCGAG"

for i in range(1, len(s)+1):
    print(s[-i])

