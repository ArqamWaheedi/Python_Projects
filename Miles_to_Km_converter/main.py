from tkinter import *

windows = Tk()
windows.title("Mile to Km Converter")
windows.minsize(width=400, height=200)
windows.config(padx=100, pady=100)

equality_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equality_label.grid(row=1, column=0)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(row=0, column=2)

Km_label = Label(text="Km", font=("Arial", 12, "bold"))
Km_label.grid(row=1, column=2)


def button_clicked():
    new_value = float(mile_inputs.get())
    km = new_value*1.609
    km_inputs.delete(0, END)
    km_inputs.insert(0, f"{km}")


button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=1)

mile_inputs = Entry(width=10)
mile_inputs.insert(END, "0")
mile_inputs.grid(row=0, column=1)

km_inputs = Entry(width=10)
km_inputs.insert(END, "0")
km_inputs.grid(row=1, column=1)

windows.mainloop()
