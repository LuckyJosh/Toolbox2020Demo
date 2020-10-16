import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1)

plt.plot(x, np.exp(x), 'r.')
plt.savefig('plot.pdf')
