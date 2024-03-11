import tkinter as tk
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk

def Onclickstart():
    # Length feature
    def length():
        def choice():
            def calculation(inp, unit_in, unit_out):
                SI = {'nanometer [nm]': 10 ** (-9), 'micrometer [μm]': 10 ** (-6), 'millimeter [mm]': 10 ** (-3),
                      'centimeter [cm]': 10 ** (-2), 'meter [m]': 1, 'kilometer [km]': 10 ** 3, 'inch [in]': 0.0254,
                      'foot [ft]': 0.3048, 'yard [yd]': 0.9144, 'mile [mi]': 1609.34}
                return inp * SI[unit_in] / SI[unit_out]

            inp = float(e1.get())
            unit_in = inputf.get()
            unit_out = inputt.get()
            result = calculation(inp, unit_in, unit_out)
            e2.delete(0, END)
            e2.insert(0, result)

        length = ttk.Frame(tabControl)
        tabControl.add(length, text='Length')

        options = ['nanometer [nm]', 'micrometer [μm]', 'millimeter [mm]', 'centimeter [cm]', 'meter [m]',
                   'kilometer [km]', 'inch [in]', 'foot [ft]', 'yard [yd]', 'mile [mi]']

        inputf = StringVar()
        inputf.set(options[9])
        dropdownf = OptionMenu(length, inputf, *options)

        inputt = StringVar()
        inputt.set(options[5])
        dropdownt = OptionMenu(length, inputt, *options)

        ttk.Label(length, text='Input: ').grid(row=0)
        e1 = Entry(length)
        e1.grid(row=0, column=1)
        dropdownf.grid(row=0, column=2)

        ttk.Label(length, text='Result: ').grid(row=1)
        e2 = Entry(length)
        e2.grid(row=1, column=1)
        dropdownt.grid(row=1, column=2)

        okbtn = Button(length, bg='#C51A4A', fg='#FFFFFF', text='Convert', font=('Footlight MT Light', 8, 'bold'),
                       command=choice)
        okbtn.grid(row=2, column=1)
        return

    win = Toplevel()
    win.deiconify()
    win.resizable(0, 0)
    win.geometry('480x270')
    win.configure(bg='#008080')
    win.title('Unit Converter')
    tabControl = ttk.Notebook(win)
    tabControl.pack(expand=1, fill='both')
    length()

    win.mainloop()
    return


if __name__ == "__main__":
    wind = tk.Tk()
    wind.deiconify()
    wind.resizable(0,0)
    wind.geometry('480x270')
    wind.configure(bg='#C51A4A')
    wind.title('Unit Converter')
    entry = Label(wind, bg='#C51A4A', fg='#FFFFFF', text='Welcome to Unit Converter!', font=('Footlight MT Light',16,'bold'))
    entry.place(x=40, y=40, width=400, height=40)
    load = Progressbar(wind, orient=HORIZONTAL, length=250, mode='indeterminate')
    start = Button(wind, bg='#f5f5f5', fg='#000000', text='START', font=('Footlight MT Light',8,'bold'), command=Onclickstart)
    start.place(x=200, y=115, width=80, height=40)
    wind.mainloop()

