 #!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage, scipy.signal

"""
EXPERIMENT 2: ELECTRON MICROSCOPE
This module plots stuff. 
Latest Revision: March 22 2016
"""

__author__ = "Eric Yeung"

# READING THE FILE
def read_(file_name):
    diffraction_pattern = scipy.ndimage.imread(file_name, flatten = True)
    return diffraction_pattern

h002 = read_('h0.02.bmp') # 276.89 K 
h153 = read_('h1.53.bmp') # 480.07 K
h232 = read_('h2.32.bmp') # 564.85 K
h296 = read_('h2.96.bmp') # 629.47 K

sewb, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

ax1.imshow(h002, cmap = 'gray') 
ax1.axes.xaxis.set_ticks([])
ax1.axes.yaxis.set_ticks([])
ax1.set_title('(a) 276.89 K')

ax2.imshow(h153, cmap = 'gray') 
ax2.axes.xaxis.set_ticks([])
ax2.axes.yaxis.set_ticks([])
ax2.set_title('(b) 480.07 K')

ax3.imshow(h232, cmap = 'gray') 
ax3.axes.xaxis.set_ticks([])
ax3.axes.yaxis.set_ticks([])
ax3.set_title('(c) 564.85 K')

ax4.imshow(h296, cmap = 'gray')
ax4.axes.xaxis.set_ticks([])
ax4.axes.yaxis.set_ticks([])
ax4.set_title('(d) 629.47 K')

plt.tight_layout()
plt.show()