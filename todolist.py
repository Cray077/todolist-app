class Todolist:
    def __init__(self, text_str):
        self.text_str = text_str
    
    def Add_list(s):
        ls = open("list.txt", "a")
        ls.write(s + "\n")
        ls.close
        
    def Read_list():
        ls = open("list.txt","r")
        l = ls.readlines()
        todolist_number = 0
        for i in l:
            todolist_number += 1
            print(str(todolist_number) + " " + i)
        ls.close()
        
    def Remove_list(num):
        ls = open("list.txt","r")
        l = ls.readlines()
        ls.close()
        l.remove(l[num - 1])
        wls = open("list.txt", "w")
        wls.writelines(l)
        wls.close()
        Todolist.Read_list()

command = ""
while command != "exit":
    command = input("Enter a Command: ")
    
    if command == "add":
        e = ""
        while e != "exit":
            e = input("Add a todolist: ")
            if e != "exit":
                Todolist.Add_list(e)
            else:e = "exit"

    if command == "read":
        Todolist.Read_list()
        
    if command == "remove":
        Todolist.Read_list()
        num = int(input("Enter the number of the list: "))
        Todolist.Remove_list(num)