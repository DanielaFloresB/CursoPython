#Interfaces graficas
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------
__author__ = "Daniela Flores"
__copyright__ = "Copyright 2007, ST Project"
__credits__ = ["Daniela Flores"]
__license__ = "GPL 2"
__version__ = "1.0.1"
__maintainer__ = "Dany"
__email__ = "hola@python.com"
__status__ =  "Debbug"
__execution__ = "python3 "

"""
#------------------------------------- Codigo no mas ancho de 80 lineas---------
import tkinter as tk
root = tk.Tk()

label = tk.Label(root, text="Hello World", padx=10, pady=10)
label.pack()

root.mainloop()
"""


#-------------------------------------------------------------------------------
#------------------------------------- Codigo no mas ancho de 80 lineas---------
import tkinter as tk
#-------------------------------------
class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.label = tk.Label(self, text="Hello World", padx=5, pady=5)
        self.label.pack()

#-------------------------------------
if __name__ == "__main__":
    root = Root()
    root.mainloop()
        

#-------------------------------------
