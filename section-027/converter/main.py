from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    result_label.config(text="{0:.2f}".format(km))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=50)
window.config(padx=20, pady=20)

# First Section
# Entry
miles_input = Entry(width=10)
miles_input.pack()
miles_input.grid(column=1, row=0)

# miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


# Second Section
# is equal label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# result label
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# kilometer label
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# calculate button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)




window.mainloop()
