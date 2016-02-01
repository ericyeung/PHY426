#!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
#from scipy import misc
import scipy.ndimage

"""
EXPERIMENT 1: HELIUM NEON LASER
Latest Revision: January 31 2015
"""

__author__ = "Eric Yeung"

# FOR POSITION 57cm
imgarray0 = scipy.ndimage.imread('0profile(57cm)crop.bmp', flatten = True)
xplot0 = np.arange(0, 230)

# FOR POSITION 67cm
imgarray1 = scipy.ndimage.imread('3profile(67cm)crop.bmp', flatten = True)
xplot1 = np.arange(0, 213)

# FOR POSITION 77cm
imgarray2 = scipy.ndimage.imread('2profile(77cm)crop.bmp', flatten = True)
xplot2 = np.arange(0, 153)

# FOR POSITION 87cm
imgarray3 = scipy.ndimage.imread('4profile(87cm)crop.bmp', flatten = True)
xplot3 = np.arange(0, 190)

# FOR POSITION 97cm
imgarray4 = scipy.ndimage.imread('1profile(97cm)crop.bmp', flatten = True)
xplot4 = np.arange(0, 225)

def diamater_finder(imgarray):
	# Count number of non- "blank pixels" in picture as the diameter of the beam
	diameter = (imgarray < 200).sum() # Values above a certain intensity
	return diameter

if __name__ == "__main__":
	print "Diameter of beam at 57cm: %s units" % diamater_finder(imgarray0[105,:])
	print "Diameter of beam at 67cm: %s units" % diamater_finder(imgarray1[110,:])
	print "Diameter of beam at 77cm: %s units" % diamater_finder(imgarray2[86,:])
	print "Diameter of beam at 87cm: %s units" % diamater_finder(imgarray3[93,:])
	print "Diameter of beam at 97cm: %s units" % diamater_finder(imgarray4[94,:])

	# Plot
	plt.figure(1)
	plt.imshow(imgarray0, cmap = 'gray')
	plt.plot(xplot0, imgarray0[105,:], color = 'r', label = 'Intensity')
	plt.title("Position: 57cm")

	plt.figure(2)
	plt.imshow(imgarray1, cmap = 'gray')
	plt.plot(xplot1, imgarray1[110,:], color = 'r', label = 'Intensity')
	plt.title("Position: 67cm")

	plt.figure(3)
	plt.imshow(imgarray2, cmap = 'gray')
	plt.plot(xplot2, imgarray2[86,:], color = 'r', label = 'Intensity')
	plt.title("Position: 77cm")

	plt.figure(4)
	plt.imshow(imgarray3, cmap = 'gray')
	plt.plot(xplot3, imgarray3[93,:], color = 'r', label = 'Intensity')
	plt.title("Position: 87cm")

	plt.figure(5)
	plt.imshow(imgarray4, cmap = 'gray')
	plt.plot(xplot4, imgarray4[94,:], color = 'r', label = 'Intensity')
	plt.title("Position: 97cm")

	#plt.show()