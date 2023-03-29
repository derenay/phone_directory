import numpy as np
import tkinter as tk
main_place = tk.Tk(screenName="Phone List")
#main_place.geometry("200x100")
main_place.title("Phone List")

phone_list = []

def add():


    name = e1.get(1.0, "end-1c")
    number = e2.get(1.0, "end-1c")
    short_list = []
    global phone_list
    for names in short_list:
        print(names)
        if name == names:
            break
    short_list.append(name)
    short_list.append(number)
    phone_list.append(short_list)
    print(phone_list)




def remove(name):
    pass

def edit(name, number):
    pass



tk.Label(main_place, text="Name").grid(row=0)
tk.Label(main_place, text="Phone number").grid(row=1)
e1 = tk.Text(main_place, width=20, height=1)

e2 = tk.Text(main_place, width=20, height=1)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

button1 = tk.Button(main_place, width=6,text="add", command=lambda: add())
button1.grid(row=0,column=2)
button2 = tk.Button(main_place, width=6, text="remove", command=lambda: add(e1, e2))
button2.grid(row=1,column=2)






main_place.mainloop()

