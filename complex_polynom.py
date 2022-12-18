import numpy as np
import matplotlib.pyplot as plt

minval = -5
maxval = 5
step = 0.01

xmin = -10
ymin = 10

xmax = 10
ymax = 10

r = minval - step

def fxn(z):
    return z**4 - 2*z**3 + 2*z**2 - z - 42

inputs = []
outputs = []
while r <= maxval:
    r += step
    c = minval - step
    while c <= maxval:
        c += step
        z = fxn(complex(r, c))
        inputs.append([r, c])
        outputs.append([z.real, z.imag])

inpus = np.asarray(inputs)
outputs = np.asarray(outputs)

plt.scatter(outputs[:,0], outputs[:,1], s=1)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.show()




