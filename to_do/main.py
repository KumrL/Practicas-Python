from customtkinter import *
import json

class main(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('500x600')
        self.resizable(0, 0)
        self.task_list = []
        self.check_list = []
        try:
            open('tasks.json', 'x')
            self.tasks = []
        except:
            with open('tasks.json') as tasks:
                try:
                    self.tasks = json.load(tasks)
                except:
                    self.tasks = []
        self.drawGui()

    def drawGui(self):
        def addTask(task):
            self.tasks.append({'task': task, 'state': False})
            with open('tasks.json', 'w') as tasks:
                json.dump(self.tasks, tasks, indent= 1)
                
        def refreshTaks():
            for x in self.task_list:
                x.destroy()
            for x in self.check_list:
                x.destroy()
            self.task_list.clear()
            self.check_list.clear()
            for x in self.tasks:
                task = CTkEntry(self.left_frame, height= 25)
                task.insert(0, x['task'])
                task.pack(padx= 5, pady= 4, fill= X)
                self.task_list.append(task)
                check = CTkCheckBox(self.right_frame, text= '', width= 1, height= 25)
                check.pack(pady= 4)
                self.check_list.append(check)

        self.top_frame = CTkScrollableFrame(self)
        self.top_frame.pack(fill= BOTH, expand= True, pady= (0, 40))

        self.left_frame = CTkFrame(self.top_frame, fg_color= 'transparent')
        self.left_frame.pack(side= LEFT, fill= BOTH, expand= TRUE)

        self.right_frame = CTkFrame(self.top_frame, fg_color= 'transparent')
        self.right_frame.pack(side= LEFT, fill= Y)

        for x in self.tasks:
            task = CTkEntry(self.left_frame, height= 25)
            task.insert(0, x['task'])
            task.pack(padx= 5, pady= 4, fill= X)
            self.task_list.append(task)
            check = CTkCheckBox(self.right_frame, text= '', width= 1, height= 25)
            check.pack(pady= 4)
            self.check_list.append(check)

        task_entry = CTkEntry(self, placeholder_text= 'New Task')
        task_entry.place(relx= 0.01, rely= 0.94, relwidth= 0.82, relheight= 0.05)
            
        create_btn = CTkButton(self, text= 'ADD', corner_radius= 50, command= lambda: [addTask(task_entry.get()), refreshTaks()])
        create_btn.place(relx= 0.84, rely= 0.94, relwidth= 0.15, relheight= 0.05)



app = main()
app.mainloop()