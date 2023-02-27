import math

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 2)
y1 = 2 ** x
y2 = x
y3 = x**2
y4 = x ** 3
y5 = np.sqrt(x)
y6 = np.log10(x)


fig, ax = plt.subplots()

ax.plot(x, y1, linewidth=2.0)
ax.plot(x, y2, linewidth=2.0)
ax.plot(x, y3, linewidth=2.0)
ax.plot(x, y4, linewidth=2.0)
ax.plot(x, y5, linewidth=2.0)
ax.plot(x, y6, linewidth=2.0)



plt.show()

