import customtkinter as ctk

class main_window():
    def __init__(self, window):
        self.window = window
        window.geometry("350x500")
        self.draw()

    def draw(self):
        self.numeros_var = ctk.StringVar()
        self.numeros = ctk.CTkEntry(self.window, font= ctk.CTkFont(size= 50), textvariable= self.numeros_var)
        self.numeros.pack(fill= 'x')

        frame_numeros = ctk.CTkFrame(self.window)
        frame_numeros.pack(fill= 'both', expand= True)
        
        for i in range(5):
            frame_numeros.rowconfigure(i, weight= 1, uniform= 'row')
        for i in range(4):
            frame_numeros.columnconfigure(i, weight= 1, uniform= 'column')

        bc= ctk.CTkButton(frame_numeros, text= 'CE', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.numeros_var.set(''))
        bc.grid(row= 0, column= 0, sticky= 'NSEW', columnspan= 2, padx= 1, pady= 1)
        bborrar= ctk.CTkButton(frame_numeros, text= '<--', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.borrar_ultimo_caracter())
        bborrar.grid(row= 0, column= 2, sticky= 'NSEW', columnspan= 2, padx= 1, pady= 1)
        b7= ctk.CTkButton(frame_numeros, text= '7', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('7'))
        b7.grid(row= 1, column= 0, sticky= 'NSEW', padx= 1, pady= 1)
        b6= ctk.CTkButton(frame_numeros, text= '6', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('6'))
        b6.grid(row= 1, column= 1, sticky= 'NSEW', padx= 1, pady= 1)
        b5= ctk.CTkButton(frame_numeros, text= '5', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('5'))
        b5.grid(row= 1, column= 2, sticky= 'NSEW', padx= 1, pady= 1)
        bx= ctk.CTkButton(frame_numeros, text= '*', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('*'))
        bx.grid(row= 1, column= 3, sticky= 'NSEW', padx= 1, pady= 1)
        b4= ctk.CTkButton(frame_numeros, text= '4', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('4'))
        b4.grid(row= 2, column= 0, sticky= 'NSEW', padx= 1, pady= 1)
        b5= ctk.CTkButton(frame_numeros, text= '5', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('5'))
        b5.grid(row= 2, column= 1, sticky= 'NSEW', padx= 1, pady= 1)
        b6= ctk.CTkButton(frame_numeros, text= '6', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('6'))
        b6.grid(row= 2, column= 2, sticky= 'NSEW', padx= 1, pady= 1)
        bmenos= ctk.CTkButton(frame_numeros, text= '-', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('-'))
        bmenos.grid(row= 2, column= 3, sticky= 'NSEW', padx= 1, pady= 1)
        b1= ctk.CTkButton(frame_numeros, text= '1', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('1'))
        b1.grid(row= 3, column= 0, sticky= 'NSEW', padx= 1, pady= 1)
        b2= ctk.CTkButton(frame_numeros, text= '2', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('2'))
        b2.grid(row= 3, column= 1, sticky= 'NSEW', padx= 1, pady= 1)
        b3= ctk.CTkButton(frame_numeros, text= '3', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('3'))
        b3.grid(row= 3, column= 2, sticky= 'NSEW', padx= 1, pady= 1)
        bmas= ctk.CTkButton(frame_numeros, text= '+', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('+'))
        bmas.grid(row= 3, column= 3, sticky= 'NSEW', padx= 1, pady= 1)
        b0= ctk.CTkButton(frame_numeros, text= '0', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('0'))
        b0.grid(row= 4, column= 0, sticky= 'NSEW', padx= 1, pady= 1)
        bpunto= ctk.CTkButton(frame_numeros, text= '.', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('.'))
        bpunto.grid(row= 4, column= 1, sticky= 'NSEW', padx= 1, pady= 1)
        bdiv= ctk.CTkButton(frame_numeros, text= '/', border_color= 'black', border_width= 2.5, corner_radius= 10, command= lambda: self.agregar_numero('/'))
        bdiv.grid(row= 4, column= 2, sticky= 'NSEW', padx= 1, pady= 1)
        bigual= ctk.CTkButton(frame_numeros, text= '=', border_color= 'black', border_width= 2.5, corner_radius= 10, command= self.calcular)
        bigual.grid(row= 4, column= 3, sticky= 'NSEW', padx= 1, pady= 1)

    def agregar_numero(self, numero):
        self.numeros.configure(state= 'normal')
        self.numeros.insert('end', numero)
        self.numeros.configure(state= 'readonly')
        self.numeros.xview_moveto(1)

    def borrar_ultimo_caracter(self):
        self.numeros_actual = self.numeros_var.get()

        if self.numeros_actual:
            self.numeros_var.set(self.numeros_actual[:-1])

    def calcular(self):
        try:
            expresion = self.numeros_var.get()
            self.resultado = eval(expresion)
            self.numeros.configure(state= 'normal')
            self.numeros.delete(0, 'end')
            self.numeros.insert(1, self.resultado)
            self.numeros.configure(state= 'readonly')
            self.numeros.xview_moveto(1)
        except:
            ventana = ctk.CTkToplevel()
            ventana.geometry('220x75')
            ventana.title("ERROR")
            
            ctk.CTkLabel(ventana, text= 'Error: mala expresión').pack()
            ctk.CTkButton(ventana, text="Cerrar", command=ventana.destroy).pack()
            ventana.focus_set()
            ventana.mainloop()
        



start_window = main_window(ctk.CTk())
start_window.window.mainloop()

#Kumar López