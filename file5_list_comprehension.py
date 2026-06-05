# List comprehension = A concise way to create lists in python
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]

#1️⃣ traditional way of creating a list

even_nums = []

for x in range(1,11):
    if x % 2 == 0:
        even_nums.append(x)
#print(even_nums)

#2️⃣ list comprehension with expression and optional condition

doubles = [num * 2 for num in range(1,11)]
#print(doubles)

triples = [num * 3 for num in range(1,11)]
#print(triples)

squares = [num * num for num in range(1,11)]
#print(squares)


#3️⃣ List comprehension with condition
random_nums = [1,-12,-15,5,7,-21,4,-7,57,6,-1,14,19]

positive_nums=[num for num in random_nums if num >= 0]
# print(positive_nums)

negative_nums = [num for num in random_nums if num < 0]
# print(negative_nums)

even_nums = [x for x in random_nums if x % 2 == 0]
# print(even_nums)

odd_nums = [o for o in random_nums if o % 2 == 1]
# print(odd_nums)

#4️⃣ list comprehension for strings

fruits = ["apple", "banana", "orange", "pine-apple", "berries"]

# fruits_in_uppercase = [fruit.upper() for fruit in fruits]
# print(fruits_in_uppercase)

fruits_in_uppercase2 = [fruit.upper() for fruit in ["apple", "banana", "orange", "pine-apple", "berries"]]
# print(fruits_in_uppercase2)

fruits_first_character = [fruit[0] for fruit in fruits]
print(fruits_first_character)