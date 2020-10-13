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
from scipy import signal
import matplotlib as mpl
   
def sobel_edge_detection(image):
    
    #grayImage = mpl.pyplot.imread(image)  #Reads in grayscale image with gaussian filter
    grayImage = image
    filter_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])  # Kernel for convulution
    
    new_image_x = signal.convolve2d(grayImage,filter_x) #Image convolved with X filter
    new_image_y = signal.convolve2d(grayImage,np.flip(filter_x.T,axis=0)) #Image convolved with y filter
    
    mpl.pyplot.imshow(new_image_x,cmap = "gray")
    mpl.pyplot.imshow(new_image_y,cmap = "gray")
   
    gradient_magnitude = np.sqrt(np.square(new_image_x) + np.square(new_image_y)) #Calculates magnitude of gradient
    gradient_magnitude *= 255/gradient_magnitude.max() #Normalizes to values between 0 to 255
    
    mpl.pyplot.imshow(gradient_magnitude,cmap = "gray")
    print("Edge Enhancement Complete.")
    
    file = open("Sobel_edge_enhanced.png","wb") #Opens
    mpl.pyplot.imsave("Sobel_edge_enhanced.png",gradient_magnitude,cmap="gray")
    file.close()
    
    return gradient_magnitude

#sobel_edge_detection()

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
