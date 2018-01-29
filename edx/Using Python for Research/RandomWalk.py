#RadomWalk
import numpy as np
import matplotlib.pyplot as plt

X_0 = np.array([[0],[0]])

delta_X = np.random.normal(0, 1, (2,10000))
X = np.cumsum(delta_X, axis = 1)
X = np.concatenate((X_0, X), axis=1)

plt.plot(X[0], X[1], 'ro-',markersize = 3)
plt.savefig('randwalk.pdf')