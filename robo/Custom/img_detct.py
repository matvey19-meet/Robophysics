import numpy as np
import argparse
import cv2
from shapely.geometry import Polygon as plygn
import opencv
from matplotlib import pyplot as plt

#supposed to turn img into bnw but doesnt work for a reason
def clrtobw():
    ogimg = cv2.imread('Custom\onlycar.jpg')

    bwimg = cv2.cvtColor(ogimg, cv2.COLOR_BGR2GRAY)
    image2 = ogimg
    retval2,thresh = cv2.threshold(bwimg,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    th = cv2.adaptiveThreshold(bwimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    
    edges2=cv2.Canny(th,100,100)
    edges = cv2.Canny(thresh,100,100)

    contours, hierarchy = cv2.findContours(edges,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    cv2.drawContours(image2, contours, -1, (0, 255, 0), 3) 

    cv2.imshow('Contours',image2)

    # Used to flatted the array containing 
    # the co-ordinates of the vertices. 

 
    cv2.imshow('Black white image', bwimg)
    cv2.imshow('Edges image',edges)
    cv2.imshow('Edges2 image',edges2)

  
    cv2.waitKey(0)
    cv2.destroyAllWindows()


clrtobw()

image=cv2.imread("onlycar.jpg")



if image == None:
    print("None")

# define the list of boundaries 
# BGR
# bigger than, smaller than
boundaries = [
	([0, 0, 230], [41, 41, 255])
    ]

# loop over the boundaries
for (lower, upper) in boundaries:
 	# create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    # show the images
    cv2.imshow("path6.jpg", np.hstack([image, output]))
    cv2.waitKey(0)
    cv2.imwrite("onlycar.jpg", output)


#use shapely to find center of the shape (array) + make that shape as starting point.
def carPos():
    ox,oy=opencv.plot_coordinate(image,)

    P = Polygon(ox,oy)

    print(P.centroid)
   
    mypolygon.centroid.coords #gives you the coordinates
    
    #set p.centroid as satring point

