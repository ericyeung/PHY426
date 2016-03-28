#!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

"""
EXPERIMENT 3: Resistivity at low temperatures
Plots resisitvity versus temperature for lead 

Latest Revision: March 27 2016, 7:00 pm
"""

__author__ = "Eric Yeung"

data = np.loadtxt('lead_raise_from_N_to_RT.txt', comments='#')
times = data[:,0]

lockin_voltage = data[:,1]

tempeature_voltage = data[:,2]
inc_tempeature_voltage = data[:,2]

plt.figure(1)
plt.plot(tempeature_voltage, lockin_voltage)
plt.xlabel('Temperature(V)')
plt.ylabel('Lockin (mV)')
plt.title('Lead Probe')
plt.show()

