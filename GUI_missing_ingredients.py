from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *


from Misc import *
from GUI_exit_windows import *

class missing_ingredients(Toplevel):
    def __init__(self,ingredients,master = None):
        super().__init__(master)
        self.master = master
        #for 100g->cal,fat,carbohydrate,protein
        self.protocol("WM_DELETE_WINDOW", master.destroy)
        self.cancel  = Button(self, text='Cancel'  , command=lambda: PopUpConfirmQuit(self))
        self.confirm = Button(self, text ='Confirm', command = self.get_values) 

        self.wm_title("Missing Ingredients(WIP)")

        self.Label = Label(self,text = "Nutritionnal Values for 100g of " + str(ingredients))

        self.cal_l = Label(self,text = "Calories : ")
        self.cal_e = Entry(self)

        self.fat_l = Label(self,text = "Fat : ")
        self.fat_e = Entry(self)

        self.car_l = Label(self,text = "Carbs : ")
        self.car_e = Entry(self)

        self.pro_l = Label(self,text = "Protein : ")
        self.pro_e = Entry(self)

        self.Label.grid(row = 1,column = 1,columnspan = 4)

        self.cal_l.grid(row = 2,column = 1,columnspan = 2)
        self.cal_e.grid(row = 2,column = 3,columnspan = 2)
        
        self.fat_l.grid(row = 3,column = 1,columnspan = 2)
        self.fat_e.grid(row = 3,column = 3,columnspan = 2)
        
        self.car_l.grid(row = 4,column = 1,columnspan = 2)
        self.car_e.grid(row = 4,column = 3,columnspan = 2)
        
        self.pro_l.grid(row = 5,column = 1,columnspan = 2)
        self.pro_e.grid(row = 5,column = 3,columnspan = 2)

        self.cancel.grid( row = 6,column = 1,columnspan = 2)
        self.confirm.grid(row = 6,column = 3,columnspan = 2)

    def get_values(self):
        cal = str_to_float(self.cal_e.get())
        fat = str_to_float(self.fat_e.get())
        car = str_to_float(self.car_e.get())
        pro = str_to_float(self.pro_e.get())
        if cal*fat*car*pro == 0 :
            showwarning("Error","Please fill all boxes with number")
        else:
            #Update database
            print(cal,fat,car,pro)
            self.master.export()
            self.destroy()
