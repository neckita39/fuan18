import numpy as np
import matplotlib.pyplot as plt
import warnings
#warnings.filterwarnings('ignore')
Napr=7
x0 = lambda t: t
F = lambda t, f=x0:  t + np.sin(f(t)/np.pi)*np.sin(f(t)/np.pi)
Fi = F
Fi = lambda t, Fi=Fi: F(t, Fi)

for i in range(0, Napr):
    Fi = lambda t, Fi=Fi: F(t, Fi)




x = np.linspace(-4*np.pi, 4*np.pi, 100)

plt.plot(x, Fi(x))
plt.show()