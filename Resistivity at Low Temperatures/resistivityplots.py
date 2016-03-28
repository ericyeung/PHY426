#!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

"""
EXPERIMENT 3: Resistivity at low temperatures
Plots resisitvity versus temperature for Cu 

Latest Revision: March 24 2016, 8:30 am
"""

__author__ = "Eric Yeung"

data = np.loadtxt('copper_test_helium_increasing.txt', comments='#')
times = data[:,0]

peak = (np.argmax(data[:,2])) # Should be 2.43 V or 4.8 K

decreasing_data = data[:peak, :]
increasing_data = data[peak:, :]

dec_lockin_voltage = decreasing_data[:,1]
inc_lockin_voltage = increasing_data[:,1]

dec_tempeature_voltage = decreasing_data[:,2]
inc_tempeature_voltage = increasing_data[:,2]

plt.figure(1)
plt.plot(dec_tempeature_voltage, dec_lockin_voltage)
plt.xlabel('Temperature(V)')
plt.ylabel('Lockin (mV)')
plt.show()

