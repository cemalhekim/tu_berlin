'''
In einem Wasserbad wird m_A kg heißes Wasser (T1_A K) mit m_B kg kaltem
Wasser (T1_B K) abgekühlt. Am Ende des Prozesses herrscht in beiden Wassermengen
die gleiche Temperatur T2 K. Die Wärmekapazität des Wassers beträgt
c J/(kg*K). Das Wasserbad ist nach außen hin adiabat. 
Temperaturbedingte Volumenänderungen des Wassers sind zu vernachlässigen

a) Wie viel Wärme wurde übertragen (Q)?

b) Wie viel Entropie wurde bei dem Vorgang erzeugt?

c) Was würde (rechnerisch) passieren, 
wenn oben beschriebener Prozess rückwärts ablaufen würde?
'''

import math

# Variables

T1_A = 370 # K
m_A = 1 # kg
m_B = 4 # kg
T1_B = 280 # K
T2 = 298 # K
c = 4.190 # kJ/(kg*K)

print("a)")

# w + Q = dU 

W = 0 # keine Arbeit

dT_B = T2 - T1_B

dU_B = c * m_B * dT_B

Q = dU_B

print(f"Q: {Q:.5f} kJ")

print("b)")

dV = 0 # kein Volumenanderung
p_A = 1 # it does not matter since p_A*dV = 0

# dS_A = (dU_A + p_A*dV)/T_A -> dS_A = dU_A/T_A -> integral
# dU_A = m_A * c * dT_A

dS_A = (m_A * c) * math.log(T2 / T1_A) * 1000 # J/K

print(f"dS_A: {dS_A:.5f} J/K")

dS_B = (m_B * c) * math.log(T2 / T1_B) * 1000 # J/K

print(f"dS_B: {dS_B:.5f} J/K")

dS_total = dS_A + dS_B

print(f"dS_total: {dS_total:.5f} J/K")

print("c)")
