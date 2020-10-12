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
def GrayScale():
    import matplotlib.image as mpl

    class Error1(FileNotFoundError):
        pass

    try:
        Input=input('File Name: ')
    except FileNotFoundError:
        raise Error1('File name incorrect, dont forget the file type')

    # Takes a file path and returns the array of the image
    def importImage(x): #x is the file path as a string
        global image # to show image in variable explorer for analysis and later use
        image = mpl.imread(x)
        return image

    #Takes he image and and makes it gray by changing the color values of each pixel.
    def RGBtoGRAY(rgb):
        global gray # to show image in cariable explorer for analysis
        for i in range(len(rgb)):
            for j in range(len(rgb[0])):
                # Gets the RGB values for a pixel
                r=rgb[i][j][0]
                g=rgb[i][j][1]
                b=rgb[i][j][2]
                # Calculates new color value grayscaled
                gray=(0.2989*r+0.5870*g+0.1140*b)
                # Assignes new gray value to old RGB values
                rgb[i][j][0],rgb[i][j][1],rgb[i][j][2]=gray,gray,gray
        return rgb

    # Opens an output file, runs applicable functions, then closes
    GOutput=open('Grayscale.png','wb')
    importImage(Input)
    RGBtoGRAY(image)
    mpl.imsave('Grayscale.png',RGBtoGRAY(image))
    GOutput.close
    return image

GrayScale()

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''