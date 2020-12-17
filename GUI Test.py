from tkinter import *

top = Tk()
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()
top.geometry(f"{int(screen_width/2)}x{int(screen_height/2)}")


class App:
    def __init__(self):
        self.btn1_state = 0
        self.topframe = Frame(top)
        self.scrollbar = Scrollbar(self.topframe, orient="vertical")
        self.buttoncanvas = Canvas(self.topframe)
        #self.buttonlist = Frame(self.buttoncanvas, bg="#aeaeae")
        self.infotab = Frame(top, bg="#aeaeae")
        self.btn1 = Button(self.buttonlist, text="Device 1", command=lambda: self.button1press())
        self.btn2 = Button(self.buttonlist, text="Device 2")
        self.btn3 = Button(self.buttonlist, text="Device 3")
        self.btn4 = Button(self.buttonlist, text="Device 4")
        self.btn5 = Button(self.buttonlist, text="Device 5")
        self.btn6 = Button(self.buttonlist, text="Device 5")

        self.scrollbar.config(command=self.buttoncanvas.yview)
        self.buttoncanvas.configure(yscrollcommand = self.scrollbar.set)


    def button1press(self):
        if self.btn1_state == 1:
            self.infotab.destroy()
            top.update()
            self.calldefault()
            self.btn1_state = 0

        else:
            self.btn1_state = 1
            self.btn1.config(bg="#bfbfbf")
            self.resizebuttonlist()
        return

    def calldefault(self):
        self.topframe.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.buttoncanvas.place(relx=0, rely=0, relwidth=0.9, relheight=1)
        self.buttonlist.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.btn1.place(relx=0, rely=0, relwidth=1, height=400)
        self.btn2.place(relx=0, rely=0.2, relwidth=1, height=400)
        self.btn3.place(relx=0, rely=0.4, relwidth=1, height=400)
        self.btn4.place(relx=0, rely=0.6, relwidth=1, height=400)
        self.btn5.place(relx=0, rely=0.8, relwidth=1, height=400)
        self.btn6.place(relx=0, rely=0.8, relwidth=1, height=400)
        self.scrollbar.place(relx=0.9, rely=0, relwidth=.1, relheight=1)

    def resizebuttonlist(self):
        self.infotab = Frame(top, bg="#aeaeae")
        self.buttoncanvas.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        # self.buttonlist.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        self.infotab.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
        top.update_idletasks()
        slider = Scale(self.infotab, sliderlength=self.infotab.winfo_height() / 4, width=self.infotab.winfo_width(),
                       showvalue=0)
        slider.place(relx=0, rely=0, relwidth=1, relheight=1)
        print(self.infotab.winfo_width())
        return


app = App()
app.calldefault()
top.mainloop()
