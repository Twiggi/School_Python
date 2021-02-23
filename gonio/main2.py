import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

numbers = []
name = "s19_original"

#for i in range(10,20):
# with open('C://Program Files (x86)//data//fft/'+str(name)+'.txt') as f:
#     numbers = numbers + f.readlines()

with open('C://Program Files (x86)//data//meranie//predMercury//Beh.csv') as f:
    numbers = numbers + f.readlines()

for i in range(0,len(numbers)):
    numbers[i] = numbers[i].strip()

numbers.pop(0)
for i in range(0,len(numbers)):
    numbers[i] = numbers[i].split(",")[1]#[2]

num = []
for k in numbers:
    num.append(float(k))
# for i in range(0,len(numbers)):
#     numbers[i] = numbers[i][0:4]
#numbers.sort()
yf2 = numbers[:250]
print(sum(num))
yf = fft(num)
yf1 = np.delete(yf,0)


plt.plot(yf1)
plt.show()
#plt.savefig(name)