import matplotlib.pyplot as plt
import math

x2 = []
xlogx = []
x = []
for i in range(1,10001):
    x.append(i)

for i in range(1,10001):
    x2.append(i*i)
    xlogx.append(i*math.log(i,10))

p1 = x2[9999]
p2 = xlogx[9999]


line1, = plt.plot(x2,color='red',label='x^2')
line2, = plt.plot(xlogx, color='blue',label='x*log(x)')
text_only, = plt.plot(0,0,color='white',label='Koncové hodnoty')
point1, = plt.plot(9999,p1,color='magenta', marker='o',label=str(p1))
point2, = plt.plot(9999,p2,color='cyan', marker='o',label=str(p2))
plt.legend(handles=[line1,line2,text_only,point1,point2])
plt.show()
