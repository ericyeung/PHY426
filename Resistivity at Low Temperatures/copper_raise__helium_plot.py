#!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

__author__ = "Eric Yeung"

data = np.loadtxt('copper_helium_pull_out.txt', comments='#')

times = data[:,0]

current = 0.5 # Constant in mA

# Normal data
lockin_voltage = data[:,1]
temperature_voltage = data[:,2]

# Converted from voltage, see page 61 of notebook
temperature_kelvin = -16.92*temperature_voltage + 46.16
resistance = lockin_voltage/current

# Let's try plotting T^5 and comparing it now
T5_dependence = []
for i in range(len(temperature_kelvin)):
	T5_dependence.append(temperature_kelvin[i]**5/10000000+1.7)

print T5_dependence

plt.figure(1)
plt.plot(temperature_kelvin,resistance, color = 'b', label = 'Resistance')
plt.plot(temperature_kelvin, T5_dependence, color = 'r', label = r'$T^{ 5}$')
plt.xlabel('Temperature(K)')
plt.ylabel(r'Resistance ($\Omega$)')
plt.title('Copper Probe')
plt.legend().draggable()
plt.show()

