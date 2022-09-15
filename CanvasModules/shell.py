#This  is a terminal program to show a list of files
import os
print("Welcome to terminal Program")
while 1:
        cmd = input("CELLESH > ")
        if cmd == "exit":
                exit()
        elif cmd == "ls":
                print("list out files ..... ")
                print(os.listdir())
        elif cmd == "lsraw":
                print(os.popen("ls").read())
        elif cmd == "create new folder":
                folder_name = input("What is your folder name? ")
                os.popen("mkdir " + str(folder_name)).read()
        else:
                print("command not understood")