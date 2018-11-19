from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *


from Misc import *
from GUI_exit_windows import *
from GUI_add_recipe import * 


class main_window(Tk):
    def __init__(self):
        super().__init__()
        self.current_weight = 0
        self.fat_percent = 0
        self.objectif = 0
        self.activity_factor = 0
        
        self.list = []
        self.document = "Groceries List.doc"
        self.Frame_1 = Frame(self, borderwidth=2, relief=GROOVE)
        self.Frame_2 = Frame(self, borderwidth=2, relief=GROOVE)
        self.Frame_3 = Frame(self, borderwidth=2, relief=GROOVE)
        
        
        self.Frame_1.pack(side=TOP)
        self.Frame_2.pack(side=TOP)
        self.Frame_3.pack(side = TOP)

        self.label_weight = Label(self.Frame_1,text = "Weight(kg): ")
        self.input_weight = Entry(self.Frame_1)

        self.label_fat = Label(self.Frame_1,text = "Fat percent: ")
        self.input_fat = Entry(self.Frame_1)


        self.varGr = StringVar()
        self.varGr.set(vals[1])
        for i in range(len(etiqs)):
            b = Radiobutton(self.Frame_2, variable=self.varGr, text=etiqs[i], value=vals[i])
            b.pack(side='top', expand=1, anchor = 'w')


        self.label_objectif = Label(self.Frame_1,text = "Objectif(kg): ")
        self.input_objectif = Entry(self.Frame_1)

        self.send_button = Button(self.Frame_1, text = "Send value" , command = self.send)
        self.add_recipe  = Button(self.Frame_1, text = "Add recipes", command = self.add)  
        self.exit = Button(self.Frame_1       , text="Quit"         , command=lambda: PopUpConfirmQuit(self))

        self.bind('<Return>',self.return_key)

        self.label_weight.grid(row = 1,column=3)
        self.input_weight.grid(row = 1,column = 5)

        self.label_fat.grid(row = 2,column=3)
        self.input_fat.grid(row = 2,column = 5)

        self.label_objectif.grid(row = 3,column=3)
        self.input_objectif.grid(row = 3,column = 5)

        self.send_button.grid(row = 1,column = 7)
        self.add_recipe.grid(row = 2, column = 7)
        self.exit.grid(row = 3,column = 7)

    def return_key(self,Event):
        self.get_objectif()

    def send(self):
        self.get_objectif()

    def get_objectif(self):
        self.current_weight = str_to_float(self.input_weight.get())
        self.activity_factor = str_to_float(self.varGr.get())
        self.fat_percent = str_to_float(self.input_fat.get())
        self.objectif = str_to_float(self.input_objectif.get())

        if (self.activity_factor * self.current_weight * self.objectif * self.fat_percent == 0):
            showwarning("Error","Please fill all boxes with number")
        else:
            pass
            print(self.activity_factor,self.current_weight,self.objectif,self.fat_percent)

    def add(self):
        add_recipe_windows(self)


if __name__ == "__main__":
    test = main_window()
    test.mainloop()