from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *


from Misc import *


class PopUpConfirmQuit(Toplevel):
    """A TopLevel popup that asks for confirmation that the user wants to quit.
                                                                              .
    Upon confirmation, the App is destroyed.
    If not, the popup closes and no further action is taken
    """
    def __init__(self, master=None):
        super().__init__(master)
        Label(self , text = "Are you sure you want to quit").pack()
        Button(self, text = 'Yes', command=master.destroy).pack(side=RIGHT, fill=BOTH, padx=5, pady=5)
        Button(self, text = 'No', command=self.destroy).pack(side=RIGHT, fill=BOTH, padx=5, pady=5)