from tkinter import *
from tkinter import messagebox



def save():

    MIS = MIS_label_entry.get()
    Name = Name_label_entry.get()
    Email = email_label_entry.get()
    Password = password_label_entry.get()
    Male_Female = v.get()
    x = ""
    if Male_Female == 1:
        x = "Male"
    else:
        x = "Female"

    if len(MIS) == 0 or len(Password) == 0 or len(Name) == 0 or Male_Female == 0:
        messagebox.showinfo(title="Opps", message="Khali choda kya kuch?")
    else:

        is_ok = messagebox.askokcancel(title=MIS, message=f"You Entered: \nName:: {Name} \nEmail: {Email} \nPassword: {Password} \nGender: {x} \nIs it okay?")

        if is_ok:
            with open("data.text",  "a") as data_file:
                data_file.write(f"{MIS} | {Name} | {Email} | {x} | {Password}\n")
                MIS_label_entry.delete(0, END)
                password_label_entry.delete(0, END)
                v.set(0)

window = Tk()
window.title("MIS College Game")
window.config(padx=50, pady=50)

canvas = Canvas(height=300, width=300)
logo_img = PhotoImage(file="MIS.png")
canvas.create_image(150, 150, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
MIS_label = Label(text='MIS No. :')
MIS_label.grid(row=1,column=0)

Name_label = Label(text="Name :")
Name_label.grid(row=2,column=0)

email_label = Label(text="Email :")
email_label.grid(row=3,column=0)

password_label = Label(text="Password :")
password_label.grid(row=4, column=0)

Male_Female_label = Label(text="Male/Female :")
Male_Female_label.grid(row=5, column=0)


#Entries
MIS_label_entry = Entry(width=40)
MIS_label_entry.grid(row=1, column=1, columnspan=2)
MIS_label_entry.focus()

Name_label_entry = Entry(width=40)
Name_label_entry.grid(row=2, column=1, columnspan=2)

email_label_entry = Entry(width=40)
email_label_entry.grid(row=3, column=1, columnspan=2)
email_label_entry.insert(END, "@coep.ac.in")

password_label_entry = Entry(width=20)
password_label_entry.grid(row=4, column=1)

v = IntVar()

Male_entry = Radiobutton(text="Male", variable=v, value=1)
Male_entry.grid(row=5, column=1, columnspan=2)
Female_entry = Radiobutton(text="Female", variable=v, value=2)
Female_entry.grid(row=5, column=2, columnspan=2)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=4, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=7, column=1, columnspan=2)

window.mainloop()
