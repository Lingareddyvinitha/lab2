import matplotlib.pyplot as plt
import numpy as np
fs=8000
f1=5
sample=8000
x1=np.arange(sample)
y1=np.sin(2*np.pi*f1*x1/fs)
y2=np.sin((2*np.pi*f1*x1/fs)+180)
plt.subplot(311)
plt.title('Addition of two different phase signals')
plt.plot(x1,y1,'g')
plt.subplot(312)
plt.plot(x1,y2,'r')
plt.subplot(313)
plt.plot(x1,y1+y2,'y')
plt.show()
