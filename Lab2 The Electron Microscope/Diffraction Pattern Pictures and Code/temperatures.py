#!/usr/bin/env python
from thermocouple_with_r import thermocouple

"""
EXPERIMENT 2: ELECTRON MICROSCOPE
This module converts the thermocouple voltage to temperatures. 
Latest Revision: March 1 2016
"""

__author__ = "Eric Yeung"

heating_voltages = [0.02, 0.12, 0.32, 0.62, 0.82,
                   1.12, 1.32, 1.83, 2.00, 2.7,
                   2.32, 2.43, 2.55, 2.77, 2.87,
                   2.96]

heating_temps_kelvin = thermocouple("R", heating_voltages, "mV", "K")
heating_temps_celsius = thermocouple("R", heating_voltages, "mV", "C")

cooling_voltages = [2.86, 2.62, 2.42, 2.12, 2.0,
                   1.88, 1.72, 1.61, 1.48, 1.35,
                   1.25, 1.11, 1.0]

cooling_temps_kelvin = thermocouple("R", cooling_voltages, "mV", "K")
cooling_temps_celsius = thermocouple("R", cooling_voltages, "mV", "C")

print "The Curie temperature Tc is %s celsius or %s kelvin" % (heating_temps_celsius[-1], 
	heating_temps_kelvin[-1])

"""
print "---- TEMPERATURES WHEN HEATING (Kelvin) ----"
print heating_temps_kelvin

print "---- TEMPERATURES WHEN HEATING (Celsius) ----"
print heating_temps_celsius

print "---- TEMPERATURES WHEN COOLING (Kelvin) ----"
print cooling_temps_kelvin

print "---- TEMPERATURES WHEN COOLING (Celsius) ----"
print cooling_temps_celsius
"""