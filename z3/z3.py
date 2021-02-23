import cv2
import numpy as np
#import matplotlib.pyplot as plt
from PIL import Image
import os
import shutil


def z3():
    images = []
    for root, dirs, files in os.walk('F://BIOM/tmp'):
        for file in files:
            p=os.path.join(root,file)
            images.append(p)


    GaborFilters = []
    tmpName = 0
    # https://stackoverflow.com/questions/30071474/opencv-getgaborkernel-parameters-for-filter-bank
    # getGaborKernel(ksize, sigma, theta, lambda, gamma, psi, ktype)
    # for j in range(1,7):
    #     if j != 5:
    #         # for i in range(0, 10):
    #         #     Gabor = cv2.getGaborKernel((5, 5), 1.0 + 2 * i, np.pi / j, 1.0, 0.5, 30.0, ktype=cv2.CV_32F)
    #         #     GaborFilters.append(Gabor)  # 45 stupnov nemenit?
    #         # for i in range(0, 10):
    #         #     Gabor = cv2.getGaborKernel((5, 5), 1.0, np.pi / j, 1.0 + 2 * i, 0.5, 30.0, ktype=cv2.CV_32F)
    #         #     GaborFilters.append(Gabor)  # 45 stupnov nemenit?
    #         # for i in range(0, 20):
    #         #     Gabor = cv2.getGaborKernel((5, 5), 1.0 + 2 * i, -np.pi / j, 1.0, 0.5, 30.0, ktype=cv2.CV_32F)
    #         #     GaborFilters.append(Gabor)
    #         Gabor = cv2.getGaborKernel((5, 5), 3.5, -np.pi / j, 7, 0.5, 30.0, ktype=cv2.CV_32F)
    #         GaborFilters.append(Gabor)
    Gabor = cv2.getGaborKernel((5, 5), 3.7, -np.pi, 7, 0.5, 30.0, ktype=cv2.CV_32F)
    GaborFilters.append(Gabor)
    Gabor = cv2.getGaborKernel((5, 5), 1, -np.pi, 1, 0.5, 30.0, ktype=cv2.CV_32F)
    GaborFilters.append(Gabor)
    Gabor = cv2.getGaborKernel((5, 5), 7, -np.pi, 10, 0.5, 30.0, ktype=cv2.CV_32F)
    GaborFilters.append(Gabor)
    Gabor = cv2.getGaborKernel((5, 5), 0.1, -np.pi, 0.1, 0.5, 30.0, ktype=cv2.CV_32F)
    GaborFilters.append(Gabor)
    Gabor = cv2.getGaborKernel((5, 5), 10, -np.pi, 20, 0.5, 30.0, ktype=cv2.CV_32F)
    GaborFilters.append(Gabor)

    #
    # for G in GaborFilters:
    #     # GaborShow = cv2.resize(Gabor,(100, 100), interpolation = cv2.INTER_LINEAR)
    #     # cv2.imshow('kernel', GaborShow)
    #     # cv2.waitKey(0)
    #     G /= 1.5 * G.sum()
    #     # GaborShow1 = cv2.resize(Gabor, (100, 100), interpolation=cv2.INTER_LINEAR)
    #     # cv2.imshow('kernel', GaborShow1)
    #     # cv2.waitKey(0)

    for image in images:
        name = image[-11:]
        img = cv2.imread(image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        for g in GaborFilters:
        # img1 = cv2.filter2D(img, cv2.CV_8UC3, Gabor)    #https://gist.github.com/kendricktan/93f0da88d0b25087d751ed2244cf770c
        # cv2.imshow('filter',img1)
        # cv2.waitKey(0)
            img1 = cv2.filter2D(img, cv2.CV_8UC3, g)
            tmp = np.sum(img1)
            tmp1 = np.size(img1)
            tmp = tmp/tmp1
        #print(tmp)
            ret, thresh1 = cv2.threshold(img1, int(tmp), 255, cv2.THRESH_BINARY)     #int(tmp)
        # cv2.imshow('filter',thresh1)
        # cv2.waitKey(0)
            new_img = Image.fromarray(thresh1)
            filename = 'C://BIOM/output/ot/binary/' + name[:7] + '/'
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            new_img.save('C://BIOM/output/ot/binary/' + name[:7] + '/' + name[:7] + str(tmpName) + name[-4:])
            tmpName += 1

        tmpName = 0


def z3_porovnanie():
    images = []
    imgs = []
    keys = []
    values = []
    same_eye = []
    name = []
    for root, dirs, files in os.walk('C://BIOM/output/ot/binary/'):
        for file in files:
            p = os.path.join(root, file)
            images.append(p)

    for image in images:
        name.append(image[-12:])
        #imgs.append(cv2.imread(name))
        if name[len(name)-1][7] == '0':
            #imgs[name] = cv2.imread(image)
            #imgs.update({name:cv2.imread(image)})
            imgs.append(image)

    # for x,y in imgs.items():
    #     keys.append(x)
    #     values.append(y)

    tmp = 0
    for i in range(1,11):
        for im in imgs:
            if im[28] == str(i) and tmp<2:
                filename = 'C://BIOM/output/ot/same_eye/' + str(i) + '/'
                if not os.path.exists(os.path.dirname(filename)):
                    os.makedirs(os.path.dirname(filename))
                shutil.copy(im,filename)
                tmp += 1
        tmp = 0

    # same_eye.append(imgs[name[1]])
    # same_eye.append(imgs[name[0]])

    # f, axarr = plt.subplots(1, 2)
    # axarr[0, 0].imshow(same_eye[0])
    # axarr[0, 1].imshow(same_eye[1])


#z3()
z3_porovnanie()
