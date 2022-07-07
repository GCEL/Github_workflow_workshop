"""
A sample script for the GCEL Github workshop, July 2022
-------------------------------------------------------
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col

if len(sys.argv)>1:
    c = sys.argv[1]
else:
    c = 'seagreen'

if not col.is_color_like(c):
    print('warning: supplied colour not recognised, switching to default')
    c = 'seagreen'

x = np.arange(-4,4,0.01)*np.pi
y = np.sin(x)*np.cos(x**1.5)**2

fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(8,4))
ax.plot(x,y,'--',color=c)
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.tight_layout()
fig.savefig('updated_test.png')


