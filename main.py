from tkinter import *
import tkinter as tk
import random
import string


window = Tk()

window.title("Password Generator")

window.geometry("800x600")

window.configure(bg="white")

#HEADINGS

headinglabel = Label(window, text="Password Generator", font=("Poppins", 20,'bold'), width=20,bg="#5a069e",fg="black",relief=SUNKEN)
headinglabel.pack()
headinglabel.place(x=230, y=0)

headinglabel2 = Label(window, text="Modifiers", font=("Poppins", 20), width=20,bg="#057a6f",fg="black",relief=SUNKEN)
headinglabel2.pack()
headinglabel2.place(x=450,y=80)



#PASSWORD LENGTH SCALE



length_frame = Frame(window)
scale_text = Label(length_frame, text="Password Length", font=("Poppins", 20),width=20,bg="#057a6f",fg="black",relief=SUNKEN)
scale_text.grid(row=0, column=0)
scale = tk.Scale(length_frame,from_=0, to=24, orient=tk.HORIZONTAL, sliderlength=20,length=325,width = 25,font=("Poppins", 16))
scale.grid(row=1, column=0)
length_frame.grid(row=0, column=0)
length_frame.place(x=0, y=80)

img = PhotoImage(file="D:/VS CODE PROJ/PASS GENERATOR/tick.png")
smaller_img = img.subsample(18, 18)
length_button = Button(window, image=smaller_img, bg='#057a6f')
length_button.pack()
length_button.place(x=340, y=175)

#MODIFIERS 1.a-z 2.A-Z 3.0-9 4.SYMBOLS

options = ["A-Z", "a-z", "0-9", "symbols"]
selected_options = []
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

checkbutton_frame = Frame(window)

def toggle_option(option):
    if option in selected_options:
        selected_options.remove(option)
    else:
        selected_options.append(option)

C1 = Checkbutton(checkbutton_frame, text=options[0], command=lambda: toggle_option(options[0]), font=("Poppins", 16), indicatoron=0, width=8,selectcolor="#5a069e",variable=var1)
C1.grid(row=0, column=0)

C2 = Checkbutton(checkbutton_frame, text=options[1], command=lambda: toggle_option(options[1]), font=("Poppins", 16), indicatoron=0, width=8,selectcolor="#5a069e",variable=var2)
C2.grid(row=0, column=1)

C3 = Checkbutton(checkbutton_frame, text=options[2], command=lambda: toggle_option(options[2]), font=("Poppins", 16), indicatoron=0, width=8,selectcolor="#5a069e",variable=var3)
C3.grid(row=2, column=0)

C4 = Checkbutton(checkbutton_frame, text=options[3], command=lambda: toggle_option(options[3]), font=("Poppins", 16), indicatoron=0, width=8,selectcolor="#5a069e",variable=var4)
C4.grid(row=2, column=1)

checkbutton_frame.grid(row=0, column=0)
checkbutton_frame.place(x=500, y=150)

#GENERATE BUTTON


def generate_password():
    char_list = ""
    choice = selected_options
    if choice == ["A-Z"]:
        char_list += string.ascii_uppercase
    elif choice == ['A-Z', 'a-z']:
        char_list += string.ascii_uppercase + string.ascii_lowercase
    elif choice == ['A-Z', 'a-z','0-9']:
        char_list += string.ascii_uppercase + string.ascii_lowercase + string.digits
    elif choice == ['A-Z', '0-9']:
        char_list += string.ascii_uppercase + string.digits
    elif choice == ["A-Z", "symbols"]:
        char_list += string.ascii_uppercase + string.punctuation
    elif choice == ["A-Z", "symbols", "0-9"]:
        char_list += string.ascii_uppercase + string.digits + string.punctuation
    elif choice == ['A-Z','a-z','symbols']:
        char_list += string.ascii_uppercase + string.ascii_lowercase +  string.punctuation

    elif choice == ["a-z"]:
        char_list += string.ascii_lowercase
    elif choice == ["a-z", "0-9"]:
        char_list += string.ascii_lowercase + string.digits
    elif choice == ["a-z", "symbols"]:
        char_list += string.ascii_lowercase + string.punctuation
    elif choice == ["a-z", "symbols", "0-9"]:
        char_list += string.ascii_lowercase + string.digits + string.punctuation
    
    elif choice == ["0-9"]:
        char_list += string.digits
    elif choice == ["0-9", "symbols"]:
        char_list += string.digits + string.punctuation
    
    elif choice == ["symbols"]:
        char_list += string.punctuation
    else:
        char_list += string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    
    password = []
    

    for char in range(scale.get()):
        randomchar = random.choice(char_list)

        password.append(randomchar)

    
# Clear any existing text in the entry box
    password_entry.delete(0, END)
    
# Set the generated password in the entry box
    password_entry.insert(0, "".join(password))


generate_button = Button(window, text="Generate Password", font=("Poppins", 16), width=20,bg="green",fg="black",relief=SUNKEN,command=generate_password)  
generate_button.pack()
generate_button.place(x=260, y=300)

password_entry = Entry(window, font=("Poppins", 16), width=20,bg="lightgrey")
password_entry.pack()
password_entry.place(x=263, y=370)




window.mainloop()   