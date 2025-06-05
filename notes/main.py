from customtkinter import *
from PIL import Image
from database import database

class main(CTk):
    def __init__(self):
        super().__init__()
        set_default_color_theme("green")
        self.title("Notes")
        self.geometry('1000x500')
        self.db = database()
        self.left_section()
        self.right_section()
        self.resizable(0, 0)

    def left_section(self):
        self.left_frame = CTkFrame(self, corner_radius= 0)
        self.left_frame.place(relx= 0, rely= 0, relwidth= 0.3, relheight= 1)

        def searching(event, keys):
            for x in self.notes_list:
                x.pack_forget()
            resultado = list()
            keys = keys.lower()
            for x in self.notes_list:
                if keys in x.cget("text").lower():
                    resultado.append(x)
            for x in resultado:
                x.pack(pady= (0, 5), fill= X, padx= 5)

        self.search= CTkEntry(self.left_frame, placeholder_text= "Search")
        self.search.pack(side= TOP, fill= X, padx= 10, pady= (10, 0))
        self.search.bind("<KeyRelease>", lambda event: searching(event, self.search.get()))
        
        self.btns_frame = CTkFrame(self.left_frame, fg_color= "transparent")
        self.btns_frame.pack(side= TOP, fill= X, padx= 10, pady= (10, 0))

        trash_frame = CTkFrame(self.btns_frame)
        trash_frame.pack(pady= 1)

        def create_note():
            create_note_window = createNoteWindow(self)
            create_note_window.grab_set()
            self.wait_window(create_note_window)
            for x in self.notes_list:
                x.destroy()
            self.notes_list.clear()
            self.active_note_btn = None
            draw_btn_notes()
            self.note_id_control.set(0)
            self.text_container.delete(1.0, END)
        img_create = CTkImage(Image.open("assets/create.png"), size= (25, 25))
        self.btn_create = CTkButton(trash_frame, text="", image= img_create, width= 15, fg_color= "transparent", command= create_note, hover_color= "#00485a")
        self.btn_create.pack(side=LEFT, pady= 5)

        def delete_notes():
            self.db.delete_note(self.note_id_control.get())
            for x in self.notes_list:
                x.destroy()
            self.notes_list.clear()
            self.active_note_btn = None
            draw_btn_notes()
            self.note_id_control.set(0)
            self.text_container.delete(1.0, END)
        img_delete = CTkImage(Image.open("assets/delete.png"), size= (25, 25))
        self.btn_delete = CTkButton(trash_frame, text= "", image= img_delete, width= 15, fg_color= "transparent", command= delete_notes, hover_color= "#00485a")
        self.btn_delete.pack(side= LEFT, padx= 10)

        self.scroll_frame = CTkScrollableFrame(self.left_frame)
        self.scroll_frame.pack(side= TOP, fill= BOTH, expand= TRUE, padx= 10, pady= (0, 10))

        def insert_text(id):
            note = self.db.get_note(id)
            self.text_container.delete(1.0, END)
            self.text_container.insert(1.0, note)
        
        self.note_id_control = IntVar()
        self.notes_list = list()
        self.active_note_btn = None
        
        def disble_note(btn):
            if self.active_note_btn == None:
                self.active_note_btn = btn
                self.active_note_btn.configure(state= "disabled")
            elif self.active_note_btn != btn:
                self.active_note_btn.configure(state= "normal")
                self.active_note_btn = btn
                self.active_note_btn.configure(state= "disabled")
            
        def draw_btn_notes():
            for x in self.db.get_notes():
                note_btn = CTkButton(self.scroll_frame, text= x[1], font= ("Arial", 13, "bold"), fg_color= "#005f76", hover_color= "#00485a")
                note_btn.configure(command= lambda x=x, b= note_btn: [self.note_id_control.set(x[0]), insert_text(x[0]), disble_note(b)])
                note_btn.pack(pady= (0, 5), fill= X, padx= 5)
                self.notes_list.append(note_btn)
        draw_btn_notes()


    def right_section(self):
        self.right_frame = CTkFrame(self, corner_radius= 0)
        self.right_frame.place(relx= 0.3, rely= 0, relwidth= 0.7, relheight= 1)

        def update_note_db(event):
            note = self.text_container.get(1.0, END)
            id = self.note_id_control.get()
            self.db.update_note(id, note)

        self.text_container = CTkTextbox(self.right_frame, activate_scrollbars= TRUE, wrap= WORD, font= ("Arial", 15))
        self.text_container.pack(fill= BOTH, expand= TRUE, padx= 4, pady= 4)
        self.text_container.bind("<KeyRelease>", update_note_db)

class createNoteWindow(CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("400x150")
        self.resizable(0, 0)
        self.title("Create Note")
        self.db = database()

        def counter(event):
            text = self.name.get()
            if len(text) > 30:
                self.name.delete(0, END)
                self.name.insert(0, text[:75])
        self.name = CTkEntry(self, placeholder_text= "Max. 30")
        self.name.place(relx= 0.1, rely=0.2, relwidth= 0.8, relheight= 0.2)
        self.name.bind("<KeyRelease>", counter)

        self.cancel = CTkButton(self, text= "Cancel", command= self.destroy, hover_color= "#5a0000", fg_color= "#005f76")
        self.cancel.place(relx= 0.10, rely= 0.60, relwidth= 0.35, relheight= 0.2)

        self.accept = CTkButton(self, text= "Accept", hover_color= "#035a00", fg_color= "#005f76", command= lambda: [self.db.create_note(self.name.get()), self.destroy()])
        self.accept.place(relx= 0.55, rely= 0.6, relwidth= 0.35, relheight= 0.2)



app = main()
app.mainloop()