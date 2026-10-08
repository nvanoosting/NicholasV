# --- Homework 1 + 2 Review ---

"""

--- Vocab Review ---

1. Git is acts as a kind of google drive for saving code and displaying edit history, while GitHub is an online site where people can share repos
2. The terminal is the entire gui that you interact with, while the command line is the place you enter commands
3. Local repos are stored on your device and can be accessed without an internet connection, while remote repos are downloaded and accessed through the internet
4. Version control is a system of managing files and edits over time
5. The staging area is where you send files before pushing them to a specific branch using git
6. git add will add the specified files to the staging area
7. git commit will save the files in the staging area locally
8. git push will push the committed files to a remote repository
9. git status will print the current status of any git procsess,and any errors it encounters
10. git pull will download a specific file or set of files from a remote repo
11. pwd will print the directory you are currently in
12. ls will list the files and directories in the directory you are currently in
13. cd will change your current directory to a specified directory
14. nano will open a specified file and allow you to make changes
15. touch will create a file
16. mv will move a file
17. rm will remove a file
18. cat will print the contents of a file to the terminal

--- Directory Tree ---

1. pwd
2. ls
3. cd ~/python_decal/brianna_repo && git pull origin main
4. mv homework.py ~/python_decal/judy_decal/homework
5. cd ~/python_decal/judy_decal/homework
6. cat homework.py
7. git add . , git commit -m "done with homework" , git push origin main
8. git pull origin main , git push origin main
9. cd ~/Recent

"""

# --- Homework 3 Review ---

def CheckDataType(value):
    return type(value)

def EvenOrOdd(value):
    if value % 2 == 0:
        return "Even"
    else:
        return "Odd"

def SumWithLoop(list):
    final_value = 0
    for num in list:
        final_value += num
    return final_value

# --- Homework 4 Review ---

def DuplicateList(list):
    final_list = []
    for value in list:
        final_list.append(value)
        final_list.append(value)
    return final_list

def square(num):
    return num * num

print(SumWithLoop([1,2,3,4,5,6,7,8,9,10]))