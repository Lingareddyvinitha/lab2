import matplotlib.pyplot as plt
import numpy as np
fs1=8000
f1=5
fs=10000
f=100
sample=8000
x1=np.arange(sample)
y1=np.sin(2*np.pi*f1*x1/fs)
x2=np.arange(sample)
y2=np.sin(2*np.pi*f*x2/fs)
plt.subplot(311)
plt.title('Addition of two different frequencies')
plt.plot(x1,y1,'g')
plt.subplot(312)
plt.plot(x2,y2,'r')
plt.subplot(313)
plt.plot(x1+x2,y1+y2,'y')
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()
