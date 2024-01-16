from tkinter import *

# create main window
r = Tk()

# Define the size of the tkinter frame
r.geometry('310x300')
r.title('my title')
r.config(background='#fff')


# Adding labels to main windw
rn = Label(r, text='roll no.', highlightcolor='#000')
rn.place(x=20, y=20)

fn = Label(r, text='First Name', highlightcolor='#000')
fn.place(x=20, y=50)

ln = Label(r, text='Last Name', highlightcolor='#000')
ln.place(x=20, y=80)

en = Label(r, text='Email', highlightcolor='#000')
en.place(x=20, y=110)

# Adding fields to window
ern = Entry(r)
ern.place(x = 100, y = 20)

efn = Entry(r)
efn.place(x = 100, y = 50)

eln = Entry(r)
eln.place(x = 100, y = 80)

eem = Entry(r)
eem.place(x = 100, y = 110)

# mainloop method called
mainloop()