import webbrowser
from tkinter import * 
root = Tk()
root.title("DZ Easy go")
root.geometry('300x200')
def google():
    webbrowser.open("www.google.com")

mygoogle = Button(root,text='open google',command=google).pack(pady=20)
root.mainloop()