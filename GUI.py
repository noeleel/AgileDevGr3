from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

from Misc import *


class main_window(Tk):
    def __init__(self):
        super().__init__()
        self.objectif = 0
        self.list = []
        self.document = "Groceries List.doc"
        self.Frame_1 = Frame(self, borderwidth=2, relief=GROOVE)
        self.Frame_2 = Frame(self, borderwidth=2, relief=GROOVE)
        self.Frame_3 = Frame(self, borderwidth=2, relief=GROOVE)
        
        
        self.Frame_1.pack(side=TOP)
        self.Frame_2.pack(side=TOP)
        self.Frame_3.pack(side = TOP)

        """self.menubar = Menu(self)
        self.filemenu = (self.menubar)
        self.filemenu.add_command(label = "Export",command = self.export)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Clear", command = self.clear)
        self.filemenu.add_command(label = "Quit",  command = self.quit)
        self.menubar.add_cascade(label = "File", menu = self.filemenu)"""

        self.label = Label(self.Frame_1,text = "Objectif: ")
        self.GUI_objectif = Entry(self.Frame_1)
        self.exit = Button(self.Frame_1, text="Quit", command=self.quit)

        self.bind('<Return>',self.get_objectif)

        self.label.grid(row = 1,column=3)
        self.GUI_objectif.grid(row = 1,column = 5)
        self.exit.grid(row = 1,column = 7)



        #self.label.pack()
        #self.GUI_objectif.pack()
        #self.exit.pack()

        #self.config(menu = self.menubar)
        


    
    def get_objectif(self,Event):
        self.objectif = str_to_float(self.GUI_objectif.get())
        if self.objectif ==-1:
            showwarning("Error","Please enter a number")
            self.GUI_objectif.delete(0,'end')
        else:
            self.show_list()

    
    def show_list(self):
        self.button_export = Button(self.Frame_3, text = "Export", command = self.export)
        self.button_export.grid()
        for i in range(len(self.list)):
            Label(self.Frame_2,text = List_days[i],width = 10).grid(row = 2,column = 3*i+1)

            Label(self.Frame_2,text = self.list[i][0],width = 10).grid(row = 3,column = 3*i+1)
            for j in range(len(self.list[i])-1):
                Label(self.Frame_2,text = "-",width = 10).grid(row = j+4,column = 3*i+1)
                Label(self.Frame_2,text = self.list[i][j+1],width = 10).grid(row = j+4,column = 3*i+2)

    def clear(self):
        pass

    def export(self):
        f = open(self.document,"w")
        for i in range(len(self.list)):
            f.write(List_days[i]+"\n")
            f.write("  "+self.list[i][0]+":\n")
            for j in range(len(self.list[i])-1):
                f.write("  ->"+self.list[i][j+1]+"\n")
            f.write("\n")
        f.close()