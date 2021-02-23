# numbers=[]
# name = "01"
#
# for i in range(1,61):
#     with open('C://Program Files (x86)//data//fft//basket//s'+str("{:02d}".format(i))+'.txt') as f:
#         numbers = numbers + f.readlines()
#
# # name = "s09_xacc"
# #
# # #for i in range(10,20):
# # with open('C://Program Files (x86)//data//fft/'+str(name)+'.txt') as f:
# #     numbers = numbers + f.readlines()
#
# for i in range(0,len(numbers)):
#     numbers[i] = numbers[i].strip()
#
# for i in range(0,len(numbers)):
#     numbers[i] = numbers[i].split(",")[0]
#
# numbers1 = numbers.copy()
# for i in range(0,len(numbers)):
#     numbers1[i] = float(numbers[i]) - 8
#
# suma = sum(numbers1)
# print(suma)
#
# for i in range(0,len(numbers)):
#     print(numbers[i])
def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j];

        list1.remove(max1);
        final_list.append(max1)

    return final_list

def Nminelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] < max1:
                max1 = list1[j];

        list1.remove(max1);
        final_list.append(max1)

    return final_list

import math

numbers = []
pocet_riadkov = []
i = 0

with open('C://Program Files (x86)//data//meranie//predMercury//saska chodza.csv') as f:
    numbers = numbers + f.readlines()


for i in range(0,len(numbers)):
    numbers[i] = numbers[i].strip()
    pocet_riadkov.append(i)

x = numbers.copy()
y = numbers.copy()

for i in range(0,len(numbers)):
    x[i] = numbers[i].split(",")[1]
    y[i] = numbers[i].split(",")[2]

x.pop(0)
y.pop(0)
pocet_riadkov.pop(len(pocet_riadkov) - 1)

rslt = 0
for i in range(0,len(x)):
    rslt += float(x[i])

print(str(rslt))

import matplotlib.pyplot as plt
from scipy.fftpack import fft

#xf = fft(x)

#plt.plot(pocet_riadkov,x)
#abc = [1.5,2.3,3.6,2,1]
x_float = []
for item in x:
    x_float.append(float(item))

y_float = []
for item in y:
    y_float.append(float(item))
#plt.plot(x_float,color='red')
N = 80
NY = 25
NY1 = 55
NY2 = 110
cumsum, moving_aves = [0], []
cumsumY, moving_avesY = [0], []
cumsumY1, moving_avesY1 = [0], []
cumsumY2, moving_avesY2 = [0], []
#klzavy pre x
for i, a in enumerate(x, 1):
    cumsum.append(cumsum[i-1] + float(a))
    if i>=N:
        moving_ave = (cumsum[i] - cumsum[i-N])/N
        moving_aves.append(moving_ave)

#klzavy pre y
for i, a in enumerate(y, 1):
    cumsumY.append(cumsumY[i-1] + float(a))
    if i>=NY:
        moving_ave = (cumsumY[i] - cumsumY[i-NY])/NY
        moving_avesY.append(moving_ave)
for i, a in enumerate(y, 1):
    cumsumY1.append(cumsumY[i-1] + float(a))
    if i>=NY1:
        moving_ave = (cumsumY1[i] - cumsumY1[i-NY1])/NY1
        moving_avesY1.append(moving_ave)
for i, a in enumerate(y, 1):
    cumsumY2.append(cumsumY2[i-1] + float(a))
    if i>=NY2:
        moving_ave = (cumsumY2[i] - cumsumY2[i-NY2])/NY2
        moving_avesY2.append(moving_ave)



moving_aves_float = []
moving_avesY_float1 = []
moving_avesY_float2 = []
for item in moving_aves:
    moving_aves_float.append(float(item))
moving_avesY_float = []
for item in moving_avesY:
    moving_avesY_float.append(float(item))
for item in moving_avesY1:
    moving_avesY_float1.append(float(item))
for item in moving_avesY2:
    moving_avesY_float2.append(float(item))
nula = moving_avesY_float.copy()
for i in range(0,len(nula)):
    nula[i] = 0
#plt.plot(moving_aves_float,color='red')
#avrgY, = plt.plot(moving_avesY_float[:1100],color='red',label='kĺzavý priemer pre N=25')
#avrgY1, = plt.plot(moving_avesY_float1[:1100],color='blue',label='kĺzavý priemer pre N=55')
#avrgY2, = plt.plot(moving_avesY_float2[:1100],color='magenta',label='kĺzavý priemer pre N=110')
osY, = plt.plot(y_float[:1500],color='blue',label = 'Acc v osi Y')
#osX, = plt.plot(x_float,color='red',label = 'Smer v osi X')
nula, = plt.plot(nula[:1500],color='orange', label='y=0')
plt.legend(handles=[nula,osY])

#plt.show()

#Hladanie maxim a detekovanie behu
usek = 400
useky = len(y_float)/usek
useky_int = int(useky)

for i in range(0,useky_int):
    tmpMAX = 0
    tmpMIN = 0
    MIN = 0
    MAX = 0
    maxValues = Nmaxelements(y_float[usek*i:usek*(i+1)],5)
    minValues = Nminelements(y_float[usek*i:usek*(i+1)],5)

    for j in range(0,len(minValues)):
        if minValues[j] < -2:
            tmpMIN += 1
            if tmpMIN == 3:
                MIN = 1
                break

    for j in range(0,len(maxValues)):
        if maxValues[j] > 1.5:
            tmpMAX += 1
            if tmpMAX == 3:
                MAX = 1
                break
    if MAX == 1 and MIN == 1:
        print("BEH V USEKU CISLO " + str(i))

################################################
#Priesecniky nulou (frekvencia vln)

for i in range(0,useky_int):
    priesecnik = 0
    jeden_usek = y_float[usek*i:usek*(i+1)]
    for j in range(0, len(jeden_usek)-1):
        if jeden_usek[j] < 0 and jeden_usek[j+1] > 0:
            priesecnik += 1
        if jeden_usek[j] > 0 and jeden_usek[j+1] < 0:
            priesecnik += 1

    print(str(priesecnik))

################################################
#Vertikalne ciary

# for xc in range(0,useky_int+1):
#     plt.axvline(x=400*xc,color='red')
plt.show()


# rslt = []
# for i in range(0,len(moving_aves_float)):
#     if i > 0:
#         if moving_aves_float[i] > moving_aves_float[i-1]:
#             rslt.append(math.sqrt(moving_aves_float[i]*moving_aves_float[i]+moving_avesY_float[i]*moving_avesY_float[i]))
#         else:
#             rslt.append((-1)*math.sqrt(moving_aves_float[i] * moving_aves_float[i] + moving_avesY_float[i] * moving_avesY_float[i]))
#     else:
#         rslt.append(math.sqrt(moving_aves_float[i] * moving_aves_float[i] + moving_avesY_float[i] * moving_avesY_float[i]))
#
# Nrslt = 200
# c, m = [0], []
# for i, a in enumerate(rslt, 1):
#     c.append(c[i-1] + float(a))
#     if i>=N:
#         moving_ave = (c[i] - c[i-Nrslt])/Nrslt
#         #can do stuff with moving_ave here
#         m.append(moving_ave)
#
# # plt.plot(m)
# # plt.show()
#
# velocity = [0]
# time = 1/205
# for acc in m:
#     velocity.append(velocity[-1] + acc * time)
# del velocity[0]
# plt.plot(m,color='green')
# plt.plot(velocity,color='red')
# plt.show()