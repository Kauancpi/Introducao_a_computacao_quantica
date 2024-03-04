import numpy as np

c1=input("Coloque o primeiro complexo: ")
c2=input("Coloque o segundo complexo: ")

c1=complex(c1)
c2=complex(c2)

print("conj(c1) + conj(c2)=",np.conj(c1)+np.conj(c2),"conj(c1 + c2)=",np.conj(c1+c2))

print("conj(c1) X conj(c2)=",np.conj(c1)*np.conj(c2),"conj(c1 x c2)=",np.conj(c1*c2))