from tkinter import *

window = Tk()
window.title("Teste Title")
window.minsize(width=600, height=600)

# Label
label = Label(text="I Am a label!", font=("Arial", 24, "bold"))
label.pack(side="bottom")

label["text"] = "New Text"
label.config(text="New Text")


# Button
def button_clicked():
    new_text = inputs.get()
    label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
inputs = Entry(width=10)
inputs.pack()
print(inputs.get())



window.mainloop()
