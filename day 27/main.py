from tkinter import *

#(row 0, column 1) quantas miles
#(0, 2) miles
#(1,0) is equal to
#(1, 1) resultado
#(1, 2) Km
#(2, 1) button calculate

def converting_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    result_label.config(text=f"{km:.2f}")

#Window configurations
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Labels configurations
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

#Entries configurations
miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

#Button configuration
button = Button(text="Calculate", command=converting_to_km)
button.grid(row=2, column=1)

window.mainloop()