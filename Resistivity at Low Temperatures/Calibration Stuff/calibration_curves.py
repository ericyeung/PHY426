#!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

"""
EXPERIMENT 3: Resistivity at low temperatures
Calibration curves and line equations of the
copper, lead, and gold probes

Latest Revision: March 27 2016, 7:00 pm
"""

__author__ = "Eric Yeung"

copper = np.loadtxt('cucal.txt', comments='#')
lead = np.loadtxt('leadcal.txt', comments='#')
gold = np.loadtxt('goldcal.txt', comments='#')

copper_temp = copper[:,0]
copper_volt = copper[:,1]

lead_temp = lead[:,0]
lead_volt = lead[:,1]

gold_temp = gold[:,0]
gold_volt = gold[:,1]

plt.figure(1)
plt.plot(copper_volt, copper_temp)
plt.xlabel('Voltage (V)')
plt.ylabel('Temperature (K)')
plt.title('Copper Calibration')

plt.figure(2)
plt.plot(lead_volt, lead_temp)
plt.xlabel('Voltage (V)')
plt.ylabel('Temperature (K)')
plt.title('Lead Calibration')

plt.figure(3)
plt.plot(gold_volt, gold_temp)
plt.xlabel('Voltage (V)')
plt.ylabel('Temperature (K)')
plt.title('Gold Calibration')

plt.show()

cu_slope = (4-27)/(2.4914-1.1323); print cu_slope
pb_slope = (4-21)/(2.4294 - 1.3983); print pb_slope
au_slope = (2.4-26)/(2.40558-1.15978); print au_slope