 #!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage, scipy.signal

"""
EXPERIMENT 2: ELECTRON MICROSCOPE
This module finds the positions of the rings of various metals. 
I take 1 row of the array so that I get a fixed y value so
I can vary x and get the intensity of the electron beam. Scipy's 
ndimage module was used to read an image and put the output into 
a 409 by 409 array.

Latest Revision: March 2 2016
"""

__author__ = "Eric Yeung"

# READING THE FILE
def read_(file_name):
    diffraction_pattern = scipy.ndimage.imread(file_name, flatten = True)
    return diffraction_pattern

xplot = np.arange(0, 409) # Axis to plot each diffraction pattern

# FOR GOLD (center is at 230.402, 179.052)
gold = read_('au4.bmp')
gold_xaxis = gold[230,:] # Extract x axis at the midpoint of y so no duplicates

# FOR ALUMINUM (center is at  230.402, 177.009)
aluminum = read_('al2.bmp')
aluminum_xaxis = aluminum[230,:]

# FOR SILVER (center is at 220.936, 171.486)
silver = read_('ag1.bmp') # Very coarse crystal, bright dots in ring)
silver_xaxis = silver[221,:] # round 220.9 up

# FOR UNKNOWN CRYSTAL (center is at 223.136, 171.568)
unknown = read_('ukn1.bmp')
unknown_xaxis = unknown[223,:]

# FOR BRIGHTER UNKNOWN CRYSTAL (center is at 222.844, 172.234)
bright_unknown = read_('ukn3.bmp')
bright_unknown_xaxis = bright_unknown[223,:]

# FOR NON-EPITAXIAL NICKEL (center is at 221.21, 180.073)
nonepitax = read_('ni1(not epitaxial).bmp')
nonepitax_xaxis = nonepitax[221,:]

# FOR EPIXTAXIAL NICKET (center is at 221.923, 166.47)
nickel = read_('ni1(epitaxial).bmp')
nickel_xaxis = nickel[166,:] # round 221.923 up

"""
def ring_finder(diffraction_pattern):
    
    I just want the peaks of the intensity found above. The peaks
    indicate each ring. Don't use this. Too complex.

    return peakdet(diffraction_pattern, 10)

print ring_finder(gold_xaxis)
"""

if __name__ == "__main__":
    # Plot diffraction patterns with the labels
    
    plt.figure(1)
    #plt.imshow(gold, cmap = 'gray')
    plt.plot(xplot, gold_xaxis)
    plt.xlabel("Position (Pixels)")
    plt.ylabel("Intensity")
    plt.title("Gold")

    plt.figure(2)
    #plt.imshow(aluminum, cmap = 'gray')
    plt.plot(xplot, aluminum_xaxis)
    plt.xlabel("Position (Pixels)")
    plt.ylabel("Intensity")
    plt.title("Aluminum")

    plt.figure(3)
    #plt.imshow(silver, cmap = 'gray')
    plt.xlabel("Position (Pixels)")
    plt.ylabel("Intensity")
    plt.plot(xplot, silver_xaxis)
    plt.title("Silver")

    plt.figure(4)
    #plt.imshow(unknown, cmap = 'gray')
    plt.plot(xplot, unknown_xaxis)
    plt.xlabel("Position (Pixels)")
    plt.ylabel("Intensity")
    plt.annotate("288.9", xy = (289, 256), xytext=(288, 265)) # First ring
    plt.annotate("155.4", xy = (155, 255), xytext=(153, 264))
    plt.annotate("115.3", xy = (115, 70), xytext=(106, 80)) # Second ring
    plt.annotate("330.8", xy = (331, 74), xytext=(328, 84))
    plt.annotate("84.16", xy = (84, 66), xytext=(72, 73)) # Third ring
    plt.annotate("360.2", xy = (360, 66), xytext=(358, 73))
    plt.annotate("384.3", xy = (384, 37), xytext=(382, 46)) # Fourth ring
    plt.annotate("", xy = (384, 37), xytext=(382, 46)) # Fourth ring
    plt.title("Unknown Sample")

    plt.figure(5)
    #plt.imshow(bright_unknown, cmap = 'gray')
    plt.plot(xplot, bright_unknown_xaxis)
    plt.title("Brighter Unknown Sample")

    plt.figure(6)
    #plt.imshow(nonepitax, cmap = 'gray')
    plt.plot(xplot, nonepitax_xaxis)
    plt.xlabel("Position (Pixels)")
    plt.ylabel("Intensity")
    plt.title("Non-epitaxial Nickel")

    plt.figure(7)
    #plt.imshow(nickel, cmap = 'gray')
    plt.plot(xplot, nickel_xaxis)
    plt.xlabel("Position (Pixels)")
    plt.ylabel("Intensity")
    plt.title("Epitaxial Grown Nickel")
    plt.show()
    
else:
    print "Importing diffraction pattern data from ringfinder.py..."    
