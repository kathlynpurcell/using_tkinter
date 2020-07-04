# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:14:06 2020

@author: kpurc
https://realpython.com/python-gui-tkinter/
https://effbot.org/tkinterbook/entry.html
https://www.delftstack.com/howto/python-tkinter/how-to-change-tkinter-button-color/
https://www.python-course.eu/tkinter_entry_widgets.php
"""

statement = "Hi from Tkinter!"

import tkinter as tk

window = tk.Tk()
window.configure(bg='white')

frame_a = tk.Frame()
greet_frame = tk.Frame()
name_frame = tk.Frame()

greeting = tk.Label(master=greet_frame, text=statement, fg ="white", bg="black", width='20', height='10')
#width and height by text units each the size of '0'
greeting.pack()


get_name = tk.Label(master=name_frame,text='Enter your name', fg='white', bg='#875bd1', width='20', height='3', font="Georgia")
get_name.pack()

entry = tk.Entry(master=name_frame, fg="white", bg='black', width='20', font="Georgia")
def callback(event):
    name = entry.get()
    your_name = tk.Label(master=name_frame, text=('Your name is '+name), bg="#b397e2", font="Georgia", width='20')
    your_name.pack()
entry.bind("<Return>", callback)
entry.pack()

'''
this is a little more complicated so the above way is better I think, but this still works
entry = tk.Entry(master=name_frame, fg="white", bg='black', width='20')
entry.pack()

def callback():
    name = entry.get()
    your_name = tk.Label(master=name_frame, text=('Your name is: '+name), bg="white")
    your_name.pack()


get = tk.Button(master=name_frame, text='Enter',command=callback, bg='white')
#get.configure(bg="yellow") #if you need to change the color
get.pack()
'''


name_frame.pack()

window.mainloop()

