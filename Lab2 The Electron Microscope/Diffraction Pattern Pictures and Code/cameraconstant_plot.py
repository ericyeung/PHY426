 #!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

"""
EXPERIMENT 2: ELECTRON MICROSCOPE
This module plots the camera constant as
a function of distance from the center 
Latest Revision: March 2 2016
"""

__author__ = "Eric Yeung"

# Pixel to millimetre proportionality constant is around 8.5 using known values for gold
# Rings correspond to 111, 200, 220, 311 respectively 

goldDiameter = np.array([285.484-168.75, 298.79 - 156.986, 
	339.012-114.617, 360.181-92.54])/8.5 # In millimetres

aluDiameter = np.array([290.625-170.87, 303.024-157.56, 342.944-116.73,
	364.113-95.87])/8.5 

silverDiameter = np.array([272.782-164.214, 287.601-151.21, 
	328.73-109.476, 350.202-88.004])/8.5

unknownDiameter = np.array([288.9-155.4, 330.8-115.3, 360.2-84.16,
	382.863-62.9])/8.5

nickelDiameter = np.array([263.71-176.31, 304.536-136.089, 
	320.565-123.992, 341.734-108.871])/8.5

# Interplanar distances for 111, 200, 220, and 311 (a = 0.407 nm for gold)
d_hkl = 0.4079*np.array([1/np.sqrt(1+1+1), 1/np.sqrt(4+0+0), 
	1/np.sqrt(4+4+0), 1/np.sqrt(9+1+1)])

camera_constant = d_hkl*goldDiameter/2 # Divide by 2 to get radius
average_camera_constant = np.mean(camera_constant)

# Lattice parameter for Aluminum 
lattice_constant_Al = camera_constant*np.sqrt(1+1+1)/(aluDiameter/2)

# Lattice parameter for Silver
lattice_constant_Ag = camera_constant*np.sqrt(1+1+1)/(silverDiameter/2)

# Lattice parameter for Unknown sample (copper)
lattice_constant_u = camera_constant*np.sqrt(1+1+1)/(unknownDiameter/2)

# Lattice parameter for epitaxially grown nickel
lattice_constant_Ni = camera_constant*np.sqrt(1+1+1)/(nickelDiameter/2)

if __name__ == '__main__':
	plt.plot(goldDiameter/2, camera_constant)
	plt.xlabel("Distance r (mm)")
	plt.ylabel("Camera Constant K (nm" r"$\times$ mm)")
	plt.title("K vs Ring Radii")
	plt.show()
	
	print lattice_constant_Al
	print lattice_constant_Ag
	print lattice_constant_u
	print lattice_constant_Ni