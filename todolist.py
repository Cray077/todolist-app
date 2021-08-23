from os import listdir
from os.path import isfile, join

class Todolist:
    
    def __init__(self, text_str):
        self.text_str = text_str
        file_name = "list"
    
    def add(s):
        ls = open(file_name + ".txt", "a")
        ls.write(s + "\n")
        ls.close
        
    def read():
        name = "list"
        ls = open(file_name + ".txt","r", encoding = "ISO-8859-1")
        l = ls.readlines()
        todolist_number = 0
        for i in l:
            todolist_number += 1
            print(str(todolist_number) + " " + i)
        ls.close()
        
    def remove(num):
        ls = open(file_name + ".txt","r")
        l = ls.readlines()
        ls.close()
        print(l[num - 1])
        l.remove(l[num - 1])
        wls = open(file_name + ".txt", "w")
        wls.writelines(l)
        wls.close()
        
    def file_name(name):
        global file_name
        file_name = name
            
    def get_list(*i):
        print(i)

command = ""
Todolist.file_name("list")
while command != "exit":
    mypath = "/home/cray077/project/todolist2/"
    command = input("Enter a Command: ")
    
    if command == "open":
        files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        files.remove("todolist.py")
        f = []
        for name in files:
            i = name.replace('.txt','')
            e = i.strip()
            print(e)
        i = input("Name of the file: ")
        Todolist.file_name(i)
    
    if command == "add":
        e = ""
        while e != "exit":
            e = input("Add a todolist: ")
            if e != "exit":
                Todolist.add(e)
            else:e = "exit"
    if command == "read":
        Todolist.read()
        
    if command == "remove":
        Todolist.read()
        num = int(input("Enter the number of the list: "))
        Todolist.remove(num)
        Todolist.read()
    
    if command == "remove-m":
        Todolist.read()
        i = True
        ls = []
        q = 0        
        ls_ = []
        while i == True:
            e = input("Number of items to remove: ")
            if e == "done":
                i = False
            else: ls.append(int(e))    
        for e in ls:
            num = int(e)
            ls_.append(num)
        ls_1 = sorted(ls_)
        for item in ls_1:
            num = int(item)
            num -= q
            Todolist.remove(num)
            q += 1
            
    if command == "iop":
        pass