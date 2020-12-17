from tkinter import *

top = Tk()
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()
intital_window_width = screen_width/2
intital_window_height = screen_height/2
top.geometry(f"{int(intital_window_width)}x{int(intital_window_height)}")


class App:
    def __init__(self):
        self.window_width = intital_window_width
        self.window_height = intital_window_height
        self.display_info_tab = 0
        self.buttoncanvas_width = intital_window_width
        self.slider1_val = 0

        self.topframe = Frame(top)
        self.scrollbar = Scrollbar(self.topframe, orient="vertical")
        self.buttoncanvas = Canvas(self.topframe)
        self.buttonlist = Frame(self.buttoncanvas, bg="#aeaeae")
        self.infotab = Frame(top, bg="#aeaeae")

        self.btn1 = Button(self.buttonlist, text="Device 1", command=lambda: self.button1press())
        self.btn2 = Button(self.buttonlist, text="Device 2")
        self.btn3 = Button(self.buttonlist, text="Device 3")
        self.btn4 = Button(self.buttonlist, text="Device 4")
        self.btn5 = Button(self.buttonlist, text="Device 5")
        self.btn6 = Button(self.buttonlist, text="Device 6")
        self.btn7 = Button(self.buttonlist, text="Device 7")

        self.scrollbar.config(command=self.buttoncanvas.yview)
        self.buttoncanvas.config(yscrollcommand = self.scrollbar.set)

    def _canvas_resize(self, event):
        self.window_width = event.width/2
        self.buttoncanvas.itemconfigure("text", width=self.window_width)
        self.buttoncanvas_width = self.window_width
        self.calldefault()


    def scroll(self, event):
        self.buttoncanvas.configure(scrollregion=self.buttoncanvas.bbox("all"))

    def calldefault(self):
        self.topframe.pack(expand=TRUE, fill=BOTH)
        self.buttoncanvas.pack(side=LEFT, expand=TRUE, fill=BOTH)
        self.scrollbar.pack(side=RIGHT, expand=FALSE, fill=Y, ipadx=10)
        self.buttonlist.pack(side=TOP, expand=TRUE, fill=BOTH)

        self.btn1.pack(side=TOP, expand=TRUE, fill=BOTH, ipady=self.window_height/5, ipadx=self.buttoncanvas_width)
        self.btn2.pack(side=TOP, expand=TRUE, fill=BOTH, ipady=self.window_height/5, ipadx=self.buttoncanvas_width)
        self.btn3.pack(side=TOP, expand=TRUE, fill=BOTH, ipady=self.window_height/5, ipadx=self.buttoncanvas_width)
        self.btn4.pack(side=TOP, expand=TRUE, fill=BOTH, ipady=self.window_height/5, ipadx=self.buttoncanvas_width)
        self.btn5.pack(side=TOP, expand=TRUE, fill=BOTH, ipady=self.window_height/5, ipadx=self.buttoncanvas_width)
        self.btn6.pack(side=TOP, expand=TRUE, fill=BOTH, ipady=self.window_height/5, ipadx=self.buttoncanvas_width)
        self.btn7.pack(side=TOP, expand=TRUE, fill=BOTH, ipady=self.window_height/5, ipadx=self.buttoncanvas_width)

        self.buttoncanvas.create_window((0, 0), window=self.buttonlist, anchor='nw')
        self.topframe.bind("<Configure>", self.scroll)
        self.buttoncanvas.bind("<Configure>", self._canvas_resize)

    def button1press(self):
        if self.display_info_tab == 1:
            self.infotab.destroy()
            self.calldefault()
            self.display_info_tab = 0

        else:
            self.display_info_tab = 1
            self.btn1.config(bg="#bfbfbf")
            self.resizebuttonlist()
        return

    def printscaleval(self):
        print(str(self.slider.get()))
        self.slider1_val = self.slider.get()
        return

    def resizebuttonlist(self):
        self.infotab = Frame(top, bg="#aeaeae")
        self.topframe.pack(side=LEFT, expand=TRUE, fill=BOTH)
        self.infotab.pack(side=RIGHT, expand=TRUE, fill=BOTH)
        top.update_idletasks()
        self.slider = Scale(self.infotab, sliderlength=self.infotab.winfo_height() / 4, width=self.infotab.winfo_width(),
                       showvalue=0, variable=self.slider1_val)

        self.applybutton = Button(self.infotab, text="Apply", command=lambda: self.printscaleval())

        self.slider.place(relx=0, rely=0, relwidth=1, relheight=0.9)
        self.applybutton.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

        self.slider.set(self.slider1_val)
        return


app = App()
app.calldefault()
top.mainloop()
