# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:03:52 2020
@author: Ismail Husain
"""
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Python Team Project: Image Analysis
	Author:         Matthew Kane, kane83@purdue.edu
	Team ID:        LC5-005
	
Contributors:   Matthew Kane, kane83@purdue.edu
                Dominick Caponigro, dcoponig@purdue.edu
                Avneesh Viswanath, viswan16@purdue.edu
                Ismail Husain, husain6@purdue.edu

	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
#Bugfix_1.4

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

#get image location
#path = input('Input image file name (in folder): ')
##Function to import image
def importImage(path):
    image = mpimg.imread(path)
    return image

#Input a threshold value
def getThresholdVal():
    global thresholdVal
    try:
        thresholdVal = float(input("Enter the desired threshold value: "))
    except ValueError:
        print("Error: Not a valid value.")
        return
    return thresholdVal

#Input a value to continue or exit program
def getContinueVal():
    global continueVal
    try:
        continueVal = int(input("If you do not like the image, press '1'. If not, click '0'. "))
    except ValueError:
        print("Error: Not a 1 or 0")
        return
    return continueVal

#Threshold and output image
def getThresholdImage(image,thresholdVal):
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
    # Export image
    mpimg.imsave('Threshold.png', image)
    plt.imshow(image)
    plt.show()


##Threshold function
#Takes each RGB value, converts to 8 bit number,
#converts to black (0) or white (255) if threshold value is met
def Threshold():
    image = mpimg.imread("Sobel_edge_enhanced.png")
    #image = mpimg.imread("Grayscale.png")
    #thresholdVal = -1

    # Get histogram
    hist, bin_edges = np.histogram(image, bins=256)

    #Calculate midpoints of each bin
    bin_midpoints = .5 * (bin_edges[1:] + bin_edges[:-1])

    #Calculate average of histogram datapoints
    histMean = np.average(bin_midpoints, weights=hist)

    #Set average of pixel data as threshold
    thresholdVal2 = histMean

    # Convert threshold to 8-bit value
    thresholdVal2 = thresholdVal2 * 255

    print(f"The recommended threshold value is {thresholdVal2}.")
    print("Here is the image printed from that threshold value.")
    getThresholdImage(image, thresholdVal2)
    cont = getContinueVal()

    while isinstance(cont,int)!=True:
        cont = getContinueVal()

    while cont == 1:
        thresholdVal = -1
        while thresholdVal > 255 or thresholdVal < 0:
            print(f"The recommended threshold value is {thresholdVal2}")
            thresholdVal = getThresholdVal()
            while isinstance(thresholdVal,float)!=True:
                thresholdVal = getThresholdVal()
        image = mpimg.imread("Sobel_edge_enhanced.png")
        getThresholdImage(image,thresholdVal)
        cont = getContinueVal()
        while isinstance(cont, int) != True:
            cont = getContinueVal()

    return image