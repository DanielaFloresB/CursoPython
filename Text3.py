#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------
#Header
__author__ = "Daniela Flores"
__copyright__ = "Copyright 2007, ST Project"
__credits__ = ["Daniela Flores"]
__license__ = "GPL 2"
__version__ = "1.0.1"
__maintainer__ = "Dany"
__email__ = "hola@python.com"
__status__ =  "Debbug"
__execution__ = "python3 "

#------------------------------------- Codigo no mas ancho de 80 lineas---------
import random  
#-------------------------------------

def bitwase():
    """Change the value of the specific byte position of the list using logical
       operators and right-left shifts"""
    #List = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
    List = [0x0f,0x10, 0x11, 0xcb, 0x02, 0x0f,0x09, 0x11, 0xcb, 0x47,\
          0x20,0x12, 0x80, 0x18, 0x1c, 0x52,0x10, 0x15, 0x63, 0x1c]
    List1 = []
    List_and = []
    List_or = []
    List_xor = []
    List_ShiftL = []
    List_ShiftR = []
    List_ShiftLMask = []
    List_ShiftRMask = []
    

    #for _ in (List):
    #    print(_)

    print("Lista original")
    print(List)
    print(hex(List[0]), hex(List[3]))
    print(hex(List[19]))
    mask=0x0f   #Mascara para corrimiento
    print("Máscara = ", mask, "\n")

    for i in List:
        List1.append(hex(i))
        List_and.append(i and mask)
        List_or.append(i or mask)
        List_xor.append(i ^ mask)
        a = i
        b = i
        List_ShiftL.append(a<<1)
        List_ShiftR.append(b>>2)
        mask2 = mask<<3
        mask3 = mask>>2
        List_ShiftLMask.append(i or mask2)
        List_ShiftRMask.append(i ^ mask3)
        

    print(List1, "\n")
    print("Lista And")
    print(List_and, "\n")
    print("Lista Or")
    print(List_or, "\n")
    print("Lista Xor")
    print(List_xor, "\n")
    print("Lista Corrimiento izquierda")
    print(List_ShiftL, "\n")
    print("Lista Corrimiento derecha")
    print(List_ShiftR, "\n")

    print("Nueva máscara = ", mask2)
    print("Lista Corrimiento izquierda con mascara")
    print(List_ShiftLMask, "\n")
    print("Lista Corrimiento derecha con mascara")
    print(List_ShiftRMask)  

#-------------------------------------
#if __name__ == "__main__":
        
bitwase()

#-------------------------------------
