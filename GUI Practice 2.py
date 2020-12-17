from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("LEARNING IS FUN")



myimg = ImageTk.PhotoImage(Image.open("Octavius.png"))

mylabel = Label(image=myimg)
mylabel.pack()










button_quit = Button(root, text="Quit", command=root.quit)
button_quit.pack()



root.mainloop()







