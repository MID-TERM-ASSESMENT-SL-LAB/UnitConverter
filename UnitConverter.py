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

    def mass():
        def choice():
            def calculation(inp, unit_in, unit_out):
                SI = {'microgram [μg]': 10 ** (-9), 'milligram [mg]': 10 ** (-6), 'gram [g]': 10 ** (-3),
                      'kilogram [kg]': 1, 'tonne [t]': 10 ** 3, 'ounce [oz]': 0.0283495, 'pound [lb]': 0.453592,
                      'US ton': 907.185}
                return inp * SI[unit_in] / SI[unit_out]

            inp = float(e1.get())
            unit_in = inputf.get()
            unit_out = inputt.get()
            result = calculation(inp, unit_in, unit_out)
            e2.delete(0, END)
            e2.insert(0, result)

        mass = ttk.Frame(tabControl)
        tabControl.add(mass, text='Mass')

        options = ['microgram [μg]', 'milligram [mg]', 'gram [g]', 'kilogram [kg]', 'tonne [t]', 'ounce [oz]',
                   'pound [lb]', 'US ton']

        inputf = StringVar()
        inputf.set(options[3])
        dropdownf = OptionMenu(mass, inputf, *options)

        inputt = StringVar()
        inputt.set(options[6])
        dropdownt = OptionMenu(mass, inputt, *options)

        ttk.Label(mass, text='Input: ').grid(row=0)
        e1 = Entry(mass)
        e1.grid(row=0, column=1)
        dropdownf.grid(row=0, column=2)

        ttk.Label(mass, text='Result: ').grid(row=1)
        e2 = Entry(mass)
        e2.grid(row=1, column=1)
        dropdownt.grid(row=1, column=2)

        okbtn = Button(mass, bg='#C51A4A', fg='#FFFFFF', text='Convert', font=('Footlight MT Light', 8, 'bold'),
                       command=choice)
        okbtn.grid(row=2, column=1)
        return


    def time():
        def choice():
            def calculation(inp,unit_in,unit_out):
                SI = {'nanosecond [ns]':10**(-9), 'microsecond [μs]':10**(-6), 'millisecond [ms]':10**(-3), 'second [s]':1, 'minute [min]':60, 'hour [h]':3600, 'day':3600*24, 'week':3600*24*7}
                return inp*SI[unit_in]/SI[unit_out]
            
            inp = float(e1.get())
            unit_in = inputf.get()
            unit_out = inputt.get()
            result = calculation(inp,unit_in,unit_out)
            e2.delete(0,END)
            e2.insert(0,result)
            
        time = ttk.Frame(tabControl)
        tabControl.add(time, text='Time')
        
        options = ['nanosecond [ns]', 'microsecond [μs]', 'millisecond [ms]', 'second [s]', 'minute [min]', 'hour [h]', 'day', 'week']

        inputf = StringVar()
        inputf.set(options[5])
        dropdownf = OptionMenu(time,inputf,*options)
        
        inputt = StringVar()
        inputt.set(options[3])
        dropdownt = OptionMenu(time,inputt,*options)
        
        ttk.Label(time, text='Input: ').grid(row=0)
        e1 = Entry(time)
        e1.grid(row=0, column=1)
        dropdownf.grid(row=0, column=2)
        
        ttk.Label(time, text='Result: ').grid(row=1)
        e2 = Entry(time)
        e2.grid(row=1, column=1)
        dropdownt.grid(row=1, column=2)    

        okbtn = Button(time, bg='#C51A4A', fg='#FFFFFF', text='Convert', font=('Footlight MT Light',8,'bold'), command=choice)
        okbtn.grid(row=2, column=1)
        return
    def speed():
        def choice():
            def calculation(inp, length_in, time_in, length_out, time_out):
                SIlength = {'centimeter [cm]':10**(-2), 'meter [m]':1, 'kilometer [km]':10**3, 'inch [in]':0.0254, 'foot [ft]':0.3048, 'mile [mi]':1609.34}
                SItime = {'second [s]':1, 'minute [min]':60, 'hour [h]':3600}
                return inp*(SIlength[length_in]/SItime[time_in])/(SIlength[length_out]/SItime[time_out])
            
            inp = float(e1.get())
            length_in = lengthf.get()
            time_in = timef.get()
            length_out = lengtht.get()
            time_out = timet.get()
            result = calculation(inp, length_in, time_in, length_out, time_out)
            e2.delete(0,END)
            e2.insert(0,result)
            
        speed = ttk.Frame(tabControl)
        tabControl.add(speed, text='Speed') 
    
        lengthoptions = ['centimeter [cm]', 'meter [m]', 'kilometer [km]', 'inch [in]', 'foot [ft]', 'mile [mi]']
        timeoptions = ['second [s]', 'minute [min]', 'hour [h]']

        lengthf = StringVar()
        lengthf.set(lengthoptions[5])
        lengthdropf = OptionMenu(speed,lengthf,*lengthoptions)

        timef = StringVar()
        timef.set(timeoptions[2])
        timedropf = OptionMenu(speed,timef,*timeoptions)
        
        lengtht = StringVar()
        lengtht.set(lengthoptions[2])
        lengthdropt = OptionMenu(speed,lengtht,*lengthoptions)

        timet = StringVar()
        timet.set(timeoptions[2])
        timedropt = OptionMenu(speed,timet,*timeoptions)

        ttk.Label(speed, text='Input: ').grid(row=0)   
        e1 = Entry(speed)
        e1.grid(row=0, column=1)
        lengthdropf.grid(row=0, column=2)
        ttk.Label(speed, text='/').grid(row=0, column=3)
        timedropf.grid(row=0, column=4)
        
        ttk.Label(speed, text='Result: ').grid(row=1)  
        e2 = Entry(speed)
        e2.grid(row=1, column=1)
        lengthdropt.grid(row=1, column=2)
        ttk.Label(speed, text='/').grid(row=1, column=3)
        timedropt.grid(row=1, column=4)      
        
        okbtn = Button(speed, bg='#C51A4A', fg='#FFFFFF', text='Convert', font=('Footlight MT Light',8,'bold'), command=choice)
        okbtn.grid(row=2, column=1)
        return
    def temperature():
        def choice():
            inp = float(e1.get())
            unit_in = inputf.get()
            unit_out = inputt.get()
            if unit_in != unit_out:
                if unit_in == 'Celsius [C]':
                    if unit_out == 'Fahrenheit [F]':
                        result = (inp*9/5)+32
                    else:
                        result = inp+273.15
                elif unit_in == 'Fahrenheit [F]':
                    if unit_out == 'Celsius [C]':
                        result = (inp-32)*5/9
                    else:
                        result = (inp-32)*5/9+273.15
                else:
                    if unit_out == 'Fahrenheit [F]':
                        result = (inp-(273.15))*9/5+32
                    else:
                        result = inp-273.15
            else:
                result = inp

            e2.delete(0,END)
            e2.insert(0,result)
            
        temperature = ttk.Frame(tabControl)
        tabControl.add(temperature, text='Temperature')
        
        options = ['Celsius [C]', 'Fahrenheit [F]', 'Kelvin [K]']

        inputf = StringVar()
        inputf.set(options[0])
        dropdownf = OptionMenu(temperature,inputf,*options)

        inputt = StringVar()
        inputt.set(options[1])
        dropdownt = OptionMenu(temperature,inputt,*options)
        
        ttk.Label(temperature, text='Input: ').grid(row=0)
        e1 = Entry(temperature)
        e1.grid(row=0, column=1)
        dropdownf.grid(row=0, column=2)
        
        ttk.Label(temperature, text='Result: ').grid(row=1)
        e2 = Entry(temperature)
        e2.grid(row=1, column=1)
        dropdownt.grid(row=1, column=2)
        
        okbtn = Button(temperature, bg='#C51A4A', fg='#FFFFFF', text='Convert', font=('Footlight MT Light',8,'bold'), command=choice)
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
    time()
    speed()
    temperature()
    mass()


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


