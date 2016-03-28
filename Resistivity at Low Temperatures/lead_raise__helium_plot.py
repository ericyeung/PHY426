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

data = np.loadtxt('lead_helium_pull_out.txt', comments='#')
times = data[:,0]

# Normal data
lockin_voltage = data[:,1]
temperature_voltage = data[:,2]

# Finds the list index in which the temperature is 2.286301 V
bottom_cutoff = np.argwhere(temperature_voltage == 2.286301)   

# Finds the list index in which the temperature is 2 V
top_cutoff = np.argwhere(temperature_voltage == 2.000542)   

# Truncated data 
short_lockin = lockin_voltage[bottom_cutoff:top_cutoff]
short_temp = temperature_voltage[bottom_cutoff:top_cutoff]

current = 0.5
resistance = short_lockin/current

plt.figure(1)
plt.plot(short_temp, resistance)
plt.axhline(y=0.000,xmin=0,xmax=3,c="red",linewidth=0.5,zorder=0)
plt.xlabel('Temperature(V)')
plt.ylabel(r'Resistance ($\Omega$)')
plt.title(r'Lead Probe (Truncated), $T_c \simeq 7.0$ K')
plt.show()

