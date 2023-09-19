import tkinter as tk
import time
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

#root window
root = tk.Tk()
root.wm_iconbitmap('icon.ico')
root.geometry("300x330")
root.resizable(False, False)
root.title("Conversion Calculator™")
root.config(bg = 'gray15')

#style config
s = ttk.Style()
s.configure('TFrame', background='gray20')
s.configure('TLabel', background='gray20', foreground='white')
s.configure('TEntry', bg='red', foreground='gray30')

main_frame = ttk.Frame(root)
main_frame.place(anchor="c", relx=.5, rely=.5)
#top frame -----------------------------------------------------------------------
t_frame = ttk.Frame(main_frame, style='TFrame')
t_frame.grid(row=0, column=0)

t_label = ttk.Label(t_frame, text='Please enter a value:')
t_label.grid(row=0, column=0, padx=10, pady=10)

userinput = tk.Entry(t_frame, bg='gray30', fg='white', relief='sunken')
userinput.grid(row=0, column=1, pady=10)

#output function
def textoutput(output):
    convoutput.delete('0','end')
    convoutput.insert('0', output)

#number conversion functions
def bin_to_hex():
    output = hex(int(userinput.get(), 2))
    textoutput(output)

def hex_to_bin():
    output = bin(int(userinput.get(), 16))
    textoutput(output)

def bin_to_den():
    output = int(userinput.get(), 2)
    textoutput(output)
        
def den_to_bin():
    output = bin(int(userinput.get(), 10))
    textoutput(output)

def hex_to_den():
    binary = bin(int(userinput.get(), 16))
    output = int(binary, 2)
    textoutput(output)

def den_to_hex():
    output = hex(int(userinput.get(), 10))
    textoutput(output)

def lb_to_kg():
    output = float(userinput.get()) * 0.4535924
    textoutput(output)

def kg_to_lb():
    output = float(userinput.get()) * 2.204623
    textoutput(output)

def in_to_cm():
    output = float(userinput.get()) * 2.54
    textoutput(output)

def cm_to_in():
    output = float(userinput.get()) * 0.3937008
    textoutput(output)
    
def ft_to_m():
    output = float(userinput.get()) * 0.3048
    textoutput(output)

def m_to_ft():
    output = float(userinput.get()) * 3.28084
    textoutput(output)

#middle frame -----------------------------------------------------------------------
m_frame = ttk.Frame(main_frame, style='TFrame')
m_frame.grid(row=1, column=0)

#number conversion buttons
b_h_button = tk.Button(m_frame, text='Bin to Hex', command=bin_to_hex, bg='gray15', fg='white', relief='flat', width=9)
b_h_button.grid(row=0, column=0, padx=10, pady=10)

b_d_button = tk.Button(m_frame, text='Bin to Den', command=bin_to_den, bg='gray15', fg='white', relief='flat', width=9)
b_d_button.grid(row=0, column=1, padx=10, pady=10)

h_d_button = tk.Button(m_frame, text='Hex to Den', command=hex_to_den, bg='gray15', fg='white', relief='flat', width=9)
h_d_button.grid(row=0, column=2, padx=10, pady=10)

h_b_button = tk.Button(m_frame, text='Hex to Bin', command=hex_to_bin, bg='gray15', fg='white', relief='flat', width=9)
h_b_button.grid(row=1, column=0, padx=10, pady=10)

d_b_button = tk.Button(m_frame, text='Den to Bin', command=den_to_bin, bg='gray15', fg='white', relief='flat', width=9)
d_b_button.grid(row=1, column=1, padx=10, pady=10)

d_h_button = tk.Button(m_frame, text='Den to Hex', command=den_to_hex, bg='gray15', fg='white', relief='flat', width=9)
d_h_button.grid(row=1, column=2, padx=10, pady=10)

lb_kg_button = tk.Button(m_frame, text='lb to kg', command=lb_to_kg, bg='gray15', fg='white', relief='flat', width=9)
lb_kg_button.grid(row=2, column=0, padx=10, pady=10)

kg_lb_button = tk.Button(m_frame, text='kg to lb', command=kg_to_lb, bg='gray15', fg='white', relief='flat', width=9)
kg_lb_button.grid(row=3, column=0, padx=10, pady=10)

in_cm_button = tk.Button(m_frame, text='inch to cm', command=in_to_cm, bg='gray15', fg='white', relief='flat', width=9)
in_cm_button.grid(row=2, column=1, padx=10, pady=10)

cm_in_button = tk.Button(m_frame, text='cm to inch', command=cm_to_in, bg='gray15', fg='white', relief='flat', width=9)
cm_in_button.grid(row=3, column=1, padx=10, pady=10)

ft_m_button = tk.Button(m_frame, text='ft to m', command=ft_to_m, bg='gray15', fg='white', relief='flat', width=9)
ft_m_button.grid(row=2, column=2, padx=10, pady=10)

m_ft_button = tk.Button(m_frame, text='m to ft', command=m_to_ft, bg='gray15', fg='white', relief='flat', width=9)
m_ft_button.grid(row=3, column=2, padx=10, pady=10)

def change(a=0):
    root.config(bg = 'red' if a & 1 else 'green')
    root.after(400,change, a ^ 1 )

def special():
    textoutput('100100001100101011011000110110001101111001000000101011101101111011100100110110001100100')
    message = messagebox.askyesnocancel('???',f'Are you sure?')
    if message == True:
        change()
        textoutput('!!!')
    else:
        textoutput('Ok')

mystery_button = tk.Button(m_frame, text='???', command=special, bg='gray15', fg='gray30', relief='flat')
mystery_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky = 'WE')

#bottom frame -----------------------------------------------------------------------
b_frame = ttk.Frame(main_frame, style='TFrame')
b_frame.grid(row=2, column=0)

b_label = ttk.Label(b_frame, text='The converted answer is:')
b_label.grid(row=0, column=0, padx=5, pady=10)

convoutput = tk.Entry(b_frame, bg='gray30', fg='#8ab839', relief='sunken')
convoutput.grid(row=0, column=1, padx=5, pady=10)

#create window
root.mainloop()