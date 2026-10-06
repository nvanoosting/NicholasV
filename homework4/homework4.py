# --- Lists ---

favorite_foods = ["Pizza", "Potato", "Chicken"]

print(favorite_foods[1], # lists the second item in the favorite foods list
      favorite_foods[-1] # lists the last item in the favorite foods list
)

favorite_foods.append("Shrimp") # adds "Shrimp" to the end of the favorite_foods list

favorite_foods.insert(0, "Apple") # adds "Apple" to the beginning of the favorite_foods list

favorite_foods.remove("Chicken") # removes the string "Chicken" from the favorite_foods list list

print(len(favorite_foods)) # prints the length of the favorite_foods list

for food in favorite_foods: # iterates over the whole favorite_foods list
    print(food.upper()) # prints the result in uppercase

first_last_favorite_foods = favorite_foods[0::3] # creates a new list with the first and last terms from favorite_foods list

for food in favorite_foods: # iterates over the whole favorite_foods list
    if food == "Potato": # checks if the food matches the given string
        print("A potato!")
    else:
        print("No potato!")

numbers = list(range(0,21)) # creates a list from 0 to 20

def get_first_15(numbers): 
    lst = numbers[0:15] # slices the numbers list from 0 to 15
    return lst

def get_every_5th(lst):
    lst1 = lst[::5] # creates lst1 from every fifth term of the input list
    return lst1

def reverse_and_stride(lst):
    lst1 = lst[::-1] # creates lst1 from the reverse of the input list
    return lst1[::3] # returns every thrid term of lst1

print(reverse_and_stride(get_every_5th(get_first_15(numbers))))

numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(numbers[2][0:3], # prints the third row
      numbers[1][1] # prints the second item in the second row
)

numbers.append([10, 11, 12]) # adds another row to the numbers list

def sum_nested(numbers):
    total = 0 
    for row in numbers: # iterates over the rows 
        for num in row: # iterates over the numbers in the rows
            total += num # adds the numbers to the total
    return total

def five_x_five_loop():
    five_x_five_list = []
    for row in range(5): # iterates from 0 to 5
        five_x_five_list.append([]) # adds a row
        for num in range(1, 6): # iterates from 1 to 6
            five_x_five_list[row].append(num + 5 * row) # adds a number to the corrisponding row
    return five_x_five_list

def multiples_of_three():
    lst = five_x_five_loop()
    for row in lst: # iterates over the rows
         for num in row: # iterates over the numbers in the rows
            if num % 3 == 0:
                row[row.index(num)] = "?" # sets numbers divisible by 3 to "?"
    return lst

def not_equal():
    lst = multiples_of_three()
    total = 0 
    for row in lst: # iterates over the rows
        for num in row: # iterates over the numbers in the rows
            if num != "?": # checks if num is not equal to "?"
                total += num # adds num to the total
    return total

# --- Dictionaries --- 

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])

ages["Milana"] = 52

ages.pop("Mariam")

for names in ages:
    print(names,
          ages[names]
    )

print(not_equal())
