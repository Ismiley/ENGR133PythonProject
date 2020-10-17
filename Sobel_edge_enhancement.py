#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:35:04 2020

@author: avneeshv
"""


'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Python Team Project
	Author:         Avneesh Viswanath, viswan16@purdue.edu
	Team ID:        LC5-05 (e.g. LC1-14 for section 1 team 14)
	
Contributors:    DJ Caponigro, ldcaponig@purdue.edu
                 Matthew Kane, kane83@purdue.edu
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
import numpy as np
import matplotlib as mpl
   
def sobel_edge_detection(image):
    
    print("Performing sobel edge detection...")
    
    grayImage = mpl.pyplot.imread(image)  #Reads in grayscale image with gaussian filter
    filter_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])  # Kernel for convulution
    
    new_image_x = convolve(grayImage,filter_x) #Image convolved with X filter
    new_image_y = convolve(grayImage,np.flip(filter_x.T,axis=0)) #Image convolved with y filter
    
    mpl.pyplot.imshow(new_image_x,cmap = "gray")
    mpl.pyplot.imshow(new_image_y,cmap = "gray")
   
    gradient = np.sqrt(np.square(new_image_x) + np.square(new_image_y)) #Calculates magnitude of gradient
    gradient *= 255/gradient.max() #Normalizes to values between 0 to 255
    
    mpl.pyplot.imshow(gradient,cmap = "gray") #Plots sobel edge enhanced image
    
    file = open("Sobel_edge_enhanced.png","wb") #Opens image file
    mpl.pyplot.imsave("Sobel_edge_enhanced.png",gradient,cmap="gray") #Save Sobel edge enhanced image plot
    file.close()
    
    print("Process completed")
    
    return gradient, createImageArray(gradient)

def createImageArray(Image): #Function to create a 3D array of the gradient magnitude for thresholding in the next step
    numRows = Image.shape[0] #Re-establish the number of rows because the padding is no longer necessary
    numCols = Image.shape[1]
    image_3d_arr = np.zeros((numRows,numCols,3)) #Create an empty array that will hold the image data
    for i in range(0,numRows): #Iterate over the empty array and populate it with the new pixel value derived from the sum of the product of the Gauss Kernel and working window
        for j in range(0,numCols):
            for k in range(0,3):
                image_3d_arr[i][j][k] = Image[i][j]
                
    return Image


def convolve(image, kernel):
    
    image_row, image_col = image.shape
    kernel_row, kernel_col = kernel.shape
 
    output = np.zeros(image.shape)
    
    for i in range(1,image_row-2):
        for j in range(1,image_col-2):
            output[i, j] = np.sum(kernel * image[i:i + kernel_row, j:j + kernel_col]) #Performs convolution operation,
           
    return output
 
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
