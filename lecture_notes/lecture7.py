# lists syntax
numbers = [1,2,3,4]
# print(numbers)

fruits = ["apple", "cherries", "bananas"]
# print(fruits)

mixed = ["hello", 5, True, None]
# print(mixed)

# access items in a list

print(numbers[1])

fruits[0] = "grape"

# adding items

numbers.append(6)

print(numbers)

print(mixed.insert(1, False))

print(mixed)

# removing items

fruits.remove("bananas")

print(fruits)

numbers.pop(0)

print(numbers)

for num in numbers:
    print(num)

list = [12, 14, 16, 18, 20, 22]

print(list[1:4])
