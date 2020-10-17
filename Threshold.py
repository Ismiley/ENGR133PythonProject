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
def Threshold():
    image = mpimg.imread("Sobel_edge_enhanced.png")
    #image = mpimg.imread("Grayscale.png")
    #thresholdVal = -1

    # Get histogram
    hist, bin_edges = np.histogram(image, bins=256)

    # Calc center of bins
    bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.

    # Get probabilities for thresholds
    weight_1 = np.cumsum(hist)
    weight_2 = np.cumsum(hist[::-1])[::-1]

    # Get means of probabilities
    mean_1 = np.cumsum(hist * bin_mids) / weight_1
    mean_2 = (np.cumsum((hist * bin_mids)[::-1]) / weight_2[::-1])[::-1]
    iCV = weight_1[:-1] * weight_2[1:] * (mean_1[:-1] - mean_2[1:]) ** 2

    # Maximize the inter class variance
    index_of_max_val = np.argmax(iCV)
    thresholdVal2 = bin_mids[:-1][index_of_max_val]

    # Convert threshold to 8-bit value
    thresholdVal2 = thresholdVal2 * 255

    while thresholdVal > 255 or thresholdVal < 0:
        print(f"The recommended threshold value is {thresholdVal2}")
        thresholdVal2 = int(input("Enter the desired threshold value: "))
        if thresholdVal2 > 255 or thresholdVal2 < 0:
            print("Please enter a valid threshold value! [0-255]")

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

