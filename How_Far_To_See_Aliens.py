#!/bin/python3
import math

# Variables
v = 29979245.8     # velocity (m/s) (0.1c by default)
m = 450000         # mass of ship (kg) (450 tons by default)
t = 365.25 * 86400 # time to stop (s) (1 Julian year by default)

# Constants
AU = 149597870700 # meters
L_vega = 3.0128e28 # Watts
parsec = AU / math.tan((math.pi/180)*(1/3600)) # 1 AU/tan(1")
F0 = L_vega / (4 * math.pi * (10*parsec)**2) # Reference Flux
c = 299792458 # meters / second
visibility_limit = 6 # Limit for human visibility

# Calculating visibility flux limit
f_vis_over_vega = 10 ** ((-2)*visibility_limit*(1/5))
F_vis = f_vis_over_vega * F0

# Calculating power of ship's thrusters
gamma = 1 / math.sqrt(1 - (v/c)**2)
power = ((gamma-1) * m*c**2) / t
distance = math.sqrt(power / (4*math.pi*F_vis))

# Printing results
print("Power required:", power, "W")
print("Distance at which ship is visible:", distance/AU, "AU")