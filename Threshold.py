# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:03:52 2020

@author: Ismail Husain
"""

### Thresholding

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#get image location
#path = input('Input image file name (in folder): ')
##Function to import image
def importImage(path):
    image = mpimg.imread(path)
    return image



##Threshold function
#Takes each RGB value, converts to 8 bit number,
#converts to black (0) or white (255) if threshold value is met
def Threshold():
    image = mpimg.imread("Sobel_edge_enhanced.png")
    thresholdVal = -1
    while thresholdVal > 255 or thresholdVal < 0:
        thresholdVal = int(input("Enter the desired threshold value [Recommended=25]: "))
        if thresholdVal > 255 or thresholdVal < 0:
            print("Please enter a valid threshold value!")
    iRows = len(image)
    iCols = len(image[0])
    iVals = len(image[0][0])
    for i in range(iRows):
        for j in range(iCols):
            for k in range(iVals):   
                valRGB = 255 * image[i][j][k]
                if valRGB > thresholdVal:
                    image[i][j][k] = 1
                else:
                    image[i][j][k] = 0
    #Export image
    mpimg.imsave('Threshold.png', image)
    plt.imshow(image)
    plt.show()

    return image



