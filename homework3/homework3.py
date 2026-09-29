# --- Print Functions ---

def say_goodbye(name):
    print("Goodbye,", name) # prints "Goodbye" and the name variable

def circle_area(radius):
    pi = 3.14
    print(pi * radius ** 2) # prints the produect of pi and radius squared

# --- Return Funtions ---

def subtract(a, b):
    return a - b # returns a minus b

def multiply(a, b):
    return a * b # returns a multiplied by b

def divide(a, b):
    return a / b # returns a divided by b

# --- Conditionals ---

def temperature_values(readings):
    return (min(readings), max(readings))

def is_weekend(day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if days.index(day) == 5 or days.index(day) == 6: # Compares the position of the inputted day to the position of Saturday and Sunday in the list
        return True
    else:
        return False

def fuel_efficiency(distance, fuel_used):
    return distance / fuel_used # divides distance by the fuel used to give fuel efficiency

def data_encryption(data):
    last_digit = data % 10 # gives last digit by giving remainder
    remaining_num = data // 10 # gives remaining number without the last digit by dropping remainder
    multiplier = 1 # multiplies last digit by the number of places in the remaining number
    temporary = remaining_num
    while temporary > 0: # ensures the temporary value is reduced to 0 
        temporary //= 10
        multiplier *= 10
    return (last_digit * multiplier) + remaining_num # multiplies last digit and multiplier to put the last digit in front of the remaining number

# --- Loops ---

def power_function(x, y):
    final_x = 1 # sets final value to 1
    for i in range(y): # multiplies final value by x for y amount of times
        final_x *= x
    return final_x

def for_minimum(list):
    min = float("inf") # sets min to the highest possible value
    for num in list: 
        if num < min: 
            min = num # sets min equal to the num if num is less than the current min
    return min

def for_maximum(list): # sets max to lowest possible value
    max = float("-inf")
    for num in list:
        if num > max: # sets max equal to the num if the num is greater than the current max
            max = num
    return max

def while_minimum(list):
    min = list[0] # starts the min at the first term in the list
    index = 0 
    while index < len(list): # ensures we iterate over the whole list
        if list[index] < min:
            min = list[index] # sets the min equal to the term being iterated over if it is less than the current min
        index += 1 # ensures the while loop moves forward
    return min

def while_maximum(list):
    max = list[0] # starts the max at the first term in the list
    index = 0
    while index < len(list): # ensures we iterate over the whole list
        if list[index] > max:
            max = list[index]
        index += 1 # ensures the while loop moves forward
    return max

def digit_sum(num):
    sum = 0 # sets the sum to zero
    while num > 0:
        last_digit = num % 10 # divides the num and gives the remainder
        remaining_number = num // 10 # divides the num and gives value without remainder
        num = remaining_number # sets the num equal to the remaining value
        sum += last_digit # adds the last digit to the final sum
    return sum
