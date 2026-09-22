# File: homework1.py

# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, whole number, no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a decimal

c = 3j
print(c)
print(type(c)) # c is a complex data set, is an imaginary number

d = "hello"
print(d)
print(type(d)) # d is a string, a phrase closed by quotes

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a set of data

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a set of data tied to another set of data

g = (1,2)
print(g)
print(type(g)) # g is a tuple, a set of ordered values that cannot be changed

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a set of data where order doesn't matter

i = True
print(i)
print(type(i)) # i is a boolean, a logical value, either true or false

j = None
print(j)
print(type(j)) # j represents the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, a set of data where order doesn't matter

l = str(14)
print(l)
print(type(1)) # l is a string, a phrase denoted by quotes or str()

m = 1e4
print(m)
print(type(m)) # m is a float, because it has an exponant

# --- Questions 1 ---
# 1. I found 9 different data types
# 2. Float, integer, string, list, dictionary, complex data set, none, tuple, boolean
# 3. variables k,h,e have the same data type (list), variables d,l have the same data type (string), 
#    and variables b,m have the same data type(float)
# 4. The data type of 1 is an integer because it is a whole number. Str() makes everything within the
#    brackets into a string
# 5. n = range(1,5)
#    print(n)
#    print(type(n)) # n is a range, a sequance of numbers

# --- Booleans ---
print(10>9) # True, 10 is greater than 9
print(10 == 9) # False, 10 does not equal 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, "abc" is a form of data
print(bool(123)) # True, 123 is a form of data
print(bool(["apple", "cherry", "banana"])) # True, ["apple", "cherry", "banana"] is a form of data
print(bool(True)) # True, True is a form of data
print(bool(False)) # True, False is a form of data
print(bool(0)) # True, 0 evaluates to true because it is an integer
print(bool("")) # False, "" is an empty string and does not contain a data type
print(bool(" ")) # True, " " evaluates to true because it is a string
print(bool(())) # False, () is an empty tuple and does not contain data
print(bool([])) # False, [] is an empty set and does not contain data
print(bool({})) # False, {} is an empty dictionary and does not contain data
print(bool(True and False)) # False, a value cannot be both true and false
print(bool(True and True)) # True, a value can be true
print(bool(False and False)) # True, a value can be false
print(bool(True or False)) # True, a value can be either true or false
print(bool(True or True)) # False, a value cannot be true or another value that is not true, but also true
print(bool(False or False)) # False, a value cannot be false or false
print(bool(not(False))) # True, a value can be not false
print(bool(not(True))) # True, a value can be not true

# --- Questions 2 ---
# 1. An expression will return true if it is type of data and it logically makes sense. A value is false
#    if it is not data, usually a empty data types, or if it does not make logical sense
# 2. False or False was somewhat surprising, but makes sense that a value cannot be false or some other value that
#    is not false but also false
# 3. print(bool(10)), it is true because it is data
# 4. print(bool(not(True) and not(False))), it is false because a value cannot be both not true and not false

# --- Operators ---

# Arimthemtic Operators
print(
10 + 5, # 15, + performs addition
10 - 5, # 5, - performs subtraction
2 * 4, # 8, * performs multiplication
6 / 3, # 2, / is division
5 % 2, # 1, % is the remained from division
3 ** 2, # 9, ** is exponent
15 // 2 # 7, // is division that rounds down to the nearest whole number
)

# Comparison Operators
print(
5 == 2, # False, 5 doesn't equal 2
10 != 10, # False, 10 does equal 10
2 < 5, # True, 2 is less than 5
12 > 5, # True, 12 is greater than 5
5 <= 6, # True, 5 is less than or equal to 6
1 >= 10 # False, 1 is not greater than or equal to 10
)

# Assignment Operators
x = 5
x += 5 # x = 10, this adds 5 to x
x -= 4 # x= 6, this subtracts 4 from x
x *= 3 # x = 18, this multiplys x by 3
print(x)

# Logical Operators
# 1. It returns as true only if it meets both conditions 
#    print(bool((1 == 1) and (10 > 2))) # returns True
#    print(bool((1==1) and (2 > 10))) # returns False
# 2. It returns as true as long as one condition
#    print(bool((1==2) or (10 > 2))) # returns as True
#    print(bool((1==2) or (2 > 10))) # returns False
# 3. It returns as true as long as it does not its condition
#    print(bool(not True)) # returns True
#    print(bool((not True) and (not False))) # returns False

# --- Questions 3 ---
# 1. / is division, while // is division rounded down to the nearest whole number
# 2. % gives the remained from division, while // divides and rounds down to the nearest whole number
# 3. You would use the % operator
#    print(10 % 4) # returns 2
# 4. Assignment operators take a variable and edit it's value

# --- Strings ---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o
print(my_string[1:3]) # Prints: el
print(my_string[0:5:2]) # Prints:hlo
print(len(my_string)) # Prints: 5
print(my_string + "goodbye") # Prints: hellogoodbye
print(my_string * 7) # Prints: hellohellohellohellohellohellohello

# --- Questions 4 ---
# 1. Slicing is when you add to a string. We did this in manipulation number 11
# 2.This returns the first string followed by the variable, which is the second string
# 3. This returns the same result as the last question, but uses an f-string
# 4. The first print uses a string and then prints the variable, while the second print includes the variable in the first string
#    using an f-string

# --- Terminal Commands ---
# 1. cd, changes directories, used to move from one folder to another, ex. cd Desktop
# 2. ls, list, lists the contents of a directory, ex. ls Desktop
# 3. ls -a,list all, lists all directories including hidden ones, ex. ls -a Desktop
# 4. mkdir, make directory, creates a new directory in the current directory, ex. mkdir PythonDecal
# 5. pwd, print working directory, lists current directory, ex. pwd
# 6. cat, print file contents, prints the contents of a file without opening it, ex. cat homework1.py
# 7. cd .., change directories, changes current directory to the one previous directory, ex. cd ..
# 8. cd ., change directory, changes to current directory, ex. cd .
# 9. cd ~, change directory, changes directory to home directory, ex. cd ~
# 10. cp, copy, copies the selected item, ex. cp homework1.py
# 11. mv, move, moves an item to a different directory, ex. mv homework1.py ~/Desktop
# 12. rm, remove, removes a file within a directory, ex. rm Desktop
# 13. clear, clear, clears current terminal, ex. clear
# 14. grep, search, searches a file for specific words, grep homework1.py hello

# --- Questions 5 ---
# 1. nano, open, opens file and allows for edits, ex. nano homework1.py
#    rmdir, remove directory, removes the selected directory, ex. rmdir Desktop
#    touch, makes file, makes a file in the current directory, ex. touch homework2.py
# 2. ls lists all non-hidden files within a directory, while ls -a lists all files in that directory,
#    including hidden files
# 3. A hidden file is a file that can only be viewed using ls -a
# 4. -h, help, lists different flags and uses for a specific command, ex. grep -h
#    -v, verbose, gives an activity log for what the command is doing,ex. greap -v
#    -f, force, forces a command to run and ignores warnings
