import tkinter


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# LABEL
my_label = tkinter.Label(text="I am a Label!", font=("Arial", 24, "bold"))
my_label.pack(side="left")



# End
window.mainloop()