import matplotlib.pyplot as plt
import numpy as np

N = 300
x = 2 * np.pi * np.random.rand(N)
y = 2 * np.random.rand(N)
area =  50 * y**2 #размер точек
colors = x

fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(x, y, c=colors, s=area, cmap='viridis', alpha=0.55, marker="*")

plt.show()