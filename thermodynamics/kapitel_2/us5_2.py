import math

# Constants
R = 0.2872  # kJ/(kg K), gas constant for air
d = 0.1  # Diameter of the cylinder in m
h = 0.5  # Height of the cylinder in m
p1 = 6  # Initial pressure in bar
T_u = 290  # Initial temperature in K (equals ambient temperature)
k = 1.3  # Adiabatic exponent
F = 1000  # Force applied in N
p2 = p1 + (F / (math.pi * (d / 2) ** 2)) * 1e-5  # Final pressure in bar
V1 = math.pi * (d / 2) ** 2 * h  # Initial volume in m^3

# process is reversibel adiabat 
# pv^k = constant

# a) Form of state change
state_change = "Adiabatic process due to rapid compression."

print("a) State change:", state_change)

# b) Volume reduction during adiabatic compression
V2 = V1 * (p1 / p2) ** (1 / k)  # Final volume using pV^k = const
volume_reduction_ratio = (V1 - V2) / V1

print(f"b) Volume reduction ratio during adiabatic compression: {volume_reduction_ratio * 100:.2f}%")

# c) Temperature after compression
# T_1 = T_u
T_2 = T_u * (p2 / p1) ** ((k - 1) / k)

print(f"c) Temperature after compression: {T_2:.2f} K")

# d) Volume reduction during isobaric cooling
V3 = V2 * (T_u / T_2)  # Final volume after isobaric cooling
relative_volume_reduction = - (V2 - V3) / V2

print(f"d) Relative volume reduction during isobaric cooling: {relative_volume_reduction * 100:.2f}%")

# e) Displacement under compression and cooling
h_2 = h * (V2 / V1)
h_3 = h_2 * (V3 / V2)
displacement_compression = h_2 - h
displacement_cooling = h_3 - h

print(f"e) Displacement under compression: {displacement_compression:.4f} m")
print(f"   Displacement under cooling: {displacement_cooling:.4f} m")