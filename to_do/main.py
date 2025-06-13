from customtkinter import *
import json

class main(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('500x600')
        self.draw_gui()

    def draw_gui(self):
        create_btn = CTkButton(self, text= "ADD", corner_radius= 50)
        create_btn.place(relx= 0.84, rely= 0.94, relwidth= 0.15, relheight= 0.05)

app = main()
app.mainloop()