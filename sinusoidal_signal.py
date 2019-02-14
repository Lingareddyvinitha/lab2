import matplotlib.pyplot as plt
import numpy as np
fs1=8000
f1=5
sample=8000
x1=np.arange(sample)
y1=np.sin(2*np.pi*f1*x1/fs1)
plt.title('sinusoidal signal')
plt.plot(x1,y1)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()

