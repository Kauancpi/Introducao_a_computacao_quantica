import numpy as np
import cmath as cm

c1=input("Coloque o primeiro complexo: ")
c2=input("Coloque o segundo complexo: ")
c3=input("Coloque o tercero complexo: ")

c1=complex(c1)
c2=complex(c2)
c3=complex(c3)

print("Comutatividade:")
print("c1+c2=",c1+c2,"c2+c1=",c2+c1)

print("Associatividade:")
print("(c1+c2)+c3=",(c1+c2)+c3,"c1+(c2+c3)",c1+(c2+c3))
print("(c1 X c2) X c3=",(c1*c2)*c3,"c1 X (c2Xc3)=",c1*(c2*c3))

print("Distributividade")
print("c1 X  (c2 + c3)=",c1*(c2+c3),"(c1 X c2) + (c1 X c3)=",(c1*c2)+(c1*c3))