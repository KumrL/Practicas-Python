from customtkinter import *
from PIL import Image
from database import database

class main(CTk):
    def __init__(self):
        super().__init__()
        self.title("Notes")
        self.geometry('1000x500')
        self.left_section()
        self.right_section()
        self.resizable(0, 0)

    def left_section(self):
        self.left_frame = CTkFrame(self, fg_color= 'red')
        self.left_frame.place(relx= 0, rely= 0, relwidth= 0.3, relheight= 1)

        self.search= CTkEntry(self.left_frame, placeholder_text= "Search")
        self.search.pack(side= TOP, fill= X, padx= 10, pady= (10, 0))
        
        self.btns_frame = CTkFrame(self.left_frame, fg_color= "yellow")
        self.btns_frame.pack(side= TOP, fill= X, padx= 10, pady= (10, 0))

        trash_frame = CTkFrame(self.btns_frame, fg_color= "green")
        trash_frame.pack(pady= 1)

        img_create = CTkImage(Image.open("assets/create.png"), size= (25, 25))
        self.btn_create = CTkButton(trash_frame, text="", image= img_create, width= 15, fg_color= "transparent")
        self.btn_create.pack(side=LEFT, pady= 5)

        img_delete = CTkImage(Image.open("assets/delete.png"), size= (25, 25))
        self.btn_delete = CTkButton(trash_frame, text= "", image= img_delete, width= 15, fg_color= "transparent")
        self.btn_delete.pack(side= LEFT, padx= 10)

        self.scroll_frame = CTkScrollableFrame(self.left_frame, fg_color= 'pink')
        self.scroll_frame.pack(side= TOP, fill= BOTH, expand= TRUE, padx= 10, pady= (0, 10))

        def insert_text(text):
            self.text_container.delete(1.0, END)
            self.text_container.insert(1.0, text)

        db = database()
        for x in db.get_notes():
            note_btn = CTkButton(self.scroll_frame, text= x[1], command= lambda x=x: [insert_text(x[2])])
            note_btn.pack(pady= (0, 5), fill= X, padx= 5)

    def right_section(self):
        self.right_frame = CTkFrame(self, fg_color= 'blue')
        self.right_frame.place(relx= 0.3, rely= 0, relwidth= 0.7, relheight= 1)

        self.text_container = CTkTextbox(self.right_frame, activate_scrollbars= TRUE, wrap= WORD)
        self.text_container.pack(fill= BOTH, expand= TRUE, padx= 4, pady= 4)


app = main()
app.mainloop()