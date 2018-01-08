# Coding archivo para que detecte los carácteres y el tipo de intérprete
# palabra reservada "append" para rellenar una lista (arreglo)
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

#-------------------------------------
import random  
#-------------------------------------
class myFirstClass():
    def __init__ (self):
        self.list1=[2,1,3,6,5,10,7,4,9,8]
        self.list2=[]
        self.a=5
        self.b=random.randint(1,10)

    def funct1(self):
        if (self.a == self.b):
            print(self.b)
            print("I'm a winner")
        else:
            print(self.b)
            print("I'm a looser")
        
    def funct2(self):
        for i in self.list1:
            self.list2.append(i)
            print(i)
        print(len(self.list1))
        print(len(self.list2))


        random.shuffle(self.list2)
        if (self.list2[3]==8):
            print("Correct")
        else:
            print("Fail")


#-------------------------------------
#
if __name__ == "__main__":
    t=myFirstClass()    #instanciacion de funcion -> herencia 
    t.funct1()          #acceder a funcion -> objeto
    t.funct2()

#-------------------------------------
