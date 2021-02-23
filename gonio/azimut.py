import numpy as np
import math
import time
import main

numbers=[]
name = "01"

# Data od 3 strany
#########################################################################################
# for i in range(1,61):
#     with open('C://Program Files (x86)//data//fft//basket//s'+str("{:02d}".format(i))+'.txt') as f:
#         numbers = numbers + f.readlines()
#
# for i in range(0,len(numbers)):
#     numbers[i] = numbers[i].strip()
#
# x = numbers.copy()
# y = numbers.copy()
#
# for i in range(0,len(numbers)):
#     x[i] = numbers[i].split(",")[6]
#
# for i in range(0,len(numbers)):
#     y[i] = numbers[i].split(",")[7]
#########################################################################################


# Moje namerane data
#########################################################################################
with open('C://Program Files (x86)//data//meranie//Rotacia_xmag_pociatoksever.csv') as f:
    numbers = numbers + f.readlines()

for i in range(0,len(numbers)):
    numbers[i] = numbers[i].strip()

x = numbers.copy()
y = numbers.copy()

for i in range(0,len(numbers)):
    x[i] = numbers[i].split(",")[1]
    y[i] = numbers[i].split(",")[2]

x.pop(0)
y.pop(0)

for i in range(len(x)):
    x[i] = -float(x[i])


#########################################################################################


final = []
triangle = []
JV = 0
JZ = 0
SZ = 0
SV = 0
J, S, V, Z = 0, 0, 0, 0
# triangle = float(x[12])/(math.sqrt(float(x[12])*float(x[12])+float(y[12])*float(y[12])))
#triangle = abs(float(x[0]))/(math.sqrt(abs(float(x[0]))*abs(float(x[0]))+abs(float(y[0]))*abs(float(y[0]))))


start = time.time()
for i in range(0,len(numbers)-10): #pocitam od osy y
    ############# ODKOMENTOVAT PRI ARKSIN ###############################################################
    # triangle.append(np.rad2deg(main.my_arcsin(abs(float(x[i]))/(math.sqrt(abs(float(x[i]))*abs(float(x[i]))+abs(float(y[i]))*abs(float(y[i])))))))
    ####################################################################################################
    # ARTAN
    if float(x[i]) == 0:
        if float(y[i]) < 0:
            V += 1
            triangle.append(90)
            # print("V")
            continue
        else:
            triangle.append(0)
            S += 1
            # print("S")
            continue
    else:
        triangle.append(np.rad2deg(main.my_atan(float(x[i])/float(y[i]))))

    if float(y[i])<0:
        triangle[i] = triangle[i] + 180
    elif float(x[i]) < 0 and float(y[i]) > 0:
        triangle[i] = triangle[i] + 360

    if triangle[i]> 337.25 or triangle[i]<22.5:
        S += 1
        print("S")
    elif triangle[i]<337.25 and triangle[i]> 292.5:
        SZ += 1
        print("SZ")
    elif triangle[i]<292.5 and triangle[i]> 247.5:
        Z += 1
        print("Z")
    elif triangle[i]<247.5 and triangle[i]> 202.5:
        JZ += 1
        print("JZ")
    elif triangle[i]<202.5 and triangle[i]> 157.5:
        J += 1
        print("J")
    elif triangle[i]<157.5 and triangle[i]> 112.5:
        JV += 1
        print("JV")
    elif triangle[i]<112.5 and triangle[i]> 67.5:
        V += 1
        print("V")
    elif triangle[i]<67.5 and triangle[i]> 22.5:
        SV += 1
        print("SV")

###########################################################################
# ARSIN




end = time.time()
for i in range(0,len(triangle)): #kontrolny vypis
    print(triangle[i])

#print("SV = " + str(SV) + ", JV = " + str(JV) + ", JZ = " + str(JZ) + ", SZ = " + str(SZ)) #pocet kvadrantov
print(str(end-start)) #cas




#vykreslovanie
# import matplotlib.pyplot as plt
# nula1, nula2 = [], []
# for i in range(-26,26):
#     nula1.append(i)
#     nula2.append(0)
# y_float = []
# for item in y:
#     y_float.append(float(item))
# x_float = []
# for item in x:
#     x_float.append(float(item))
# plt.plot(x_float,y_float)
# plt.plot(nula1,nula2,color='red')
# plt.axvline(x=0,color='red')
# plt.show()