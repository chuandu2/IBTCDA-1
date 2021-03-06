# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 19:41:22 2016

@author: Chris
"""

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
np.set_printoptions(threshold=np.inf)

#image=misc.imread('C:\\Users\\Chris\\Downloads\\checkerboard.jpg')
image=misc.imread('C:\\Users\\Chris\\Downloads\\small kazak.jpg') #We have a problem here. Because of how we set up the code, this lines requires us to either
																  #change the file name in the directory to match this or we have to edit the code to match
																  #the file name in the directory.
#print (image[0])

#plt.imshow(image) #Loads Image
#plt.show() #Shows the image window

#average method
def average(pixel):
    return (pixel [0] + pixel [1] + pixel [2])/3
#luminosity method
#def modedversion(pixel):
    #return (0.21*pixel [0] + 0.72*pixel [1] + 0.07*pixel [2])
grey = np.zeros((image.shape[0], image.shape[1]))
for rownum in range(len(image)):
    for colnum in range(len(image[rownum])):
        grey[rownum][colnum] = average(image[rownum][colnum])
        #use line below when running modedversion function for our code
	#grey[rownum][colnum] = modedversion(image[rownum][colnum])
plt.imshow(grey, cmap = cm.Greys_r)
plt.show() #This pushes out the image that we use in the other block of code to anaylzse for persistent pairs


#image=misc.imread('C:\\Users\\Chris\\Downloads\\cat.jpg')
#print(image) #Gives the RGB values for all pixels. The Inner most brackers give the RGB values for the rows
#print (image.shape) #Gives the height and width of the image
#print (image[0]) #Gives RGB values for row 0
#print (image[0][0]) #Gives RGB values for row 0 and column 0
