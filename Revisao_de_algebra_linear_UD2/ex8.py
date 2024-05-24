import numpy as np
import matplotlib.pyplot as plt

z1=2-1j
z2=1+1j

x1=z1.real
y1=z1.imag

x2=z2.real
y2=z2.imag

plt.plot(x1,y1,'-g*')
plt.text(x1,y1+0.05,"z1")
plt.plot(x2,y2,'g*')
plt.text(x2,y2+0.05,"z2")
plt.plot(x1+x2,y1+y2,'r*')
plt.text(x1+x2,y1+y2+0.05,"z1+z2")
plt.plot(x1-x2,y1-y2,'r*')
plt.text(x1-x2,y1-y2+0.05,"z1-z2")
plt.xlabel("Real")
plt.ylabel("Imag")

plt.show()