import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#DataAll1D = np.loadtxt("datacsv_1d.csv", delimiter=",")

DataAll1D= np.loadtxt("Table1.txt", delimiter=" ", skiprows=0,
                  usecols=[0,1,2])


# create 2d x,y grid (both X and Y will be 2d)
X, Y = np.meshgrid(DataAll1D[:,0], DataAll1D[:,1])

# repeat Z to make it a 2d grid
Z = np.tile(DataAll1D[:,2], (len(DataAll1D[:,2]), 1))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='ocean')

plt.show()