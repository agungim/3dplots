# importing mplot3d toolkits, numpy and matplotlib
from mpl_toolkits import mplot3d
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
 
fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining all 3 axes
x = np.linspace(0, 20, 600)
z = sp.exp(-(3*x-20)**2)*np.sin(5 * x) 
y = sp.exp(-(3*x-20)**2)*np.cos(5 * x) 
#np.exp(-0.5*np.power(((x-0.5)/0.08), 2))
 
# plotting
ax.plot3D(x, y, z, 'green')
ax.set_title('3D line plot')
plt.show()