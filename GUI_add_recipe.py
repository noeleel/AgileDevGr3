from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *


from Misc import *
from GUI_exit_windows import *
from GUI_missing_ingredients import * 



class add_recipe_windows(Toplevel):
    def __init__(self,master = None):
        super().__init__(master)
        self.recipe_name = ""
        self.name_given = 0
        self.number_ingredients = 0
        self.recipe_list = []
        self.wm_title("Add Recipe")

        self.Frame_1 = Frame(self, borderwidth=2, relief=GROOVE)
        self.Frame_2 = Frame(self, borderwidth=2, relief=GROOVE)

        self.Frame_1.pack(side=TOP)
        self.Frame_2.pack(side=TOP)


        self.entry_l = Label(self.Frame_2,text = "Recipe_name")
        self.entry_e = Entry(self.Frame_2)
        

        self.send   = Button(self.Frame_2,text = "add",   command = self.add)
        self.cancel = Button(self.Frame_2, text='Cancel', command = lambda: PopUpConfirmQuit(self))
        self.done   = Button(self.Frame_2,text = "export",command = self.export)


        self.entry_l.grid(row = 1,column = 1)
        self.entry_e.grid(row = 1,column = 2)

        self.send.grid(row = 2,column = 1)
        self.cancel.grid(row = 2,column = 2)
        self.done.grid(row = 2,column = 3)


    def add(self):
        if self.name_given == 0:
            self.name_given = 1
            self.recipe_name = self.entry_e.get()
            self.recipe_list.append(self.recipe_name)
            Label(self.Frame_1,text = self.recipe_name).grid(row = self.number_ingredients,column = 1)
            self.entry_l['text'] = "Ingredients"
            print(self.name_given,self.recipe_name)
            self.number_ingredients+=1
        
        else:
            ingredients = self.entry_e.get()
            self.recipe_list.append(ingredients)
            Label(self.Frame_1,text = " - "+ingredients).grid(row = self.number_ingredients,column = 1)
            self.number_ingredients+=1
    
    def export(self):
        print(self.recipe_list)
        missing_ingredients(self.recipe_list[1],self)

    




if __name__ == "__main__":
    test = add_recipe_windows()  
    test.mainloop()
