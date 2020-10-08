
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     e.g. Py1 Task 1
	Author:         Name, dcaponig@purdue.edu
	Team ID:        LC5-05 
	
Contributors:   Ismail Husain, husain6@purdue 
                Matthew Kane, kane83@purdue 
                Name, login@purdue 
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
import matplotlib.image as mpl
import numpy as num
import sys as s

class Error1(FileNotFoundError):
    pass

try:
    Input=input('File Name: ')
except FileNotFoundError:
    raise Error1('File name incorrect, dont forget the file type')

# Takes a file path and returns the array of the image
def importImage(x): #x is the file path as a string
    global image # to show image in variable explorer for analysis
    image = mpl.imread(x)
    image=image #here for debug sake
    return image

def RGBtoGRAY(rgb):
    global gray
    for i in range(len(rgb)):
        for j in range(len(rgb[0])):
            r=rgb[i][j][0]
            g=rgb[i][j][1]
            b=rgb[i][j][2]           
            gray=(0.2989*r+0.5870*g+0.1140*b)
            rgb[i][j][0],rgb[i][j][1],rgb[i][j][2]=gray,gray,gray
    return rgb

GOutput=open('Grayscale.png','wb')
importImage(Input)
RGBtoGRAY(image)

mpl.imsave('Grayscale.png',RGBtoGRAY(image))




#g=0
#for i in Input:
#    importImage(Input)
#    RGBtoGRAY(image)
#    GOutput.write(gray)
#    g=g+1.1
#    if g%11==0:
#        print(g)
#    else:
#        pass
    
    
    
    
#    print(importImage)
#    s.exit()



GOutput.close



'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''

