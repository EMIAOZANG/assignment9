import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
fig =plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.edgecolor=None
ax1.facecolor='g'
fig.grid=True
ax1.plot([1,2],[3,4])
plt.show()