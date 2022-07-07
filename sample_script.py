"""
A sample script for the GCEL Github workshop, July 2022
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-4,4,0.1)*np.pi
y = np.sin(x)*np.cos(x)**2

fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(6,4))
ax.plot(x,y,'-',color='seagreen')
fig.show()

