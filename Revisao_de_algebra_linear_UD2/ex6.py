import numpy as np


c1=input("Coloque o primeiro complexo: ")
c2=input("Coloque o segundo complexo: ")

c1=complex(c1)
c2=complex(c2)

print("|c1||c2|=",abs(c1)*abs(c2),"|c1 X c2|=",abs(c1*c2))

print("|c1 + c2|=",abs(c1+c2),"|c1|+|c2|",abs(c1)+abs(c2))