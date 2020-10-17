
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
#The following code is the program that performs the edge blurring on the converted grayscale image.
#All commented print statements are for debug purposes only

import matplotlib.image as mpl
import matplotlib.pyplot as plt
import numpy as np
import math as m
import time

def getInputs():                                                               #Function for obtaining input values from the user                                                       
    try:                                                                       #Error handling for incorrect entries for a sigma value
        sigma = float(input("Enter a value for the sigma/variance: "))
    except ValueError:
        print("ERROR: The sigma value must be a positive floating point number.")  
    else:
        try:
            n = float(input("Enter the size for the kernel dimensions: "))     #Error handling for incorrect entries for kernel dimensions
        except ValueError:
            print("ERROR: The kernel dimension must be a positive, odd integer greater than 1.")
        else:
            if n % 2 == 0 or int(n) != n or n <= 0 or n == 1:
                print("ERROR: The kernel dimension MUST be a positive, odd integer greater than 1.")
                if sigma <= 0:
                    print("ERROR: The sigma value must be greater than 0.")
                return
            if sigma <= 0:
                print("ERROR: The sigma value must be greater than 0.")
                if n % 2 == 0 or int(n) != n or n <= 0 or n == 1:
                    print("ERROR: The kernel dimension MUST be a positive, odd integer greater than 1.")
                return
            else:
                return sigma, n

def getGrayImageData(grayImage):                                               #Function for importing grayscale image
    #grayImage = mpl.imread("Grayscale.png")                                   #Get the grayscaled image from the previous filter using matplotlib
    data = np.array(grayImage)                                                 #Establish a NumPy array with the grayscale image data
    numRows = data.shape[0]                                                    #Store variables with the x and y dimensions of the photo
    numCols = data.shape[1]
    grayscaleVals = np.zeros((numRows,numCols))                                #Create an empty array for simplified image data
    for i in range(0,numRows):                                                 #Loop through the image and convert to 2D array
        for j in range(0,numCols):
            grayscaleVals[i][j] = data[i][j][0]
    numPixels = numRows * numCols
    #print(f"The dimesions of the image are x: {numCols} and y: {numRows}")
    #print(f"The first row of data is: {grayscaleVals[0]}")                       
    return grayscaleVals,numRows,numCols,numPixels

def padImage(numRows,numCols,kernelRows,kernelCols,grayscaleVals):             #Function for giving the image a border to prevent going "out of bounds" with the kernel
    topBottom =  m.floor(kernelRows/2)                                         #Caclulate the width of the border
    leftRight = m.floor(kernelCols/2)
    grayscaleVals = np.pad(grayscaleVals, [(topBottom,topBottom),(leftRight,leftRight)])
    numCols += leftRight                                                       #Update the number of columns and rows in the image
    numRows += topBottom
    #print(f"Zeros added to top and bottom: {topBottom}")
    #print(f"Zeros added to left and right: {leftRight}")
    return grayscaleVals,numCols,numRows

def calcGaussKernel(sigma,kernelRows,kernelCols):                              #Function for creating the Gaussian Blur Kernel
    gaussKernel = np.zeros((kernelRows,kernelCols))                            #Create an empty array to hold the Gaussian Kernel
    for i in range(0,kernelRows):                                              #Iterate through the empty array and fill it with the normal Gaussian distribution values
        for j in range(0,kernelCols):
            x = abs(m.floor(kernelCols/2)-i)                                   #The x and y values are relative to the distance from the center pixel in the kernel. (0,0) is the center pixel
            y = abs(m.floor(kernelRows/2)-j)
            gaussKernel[i][j] = (1/(2*m.pi*sigma**2))*(m.e**(-((x**2+y**2)/(2*sigma**2))))
    sumGauss = np.sum(gaussKernel)                                             #Correct the Gaussian Kernel so that the sum of the array is 1
    for i in range(0,kernelRows):                                              #Iterate through the kernel and apply the correction 
        for j in range(0,kernelCols):
            gaussKernel[i][j] = gaussKernel[i][j] * (1/sumGauss)
    #print("Gaussian Kernel:")
    #print(gaussKernel)
    #print(f"Sum: {np.sum(gaussKernel)}\n")
    return gaussKernel, sumGauss

def calcWindow(kernelRows,kernelCols,grayscaleVals,currentCol,currentRow,colInImage): #Function that populates the "working window" with the values of the pixels it is currently centered over
    kernel = np.zeros((kernelRows,kernelCols))                                 #Create an empty array to hold the "working" kernel
    for i in range(0,kernelRows):                                              #Iterate through the kernel and populate it with the pixles in the image that it is currently on top of
        for j in range(0,kernelCols):
            kernel[i][j] = grayscaleVals[currentRow+i][currentCol+j]
    #print(f"Pixel of interest: is {grayscaleVals[rowInImage][colInImage]} at row {rowInImage} and column {colInImage}")
    #print("Working Kernel:")
    #print(f"{kernel},\n")        
    return kernel    

def calcBlur(kernelRows,kernelCols,gaussKernel,kernel):                        #Function to calculate the the "blur value" based on the Gaussian kernel applied over the working window of the image
    blurKernel = np.zeros((kernelRows,kernelCols))                             #Create an empty array to hold the values of the Gaussian kernel applied over the working window
    for i in range(0,kernelRows):                                              #Iterate over the empty array and replace the value with the pixels in the window and the Gauss kernel multiplied together
        for j in range(0,kernelCols):
            blurKernel[i][j] = gaussKernel[i][j] * kernel[i][j]
    blurVal = np.sum(blurKernel)                                               #Sum the contents of the kernel
    #previousVal = grayscaleVals[rowInImage][colInImage]
    #print("Blurred Kernel:")
    #print(blurKernel)
    #print(f"Sum: {blurVal}\n")
    #print(f"Old Pixel Value: {previousVal}")
    #print(f"New Pixel Value: {blurVal}")  
    return blurVal
  
def construct2DArray(blurredImage,kernelRows,kernelCols,numRows,numCols,grayscaleVals,gaussKernel,numPixels):
    print("Processing image...") 
    currentPixel = 0
    currentCol = 0                                                             #Variable to store where cursor is relative to the window
    currentRow = 0                                                                 
    rowInImage = m.floor(kernelRows/2)                                         #variable to store where the cursor is relative to the image
    colInImage = m.floor(kernelCols/2)                                             
    rowBlur = 0                                                                #Variable to store the cursor relative to the blurred image
    colBlur = 0                                                                    
    while rowInImage < numRows and colInImage < numCols:                       #Iterate through the rows and columns of the image, making each pixel the center pixel of the working window
        kernel = calcWindow(kernelRows,kernelCols,grayscaleVals,currentCol,currentRow,colInImage)
        if colInImage == (numCols-1):                                          #Handle the case when the counter reaches the end of a row
            rowInImage += 1                                                        
            colInImage = (m.floor(kernelCols/2)-1)                                 
        colInImage += 1                                                                                                                   
        currentCol = colInImage - m.floor(kernelCols/2)                        #calculate the row/column that the window starts filling from 
        currentRow = rowInImage - m.floor(kernelRows/2)                            
        #print(f"The new window will be centered on pixel at row {rowInImage} and column {colInImage} and will start from row {currentRow} and start from column {currentCol}")
        #pauseBuffer = input("Pausing... Press Enter to Continue")
    
        blurVal = calcBlur(kernelRows,kernelCols,gaussKernel,kernel)           #Construct the blur Value 

        blurredImage[rowBlur][colBlur] = blurVal                               #Fill in the 2D blurred image array using the blurred pixel value and the current location of the pixel in the image
        colBlur += 1
        if colBlur == (numCols - m.floor(kernelCols/2)):                       #Handles when the cursor in the blurred image reaces the end
            colBlur = 0
            rowBlur += 1
        print(f"\r{int((currentPixel/numPixels)*100)}% Complete",end='')
        currentPixel += 1
        #pauseBuffer = input("Pausing...Press Enter to Continue") 
    return blurredImage
  
def createImageArray(blurredImage):                                            #Function to create a 3D array of the blurred image
    numRows = blurredImage.shape[0]                                            #Re-establish the number of rows because the padding is no longer necessary
    numCols = blurredImage.shape[1]
    gaussBlurImage = np.zeros((numRows,numCols,3))                             #Create an empty array that will hold the image data
    #print(f"The dimensions of the output image are x: {numCols} and y: {numRows}")
    for i in range(0,numRows):                                                 #Iterate over the empty array and populate it with the new pixel value derived from the sum of the product of the Gauss Kernel and working window
        for j in range(0,numCols):
            for k in range(0,3):
                gaussBlurImage[i][j][k] = blurredImage[i][j]
    return gaussBlurImage

def finalOutput(gaussBlurImage):                                               #Function to write the contents of the 3D array to a file   
    plt.imshow(gaussBlurImage) 
    plt.show()
    file = open('gaussBlur.png','wb')                                          #Construct a file named "gaussBlur" in the .png format
    mpl.imsave('gaussBlur.png',gaussBlurImage)                                 #use the matplotlib to write the array to an image file
    file.close()     
    print("\nGaussian Blur Complete. Please see file \"gaussBlur.png\"")       #Close the file
    return

'''
===============================================================================
'''

def GaussianBlur(grayImage): 

    inputs = getInputs()                                                       #Call the inputs function
    while isinstance(inputs, tuple) != True:                                   #Workaround for inputs function returning invalid values
        inputs = getInputs()
    sigma = float(inputs[0])                                                   #Separate the tuple of inputs into useful variable names
    kernelRows = int(inputs[1])
    kernelCols = int(inputs[1])

    #Start the timer
    start = time.time()

    #Get the image data
    grayscaleVals,numRows,numCols,numPixels = getGrayImageData(grayImage)                        

    #Create an empty array to later store the blurred image in
    blurredImage = np.zeros((numRows,numCols))                                     
    
    #Pad the image with extra 0s for processing and return new number of columns/rows (terrible bugfix but that's okay)
    grayscaleVals,numCols,numRows = padImage(numRows,numCols,kernelRows,kernelCols,grayscaleVals) 

    #Calculate the Gaussian kernel
    gaussKernel,sumGauss = calcGaussKernel(sigma,kernelRows,kernelCols)             

    #Create a 2D array of the blurred image data
    blurredImage = construct2DArray(blurredImage,kernelRows,kernelCols,numRows,numCols,grayscaleVals,gaussKernel,numPixels)

    #Construct 3D array with the blurred image data
    gaussBlurImage = createImageArray(blurredImage)                           

    #Write the image to a file
    finalOutput(gaussBlurImage)     

    #Return the image for use in the next program
    end = time.time()                                   
    print(f"\nGaussian blur completed in {round(end - start,2)} seconds.")
    return blurredImage

#GaussianBlur()
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''

