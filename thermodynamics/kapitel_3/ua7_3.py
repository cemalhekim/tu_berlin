'''
Zwei Luftströme mit dot_mA kg/s und dot_mB kg/s mit dem gleichen Druck von
p1 MPa aber verschiedenen Temperaturen TA K und TB K werden in
einem Rohr isobar vermischt. Das Rohr ist nach außen adiabatisch isoliert.

a) Welche Mischungstemperatur T2 stellt sich ein?

b) Wie groß ist die irreversible Zunahme der spezifischen Entropie 
nach der vollständigen Vermischung?

Hinweise: Luft soll als ideales Gas mit R kJ/(kg K) und cv kJ/(kg K) betrachtet werden.
'''

import math

# Variables

dot_mA = 0.1 # kg/s
dot_mB = 0.3 # kg/s
p1 = 0.1*1000 # Pa
TA = 300 # K
TB = 400 # K
# isboar, p1 = constant
dp = 0
V = 1 # does not matter
# adiabat
R = 0.287 
cv = 0.718 



print("a)")

dot_m2 = dot_mA + dot_mB

dH = 0

T2 = (dot_mA*TA + dot_mB*TB)/(dot_mA + dot_mB)

print(f"T2: {T2:.10f} K")

print("b)")

# dS = (dH + V * dp) / T2

dsA = (cv+R)*math.log(T2/TA)

print(f"dSA: {dsA:.10f} kJ/kgK")

dsB = (cv+R)*math.log(T2/TB)

print(f"dSB: {dsB:.10f} kJ/kgK")

dS = (dot_mA*dsA + dot_mB*dsB)

ds_irr = dS / dot_m2

print(f"ds_irr: {ds_irr:.10f} kJ/kgK")
