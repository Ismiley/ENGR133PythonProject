
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
#The final edge detection program using the Sobel Algorithm 
import Doms_test as gray
import image_blurr_functions as blur
import Sobel_edge_enhancement as enhance
import Threshold as detect
import time

#Create a grayscale image
start = time.time()
grayImage = gray.GrayScale()
end = time.time()
print(f"GrayScale Conversion completed in {round(end-start,2)} seconds.")

#Apply a Gaussian Blur
blurImage = blur.GaussianBlur(grayImage)

#Perform Edge Enhancement
start = time.time()
enhancedImage = enhance.sobel_edge_detection(blurImage)
end = time.time()
print(f"Edge enhancement completed in {round(end-start,2)} seconds.")

#Perform Sobel Edge Detection 
start = time.time()
finalImage = detect.Threshold(enhancedImage)
end = time.time()
print(f"Final edge detection completed in {round(end-start,2)} seconds.")


'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''

