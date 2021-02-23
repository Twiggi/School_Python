import math
import os
import numpy as np
import cv2


# image = cv2.imread('C://Users/vizva/OneDrive/Dokumenty/GitHub/biometria/images/001/1/001_1_1.bmp')
# #image = cv2.imread('C://Users/vizva/OneDrive/Dokumenty/GitHub/biometria/images/008/2/008_2_2.bmp')
# output = image.copy()
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # cv2.imshow('image',image)
#
#
# image = cv2.GaussianBlur(image, (9, 9), 2)
# # image=cv2.equalizeHist(image)
# #cv2.imshow('image', image)
# #image = cv2.Canny(image,40,40)
# #WORKING SMALL CIRCLE below
# #circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 0.9, 280/8,2,100,50,1,100)#cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 10, 0.5,param1=20,param2=1,minRadius=150)#cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1.4, 1,0.1,param1=60,param2=50,minRadius=140) #cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 0.9, 280/8,2,100,50,1,100)
#
#
# circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 2, 150, param1=100, param2=10, minRadius=150)     #upper and lower "working"  ???????????
# tmp = 0
# tmp2 = 0
# # print(np.size(image, 1))
# width = np.size(image, 1)
# circlesN = np.zeros(shape=(2,3))
# if circles is not None:
#     # convert the (x, y) coordinates and radius of the circles to integers
#     circles = np.round(circles[0, :]).astype("int")
#     # loop over the (x, y) coordinates and radius of the circles
#     for (x, y, r) in circles:
#         print(x)
#         if x < width / 2 + 35 and x > width / 2 - 35:
#             circlesN[tmp2]=(np.copy(circles[tmp]))
#             tmp2+=1
#         else:
#             np.delete(circles,tmp)
#         tmp+=1
#
# # ensure at least some circles were found
# if circlesN is not None:
#     # convert the (x, y) coordinates and radius of the circles to integers
#     circlesN = circlesN.astype("int")
#     # loop over the (x, y) coordinates and radius of the circles
#     for (x, y, r) in circlesN:
#         #print(x)
#         # draw the circle in the output image, then draw a rectangle
#         # corresponding to the center of the circle
#         cv2.circle(output, (x, y), r, (0, 255, 0), 4)
#         cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
#
# circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1.5, 280/8,1,100,50,1)
# #circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 0.9, 280/8,2,100,50,1,100)    #small circle working
#
# # ensure at least some circles were found
# if circles is not None:
# 	# convert the (x, y) coordinates and radius of the circles to integers
# 	circles = np.round(circles[0, :]).astype("int")
#
# 	# loop over the (x, y) coordinates and radius of the circles
# 	for (x, y, r) in circles:
# 		# draw the circle in the output image, then draw a rectangle
# 		# corresponding to the center of the circle
# 		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
# 		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
#
#
# circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 250, 0.1, param1=30, param2=1, minRadius=70, maxRadius=120)    #big circle
#
# # ensure at least some circles were found
# if circles is not None:
# 	# convert the (x, y) coordinates and radius of the circles to integers
# 	circles = np.round(circles[0, :]).astype("int")
#
# 	# loop over the (x, y) coordinates and radius of the circles
# 	for (x, y, r) in circles:
# 		# draw the circle in the output image, then draw a rectangle
# 		# corresponding to the center of the circle
# 		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
# 		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
#


#cv2.imshow('output', output)
#cv2.waitKey(0)


def lowestDist(circles, small):
    smallestDist = 99999999
    smallestPoint = (9999,9999,9999)
    for (x,y,r) in circles:
        if x == 0 and y == 0: continue
        dist = math.hypot(y - small[0][1], x - small[0][0])
        if dist < smallestDist:
            smallestPoint = (x,y,r)
            smallestDist = dist
    return smallestPoint

def closestorig(circles, small):
    smallestDist = 99999999
    smallestPoint = (9999,9999,9999)
    for (x,y,r) in circles:
        if x == 0 and y == 0: continue
        dist = math.hypot(y - small[1], x - small[0])
        if dist < smallestDist:
            smallestPoint = (x,y,r)
            smallestDist = dist
    return smallestPoint

def closest(circles, small):
    smallestDist = 99999999
    smallestPoint = (9999,9999,9999)
    numbersX = [small[0]]
    numbersY = [small[1]]
    numbersR = [210]
    for (x,y,r) in circles:
        if x == 0 and y == 0: continue
        dist = math.hypot(y - small[1], x - small[0])
        if dist< 2:
            if dist < smallestDist:
                smallestPoint = (x,y,r)
                smallestDist = dist

            numbersX.append(int(x))
            numbersY.append(int(y))
            numbersR.append(int(r))
        if dist < smallestDist:
            smallestPoint = (x,y,r)
            smallestDist = dist
    return (aver(numbersX),aver(numbersY),aver(numbersR))#smallestPoint

def aver(numbers):
    total=0
    tmp=0
    for value in numbers:
        total += value
        tmp+=1
    return total/tmp

def fnc(imagepath):
    image = cv2.imread(imagepath)
    name = imagepath[-11:]#11
    output = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('image',image)


    image = cv2.GaussianBlur(image, (5, 5), 25)
    # image=cv2.equalizeHist(image)
    #cv2.imshow('image', image)
    #image = cv2.Canny(image,40,40)
    #WORKING SMALL CIRCLE below
    #circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 0.9, 280/8,2,100,50,1,100)#cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 10, 0.5,param1=20,param2=1,minRadius=150)#cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1.4, 1,0.1,param1=60,param2=50,minRadius=140) #cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 0.9, 280/8,2,100,50,1,100)

    #imageX = cv2.Canny(image,40,40)
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 30, param1=10, param2=10, minRadius=150)     #upper and lower "working"  ???????????
    tmp = 0
    tmp2 = 0
    # print(np.size(image, 1))
    width = np.size(image, 1)
    circlesN = np.zeros(shape=(2,3))
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            #print(x)
            if x < width / 2 + 35 and x > width / 2 - 35:
                circlesN[tmp2]=(np.copy(circles[tmp]))
                tmp2+=1
            else:
                np.delete(circles,tmp)
            tmp+=1

    # ensure at least some circles were found
    if circlesN is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circlesN = circlesN.astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circlesN:
            #print(x)
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)


    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 0.9, 280/8,2,100,50,1,100)    #small circle working

    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)


    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 250, 0.1, param1=30, param2=1, minRadius=70, maxRadius=120)    #big circle

    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)



    #cv2.imshow('output', output)
    #cv2.waitKey(0)

    from PIL import Image
    im = Image.fromarray(output)
    im.save('C://BIOM/output/' +name)

from PIL import Image, ImageOps

def ellipseFunction(image, output):
    img=image
    img_res=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    image = cv2.GaussianBlur(image, (5, 5), 3)
    image=cv2.equalizeHist(image)
    #nzs = cv2.Canny(image,45,45)
    nzs = cv2.Canny(image,100,150)
    nzs=cv2.findNonZero(nzs)
    #calling fitEllipse on the non zeros
    ellipse=cv2.fitEllipse(nzs) #ellipse[0]=(x,y).....ellipse[1]=(sirka,vyska)
    # ellipseA = ellipse
    # if smallC[0]-10<width/2:
    #     ellipseA=((ellipse[0][0]-40,ellipse[0][1]+15),(ellipse[1][0]-20,300),ellipse[2])
    # if smallC[0]+10>width/2:
    #     ellipseA=((ellipse[0][0]+40,ellipse[0][1]+15),(ellipse[1][0]-20,300),ellipse[2])
    # else:
    ellipseA=((ellipse[0][0],ellipse[0][1]+15),(ellipse[1][0],300),ellipse[2])
    #drawing the found ellipse
    #img_res=cv2.ellipse(img_res,ellipseA,(0,0,255),thickness=3)
    return cv2.ellipse(output,ellipseA,(0,0,255),thickness=3)

def fnc2(imagepath):
    import cv2

    image = cv2.imread(imagepath)
    #image = cv2.imread('path')
    name = imagepath[-11:]#11

    # cv2.imshow('image',image)
    bordersize=70
    image=cv2.copyMakeBorder(image, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize, borderType= cv2.BORDER_CONSTANT, value=[255,255,255] )
    output = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image = cv2.GaussianBlur(image, (5, 5), 15)
    # image=cv2.equalizeHist(image)
    #cv2.imshow('image', image)
    #image = cv2.Canny(image,40,40)
    #WORKING SMALL CIRCLE below
    #circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 0.9, 280/8,2,100,50,1,100)#cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 10, 0.5,param1=20,param2=1,minRadius=150)#cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1.4, 1,0.1,param1=60,param2=50,minRadius=140) #cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 0.9, 280/8,2,100,50,1,100)

    import numpy as np
    from PIL import Image
    from matplotlib import pyplot as plt
    tmp = 0
    tmp2 = 0
    #imageBIG = cv2.imread('file')
    #imageBIG = cv2.copyMakeBorder(imageBIG,300,300,0,0,cv2.BORDER_CONSTANT,)
    #imageBIG = cv2.cvtColor(imageBIG, cv2.COLOR_BGR2GRAY)
    #imageBIG[160:160+image.shape[0], 0:0+image.shape[1]] = image
    #cv2.imshow('test',imageBIG)
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 2,param1=10,param2=40, minRadius=180)     #upper and lower "working"  ???????????

    ####LOWER UPPER CIRCLE
    width = np.size(image, 1)
    height = np.size(image, 0)
    circlesN = np.zeros(shape=(500,3))
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            #print(x)
            if x < width / 2 + 25 and x > width / 2 - 25 and (y < height/2-30 or y > height/2+30):
                circlesN[tmp2]=(np.copy(circles[tmp]))
                tmp2+=1
            else:
                np.delete(circles,tmp)
            tmp+=1
    circlesNup = closest(circlesN,(230,105))
    circlesNdown = closest(circlesN,(230,335))
    circlesNa = np.zeros(shape=(2,3))
    circlesNa[0]=(np.copy(circlesNup))
    circlesNa[1]=(np.copy(circlesNdown))
    # ensure at least some circles were found
    # if circlesN is not None:
    #     # convert the (x, y) coordinates and radius of the circles to integers
    #     circlesN = circlesN.astype("int")
    #     # loop over the (x, y) coordinates and radius of the circles
    #     for (x, y, r) in circlesN:
    #         #print(x)
    #         # draw the circle in the output image, then draw a rectangle
    #         # corresponding to the center of the circle
    #         cv2.circle(output, (x, y), r, (0, 255, 0), 4)                                  #UNCOMMENT THIS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #         cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    #         a=2

    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1.5, 280/8,1,100,50,1 , maxRadius=70)
    #circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 0.9, 280/8,2,30,50,1,100)    #small circle working
    height = np.size(image, 0)
    tmp=0
    tmp2=0
    radius = 0
    circlesN = np.zeros(shape=(1,3))
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            #print(x)
            if x < width/2  + 45 and x > width / 2 - 45 and y < height/2  + 40 and y > height / 2 - 40 and image[y,x]<65 and image[y,x]>15:
                if radius<r:
                    circlesN[0]=(np.copy(circles[tmp]))
                    tmp2+=1
                    radius=r
            else:
                np.delete(circles,tmp)
            tmp+=1
    small = circlesN
    outfile = ""
    # ensure at least some circles were found
    if circlesN is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circlesN = np.round(circlesN[0, :]).astype("int")
        outfile += np.array2string(circlesN, separator=',',suppress_small=True) + '\n'
        # loop over the (x, y) coordinates and radius of the circles
        #for (x, y, r) in circlesN:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
        cv2.circle(output, (circlesN[0], circlesN[1]), circlesN[2], (0, 255, 0), 4)
        cv2.rectangle(output, (circlesN[0] - 5, circlesN[1] - 5), (circlesN[0] + 5, circlesN[1] + 5), (0, 128, 255), -1)
    smallC = circlesN


    #output = ellipseFunction(image, output)                                                                                    ############### ELIPSA

    #im = Image.fromarray(img_res)
    #im.save('imagepath'+name)
    ##x,y = circles[0][0],circles[0][1]
    #r, g, b = image.getpixel((x,y))
    #print(r, g, b)
    ##print(image[x,y])

    height = np.size(image, 0)

    #circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 3.0, 50,2,20,1, minRadius=75)
    #circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 3, 280/8,5,100,20, minRadius=75)
    #circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 3, 100,param1=40,param2=160, minRadius=75) #lukasM
    #circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 3, 1,2,40,5, minRadius=80, maxRadius=120)
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 3, 1, param1=30, param2=135, minRadius=85, maxRadius=120)
    #circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 230, 0.1, param1=15, param2=1, minRadius=70, maxRadius=120)    #big circle

    #odtialto dole big circle
    tmp=0
    tmp2=0
    radius = 0
    circlesN = np.zeros(shape=(500,3))
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            #print(x)
            if x < smallC[0]+smallC[2]/2-4 and x > smallC[0]-smallC[2]/2-4 and y < smallC[1]+smallC[2]/2-4 and y > smallC[1]-smallC[2]/2-4: #and image[x,y]<55 and image[x,y]>20:
                if radius<r:
                    circlesN[tmp2]=(np.copy(circles[tmp]))
                    tmp2+=1
                    radius=r
            else:
                np.delete(circles,tmp)
            tmp+=1
    circlesN = lowestDist(circlesN,small)
    # ensure at least some circles were found
    if circlesN is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circlesN = np.round(circlesN[:]).astype("int")
        outfile += np.array2string(circlesN, separator=',',suppress_small=True) + '\n'
        # loop over the (x, y) coordinates and radius of the circles
        #for (x, y, r) in circlesN:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
        cv2.circle(output, (circlesN[0], circlesN[1]), circlesN[2], (0, 255, 0), 4)
        cv2.rectangle(output, (circlesN[0] - 5, circlesN[1] - 5), (circlesN[0] + 5, circlesN[1] + 5), (0, 128, 255), -1)

    import math
    # diff= - circlesNa[0][1] + smallC[1] + smallC[2] #- circlesNa[0][2]
    # if diff>0:
    #     circlesNa[0][2] = 1.5*diff
    # if diff<0:
    #     circlesNa[0][2] = 1.5*diff
    if circlesNa is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circlesNa = circlesNa.astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circlesNa:
            #print(x)
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)                                  #UNCOMMENT THIS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            a=2
    outfile += np.array2string(circlesNa, separator=',',suppress_small=True) + '\n'
    #cv2.imshow('output', output)
    #cv2.waitKey(0)

    from PIL import Image
    im = Image.fromarray(output)
    im.save('C://BIOM/output/' +name)


    with open('C://BIOM/output/out.txt', "a") as myfile:
        myfile.write(name + ":\n" + outfile + "\n")
    #np.savetxt('C://Users/vizva/OneDrive/Dokumenty/GitHub/biometria/output/' +name +'.txt', outfile, delimiter=',')   # X is an array


import os

# for root, dirs, files in os.walk('C://Users/vizva/OneDrive/Dokumenty/GitHub/biometria/images/'):
#     for filename in files:
#         if filename.endswith(('.bmp')):
#             print('C://Users/vizva/OneDrive/Dokumenty/GitHub/biometria/images/'+filename)


for root, dirs, files in os.walk('C://BIOM/iris'):
    for file in files:
        p=os.path.join(root,file)
        if p.endswith(('.bmp')):
            print(p)
            fnc2(p)
