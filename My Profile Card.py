from tkinter import *

window = Tk()
window.title("My Profile Card")
window.geometry("400x380")

title = Label(window, text="My Profile Card", fg="white", bg="purple", width=40)
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

name_label = Label(window, text="Name:")
name_label.grid(row=1, column=0, padx=5, pady=5)

name_entry = Entry(window, fg='blue', bg='lightyellow', width=25)
name_entry.grid(row=1, column=1, padx=5, pady=5)

hobby_label = Label(window, text="Hobby:")
hobby_label.grid(row=2, column=0, padx=5, pady=5)

hobby_entry = Entry(window, fg='blue', bg='lightyellow', width=25)
hobby_entry.grid(row=2, column=1, padx=5, pady=5)

about_frame = Frame(window, relief="raised", borderwidth="2", width=300, height=100)
about_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

about_label = Label(about_frame, text="About Me:")
about_label.pack()

about_text = Text(about_frame, fg='green', bg='lightyellow', width=30, height=5)
about_text.pack()

submit_button = Button(window, text="Show my card", fg="purple", bg="green", width=10)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10) 
window.mainloop()
