# Possible commands:
# mkdir <filename>, touch <filename>, cd <path>, ls or ls <path>, pwd, rmdir <path>, exit(d)

import os

#done
def mkdir(s):
    try:
        os.makedirs(s)
        print(s + " directory created successfully\n")
    except IOError:
        print("Error making folder" + s)

#done
def touch(s):
    try:
        outputfile = open(s,"w")
        print("File " + s + " created successfully")
    except IOError:
        print("there was an error creating output file!")

#done
def pwd():
    print(os.getcwd())

#done
def cd(s):
    try:
        os.chdir(s)
        print("navigated to " + s + " successfully")
    except IOError:
        print("there was an error navigating to " + s)

#done
def ls(s):
    if s == "":
        s = os.getcwd()
    try:
        print(os.listdir(s))
    except IOError:
        print("there was an error navigating to " + s)

#done
def rmdir(s):
    print(s)
    try:
        os.removedirs(s)
    except IOError:
        print("there was an error navigating to " + s)

def userSelection():
    flag = 0
    print("Welcome to Unix File System Simulator\n ")
    while flag is 0:
        print("Menu options:")
        print("mkdir")
        print("touch")
        print("cd")
        print("ls")
        print("pwd")
        print("rmdir")
        print("exit")

        selection = input("input: ")

        r = selection.split(" ")
        if len(r) < 2 and selection != "pwd" and selection != "ls" and selection != "exit":
            print("invalid input!")
            flag = 0
            continue


        searchVal = r[0]

        if(selection != "pwd" and selection != "ls" and selection != "exit"):
            passVal = r[1]
        else:
            passVal = ""

        if(searchVal.lower() == ("mkdir")):
            mkdir(passVal)
            flag = 0
        elif(searchVal.lower() ==  ("touch")):
            touch(passVal)
            flag = 0
        elif (searchVal.lower() == ("cd")):
            cd(passVal)
            searchVal = passVal
            flag = 0
        elif (searchVal.lower() == ("ls")):
            ls(passVal)
            flag = 0
        elif (searchVal.lower() == ("pwd")):
            pwd()
            flag = 0
        elif (searchVal.lower() == ("rmdir")):
            rmdir(passVal)
            flag = 0
        elif (searchVal.lower() == "exit"):
             flag = 1
             print("exiting..")
             break
        else:
            print("unsupported command")
            flag = 0

def main():
    userSelection()


main()
