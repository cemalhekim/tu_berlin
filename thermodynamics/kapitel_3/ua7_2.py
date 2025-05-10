'''
Ein Probenbehälter mit dem Volumen V_A dm^3 ist mit Methan gefüllt (p1 MPa,
T1 ◦C). Nun soll das Gas auf zwei Behälter verteilt werden. Dazu wird ein 
evakuierter Behälter mit dem Volumen VB dm3 mit dem ersten verbunden 
und das Ventil geöffnet. Dieser Vorgang verläuft adiabat.
Zur Vereinfachung stellen wir uns vor, dass überall im Methan der gleiche Druck/Temperatur
herrscht, d.h. das System Gas expandiert gegen ein Vakuum.

a) Wie viel Masse an Gas wird umgefüllt (m2_B)?

b) Welche Temperatur liegt nach dem Umfüllen vor?

c) Wie groß ist die Entropieänderung des Gases beim Umfüllvorgang?

Hinweise: Methan soll als ideales Gas mit R kJ/(kg K) und cv kJ/(kg K) betrachtet werden. 
Das Volumen des Verbindungsrohrs ist zu vernachlässigen.
'''

import math

# Variables

V_A = 1/1000 # m^3
p1 = 0.24*1000 # Pa
T1 = 20 + 273.15 # K
V_B = 0.5/1000 # m^3
R = 0.5197 # kJ/(kgK)
c_v = 1.559 # kJ/(kgK)
p = 0

print("a)")

m1 = p1 * V_A / (R * T1)

print(f"m1: {m1:.10f} kg")

m2 = m1

V2 = V_A + V_B

v2 = (V_A + V_B) / m1

m2_B = V_B / v2

print(f"m2_B: {m2_B:.10f} kg")

print("b)")

# dU = m2 * c_v * (T2 - T1) = Q12 + W12

Q12 = 0

W12 = 0 # p = 0

dU = Q12 + W12

T2 = T1 # m2 * c_v * (T2 - T1) = 0

print(f"T2: {T2:.10f} K")

print("c)")

# dS12 = (dU + p*dV)/T =  (m2 * c_v * dT / T) + p*dV/T -> 1,2∫(m2*R/V)dV

dS12 = m2 * R * math.log(V2 / V_A) * 1000 # J/K

print(f"dS12: {dS12:.10f} J/K")
