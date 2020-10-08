# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:03:52 2020

@author: Ismail Husain
"""

### Thresholding

import matplotlib.image as mpimg


path = input('Input image file name (in folder): ')

def importImage(path):
    image = mpimg.imread(path)
    return image


image = importImage(path)



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


image = Threshold(image)

mpimg.imsave('Threshold.png', image)

