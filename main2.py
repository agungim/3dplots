# library
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import  seaborn as sns
import numpy as np

# Get the data (csv file is hosted on the web)
#url = 'https://python-graph-gallery.com/wp-content/uploads/volcano.csv'
#data = pd.read_csv(url)

DataAll= np.loadtxt("Table1.txt", delimiter=" ", skiprows=1,
                  usecols=[0,1,2])

df = pd.DataFrame(DataAll, columns = ['X','Y','Z'])

# Transform it to a long format
#df = data.unstack().reset_index()
#df.columns = ["X", "Y", "Z"]
print(df)

# And transform the old column name in something numeric
#df['X'] = pd.Categorical(df['X'])
#df['X'] = df['X'].cat.codes
#print(df['X'])
# Make the plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
ax.set_xlabel('$Temp(K)$', fontsize=10)
ax.set_ylabel('$eV$', fontsize=10)
ax.set_zlabel('$Sigma/time$', fontsize=10)
plt.show()

# to Add a color bar which maps values to colors.
surf = ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

# Rotate it
ax.view_init(30, 45)
plt.show()

# Other palette
ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.jet, linewidth=0.01)

plt.show()
