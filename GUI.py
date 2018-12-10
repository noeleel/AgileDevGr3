from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *


from Misc import *
from GUI_exit_windows import *
from GUI_add_recipe import * 

from subprocess import call

class main_window(Tk):
    def __init__(self):
        super().__init__()
        self.current_weight = 0
        self.fat_percent = 0
        self.objectif = 0
        self.activity_factor = 0
        
        self.list = []
        self.document = "List.md"
        self.Frame_1 = Frame(self, borderwidth=2, relief=GROOVE)
        self.Frame_2 = Frame(self, borderwidth=2, relief=GROOVE)
        self.Frame_3 = Frame(self, borderwidth=2, relief=GROOVE)
        self.Frame_4 = Frame(self, borderwidth=2, relief=GROOVE)
        
        
        self.Frame_1.pack(side = TOP)
        self.Frame_2.pack(side = TOP)
        self.Frame_3.pack(side = TOP)
        self.Frame_4.pack(side = TOP)

        self.label_weight = Label(self.Frame_1,text = "Weight(kg): ")
        self.input_weight = Entry(self.Frame_1)

        self.label_fat = Label(self.Frame_1,text = "Body Fat percent: ")
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
        self.exit = Button(self.Frame_1       , text = "Quit"       , command=lambda: PopUpConfirmQuit(self))

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
            showwarning("Error","Please fill all boxes with non-zero number")
        else:
            self.list = optimisation_lineaire(read_recipes(),self.objectif,1500)
            self.show_list()

    def add(self):
        add_recipe_windows(self)

    def show_list(self):
        self.button_export = Button(self.Frame_4, text = "Export", command = self.export)
        self.button_export.grid(row = 1,column = 1)
        max_len = max_lenght(self.list)+2
        for widget in self.Frame_3.winfo_children():
            widget.destroy()
        for i in range(len(self.list)):
            Label(self.Frame_3,text = List_days[i],width = 10).grid(row = 2,column = 4*i+1)
            cal_days = 0
            for j in range (len(self.list[i])):
                Label(self.Frame_3,text = List_meals[j] + ":",width = 10).grid(row = 3+j*max_len+1,column = 4*i+1)
                cal_days += self.list[i,j].calories
                Recipe = self.list[i,j]
                Label(self.Frame_3,text = Recipe.Name,width = 10).grid(row = 3+j*max_len+1,column = 4*i+2)
                Label(self.Frame_3,text = " ",width = 3).grid(row = 3+j*max_len+1,column = 4*i+3)
                for k in range(Recipe.NumberIngredients):
                    Label(self.Frame_3,text = " - ",width = 1).grid(row = 3+j*max_len+k+2,column = 4*i+1)
                    Label(self.Frame_3,text = Recipe.Ingredients[k].Name,width = 10).grid(row = 3+j*max_len+k+2,column = 4*i+2)
                Label(self.Frame_3,text = " ",width = 3).grid(row = 3+j*max_len+Recipe.NumberIngredients+2,column = 4*i+3)
            
            Label(self.Frame_3,text = "Calories : "+str(cal_days),width = 12).grid(row = 2,column = 4*i+2)

    def export(self):
        f = open(self.document,"w")
        f.write("# Groceries List for the week\n")
        for i in range(len(self.list)):
            f.write("## "+List_days[i]+"\n")
            for j in range (len(self.list[i])):
                f.write("### "+List_meals[j])
                Recipe = self.list[i,j]
                f.write(" : " + Recipe.Name + "\n")
                for k in range(Recipe.NumberIngredients):
                    f.write(" \n->" + str(Recipe.QTT[k])+" "+Recipe.Ingredients[k].Name + "\n")
                f.write("\n")
        f.close()
        print("export Done")
        call(["pandoc","-s","-o","Groceries_List.pdf","List.md"])
        print("Conversion Done")
        call(["rm","-f","List.md"])

