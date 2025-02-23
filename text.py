from tkinter import *

window = Tk()
window.title('Application')
window.geometry('600x600')

greeting =Label(text='Welcome to my app', fg='green', bg='black')
greeting.pack()
e =Entry()
e.pack()
button =Button(text="click", fg='red')
button.pack()

label =Label(master=window, text='Thank you for registration')
label.pack()

window.mainloop()