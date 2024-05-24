import numpy as np
import matplotlib.pyplot as plt

z1=2-1j
z2=1+1j


abs1=np.abs(z1)
abs2=np.abs(z2)
abs_soma=np.abs(z1+z2)
abs_diferenca=np.abs(z1-z2)

angle1=np.angle(z1)
angle2=np.angle(z2)
angle_soma=np.angle(z1+z2)
angle_diferenca=np.angle(z1-z2)



fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angle1, abs1,"g*")
ax.plot(angle2, abs2,"g*")
ax.plot(angle_soma, abs_soma,"r*")
ax.plot(angle_diferenca, abs_diferenca,"r*")

ax.text(angle1, abs1,"z1")
ax.text(angle2, abs2,"z2")
ax.text(angle_soma, abs_soma,"z1+z2")
ax.text(angle_diferenca, abs_diferenca,"z1-z2")

ax.set_rmax(3.2)
ax.set_rticks([1, 1.5, 2, 2.5, 3])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()