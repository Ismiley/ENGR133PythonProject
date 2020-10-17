# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:03:52 2020

@author: Ismail Husain
"""

### Thresholding

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

#get image location
#path = input('Input image file name (in folder): ')
##Function to import image
def importImage(path):
    image = mpimg.imread(path)
    return image



##Threshold function
#Takes each RGB value, converts to 8 bit number,
#converts to black (0) or white (255) if threshold value is met
def Threshold(image):
    #image = mpimg.imread("Sobel_edge_enhanced.png")
    #image = mpimg.imread("Grayscale.png")
    thresholdVal = -1

    #Total number of bins in histogram
    bins_num = 256

    #Get histogram
    hist, bin_edges = np.histogram(image, bins=bins_num)

    #Calc center of bins
    bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.

    #Get probabilities for thresholds
    weight1 = np.cumsum(hist)
    weight2 = np.cumsum(hist[::-1])[::-1]

    #Get means of probabilities
    mean1 = np.cumsum(hist * bin_mids) / weight1
    mean2 = (np.cumsum((hist * bin_mids)[::-1]) / weight2[::-1])[::-1]
    inter_class_variance = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

    #Maximize inter_class_variance
    index_of_max_val = np.argmax(inter_class_variance)
    thresholdVal2 = bin_mids[:-1][index_of_max_val]

    #Convert threshold to 8-bit value
    thresholdVal2 = thresholdVal2 * 255

    #while thresholdVal > 255 or thresholdVal < 0:
    #    thresholdVal = int(input("Enter the desired threshold value [Recommended=25]: "))
    #    if thresholdVal > 255 or thresholdVal < 0:
    #        print("Please enter a valid threshold value!")

    iRows = len(image)
    iCols = len(image[0])
    iVals = len(image[0][0])
    for i in range(iRows):
        for j in range(iCols):
            for k in range(iVals):
                valRGB = 255 * image[i][j][k]
                if valRGB > thresholdVal2:
                    image[i][j][k] = 1
                else:
                    image[i][j][k] = 0
    #Export image
    mpimg.imsave('Threshold.png', image)
    plt.imshow(image)
    plt.show()

    return image

