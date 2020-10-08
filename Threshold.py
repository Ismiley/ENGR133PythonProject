# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:03:52 2020

@author: Ismail Husain
"""

### Thresholding

import matplotlib.image as mpimg

#get image location
path = input('Input image file name (in folder): ')

##Function to import image
def importImage(path):
    image = mpimg.imread(path)
    return image

#import image
image = importImage(path)


##Threshold function
#Takes each RGB value, converts to 8 bit number,
#converts to black (0) or white (255) if threshold value 160 is met
def Threshold(image):
    iRows = len(image)
    iCols = len(image[0])
    iVals = len(image[0][0])
    for i in range(iRows):
        for j in range(iCols):
            for k in range(iVals):   
                valRGB = 255 * image[i][j][k]
                if valRGB > 160:
                    image[i][j][k] = 1
                else:
                    image[i][j][k] = 0
    return image

#Apply Threshold function
image = Threshold(image)

#Export image
mpimg.imsave('Threshold.png', image)

