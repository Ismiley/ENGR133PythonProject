
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Python Team Project: Image Analysis
	Author:         Matthew Kane, kane83@purdue.edu
	Team ID:        LC5-005
	
Contributors:   Matthew Kane, kane83@purdue.edu
                Dominic Caponigo, dcoponig@purdue.edu
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
import image_blurr_functions as blur
import matplotlib.pyplot as plt
import numpy as np
import time

inputs = blur.getInputs()                      #Call the inputs function
while isinstance(inputs, tuple) != True:       #Workaround for inputs function returning invalid values
    inputs = blur.getInputs()
sigma = float(inputs[0])                       #Separate the tuple of inputs into useful variable names
kernelRows = int(inputs[1])
kernelCols = int(inputs[1])

#Start the timer
start = time.time()

#Get the image data
grayscaleVals,numRows,numCols = blur.getGrayImageData()                        

#Create an empty array to later store the blurred image in
blurredImage = np.zeros((numRows,numCols))                                     

#Pad the image with extra 0s for processing and return new number of columns/rows (terrible bugfix but that's okay)
grayscaleVals,numCols,numRows = blur.padImage(numRows,numCols,kernelRows,kernelCols,grayscaleVals) 

#Calculate the Gaussian kernel
gaussKernel,sumGauss = blur.calcGaussKernel(sigma,kernelRows,kernelCols)             

#Create a 2D array of the blurred image data
blurredImage = blur.construct2DArray(blurredImage,kernelRows,kernelCols,numRows,numCols,grayscaleVals,gaussKernel)

#Construct 3D array with the blurred image data
gaussBlurImage = blur.createImageArray(blurredImage)                           

#Write the image to a file
blur.finalOutput(gaussBlurImage)     

#Display the image in the monitor, might be eliminated later?
end = time.time()                                   
print(f"Time elapsed: {round(end - start,2)} seconds.")
imgplot = plt.imshow(gaussBlurImage)

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''

