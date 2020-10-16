import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1)

plt.plot(x, np.exp(x), 'r.')
plt.xlabel("$t$/Tage")
plt.ylabel("Coronafallzahlen")

plt.savefig('plot.pdf')
