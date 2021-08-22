class Todolist:
    def __init__(self, text_str):
        self.text_str = text_str
    
    def add(s):
        ls = open("list.txt", "a")
        ls.write(s + "\n")
        ls.close
        
    def read():
        ls = open("list.txt","r")
        l = ls.readlines()
        todolist_number = 0
        for i in l:
            todolist_number += 1
            print(str(todolist_number) + " " + i)
        ls.close()
        
    def remove(num):
        ls = open("list.txt","r")
        l = ls.readlines()
        ls.close()
        print(l[num - 1])
        l.remove(l[num - 1])
        wls = open("list.txt", "w")
        wls.writelines(l)
        wls.close()
        
    def get_list(*i):
        print(i)

command = ""
while command != "exit":
    command = input("Enter a Command: ")
    
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
        while i == True:
            e = input("Number of items to remove: ")
            if e == "done":
                i = False
            else: ls.append(e)
                
        q = 0        
        ls_ = []
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
        Todolist.read()
        i = True
        ls = []
        while i == True:
            e = input("Number of items to remove: ")
            if e == "done":
                i = False
            else: ls.append(e)
                
        q = 0        
        ls_ = []
        for e in ls:
            num = int(e)
            ls_.append(num)
        
        ls_1 = sorted(ls_)
        #print(ls)
        print(ls_1)
        
        
        
        