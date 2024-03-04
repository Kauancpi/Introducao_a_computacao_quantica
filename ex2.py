import numpy as np
import cmath as cm

x=input("Coloque a potencia do i: ")
x=int(x)
if (x%4==0):
    print("i^",x,"=1")

if (x%4==1):
    print("i^",x,"=i")

if (x%4==2):
    print("i^",x,"=-1")
    
if (x%4==3):
    print("i^",x,"=-1")
    
