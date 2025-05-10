import math
from sympy import symbols, integrate

# Given Data

R = 0.287  # kJ/(kg K), specific gas constant for air
p1 = 1  # bar
T1 = 300  # K
V1 = R*T1  
V2 = 0.5 * V1  # compression to half the volume
n = 1.4  # polytropic index for air
m = 1  # Mass of air in kg

# Symbols for integration
V = symbols('V')

# a) Work done for i) isothermal compression
# W = m * R * T1 * ln(V1/V2)
W_isothermal = m * R * T1 * math.log(V1 / V2)

# ii) Work done for polytropic compression
# W = (p2 * V2 - p1 * V1) / (1 - n)
p2_polytropic = p1 * (V1 / V2) ** n  # Using p1 * V1^n = p2 * V2^n
W_polytropic = (p2_polytropic * V2 - p1 * V1) / (1 - n) * 100  # Convert pressure from bar to kPa

# Convert pressure from bar to kPa for energy in kJ
W_polytropic_kJ = W_polytropic * 100

print("a) Work done:")
print(f"i) Isothermal compression: W = {W_isothermal:.2f} kJ")
print(f"ii) Polytropic compression: W = {W_polytropic_kJ:.2f} kJ")

# b) Final pressure in both cases
p2_isothermal = p1 * (V1 / V2)  # Isothermal case: p1 * V1 = p2 * V2

print("\nb) Final pressure:")
print(f"i) Isothermal compression: p2 = {p2_isothermal:.2f} bar")
print(f"ii) Polytropic compression: p2 = {p2_polytropic:.2f} bar")

# c) Heat transferred in isothermal case
# dU_12 = W_isothermal + Q_12
# dU_12 = m*c_v*(T2-T1)
# dT = 0 because of isothermal situation, so
Q_12 = - W_isothermal

print("\nc) Heat transferred in isothermal case:")
print(f"Q = {Q_12:.2f} kJ")