#!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

__author__ = "Eric Yeung"

data = np.loadtxt('gold_helium_pull_out2.txt', comments='#')

times = data[:,0]

# Normal data
lockin_voltage = data[:,1]
temperature_voltage = data[:,2]

current = 0.5 
# Converted from voltage, see page 65 of notebook
temperature_kelvin = -18.94*temperature_voltage + 47.97
resistance = lockin_voltage/current

# Let's try plotting ln(T) and comparing it now
lnT_dependence = []

for i in range(len(temperature_kelvin)):
	lnT_dependence.append(np.log(temperature_kelvin[i])/100+0.05)

print lnT_dependence

plt.figure(1)
plt.plot(temperature_kelvin,resistance)
#plt.plot(temperature_kelvin, lnT_dependence)
plt.xlabel('Temperature(K)')
plt.ylabel(r'Resistance ($\Omega$)')
plt.title(r'Au $+ 0.07\%$ Fe Probe')
plt.show()
