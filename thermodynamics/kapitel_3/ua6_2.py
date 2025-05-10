'''
Ein Luftkompressor, der Luft von p1 auf p2 isotherm verdichtet, hat eine 
Förderleistung von dot_m1 und benötigt eine Antriebsleistung P12.

a) Wie groß ist der irreversible Anteil der Antriebsleistung, 
der dissipiert wird (P12_diss)?

b) Wie viel Wärme muss bei der Kompression übertragen werden (dot_Q12)?

Hinweis: Die Luft soll als ideales Gas mit R = 0.287 kJ/kgK betrachtet werden.
'''

import math

p1 = 1 # bar
p2 = 10 # bar
T = 285 # K
dot_m1 = 0.1 # kg/s
P12 = 23 # kW
R_Luft = 0.287 # kJ/(kg*K)

print("a)")

wt_12_rev = R_Luft * T * math.log(p2/p1) # kJ/kg 

print(f"wt_12_rev: {wt_12_rev:.5f} kJ/kg")

# P12 = P12_diss + P12_rev = P12_diss + dot_m1 * wt_12_rev

P12_diss = P12 - dot_m1 * wt_12_rev #kW

print(f"P12_diss: {P12_diss:.5f} kW")

print("b)")

# dot_m1 * dh = P12 + dot_Q12

# dh = cp * dT 

dT = 0

dh = 0

dot_Q12 = -P12

print(f"dot_Q12: {dot_Q12:.5f} kW")

