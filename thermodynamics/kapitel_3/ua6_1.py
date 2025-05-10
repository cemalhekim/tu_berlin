'''
In einer Warmwasserheizung soll isobar ein Wassermassenstrom m_dotW von T1W 
auf T2W isobar aufgeheizt werden. Für die Erwärmung werden die Abgase eines
Ölbrenners verwendet, welche als ideales Gas betrachtet werden können.

a) Wie groß muss m_dotW für die Übertragung eines Wärmestroms von Q12W sein?
b) Der Abgasstrom kühlt von T1A auf T2A ab. Wie groß ist der Abgasmassenstrom?
'''
import math

# Constants for water
cpW = 4.183  # kJ/(kg K)
T1W = 30  # Initial water temperature in °C 
T2W = 50  # Final water temperature in °C 
Q12W = 10  # Heat flow in kW

# Constants for exhaust gas
T2A = 800  # Initial exhaust gas temperature in °C 
T1A = 90  # Final exhaust gas temperature in °C
T0A = 0
Q12A = -10
cp01A = 1.007
cp02A = 1.071

# a) Required water mass flow rate
dTW = T2W - T1W  # Temperature change for water in K
m_dotW = Q12W / (cpW * dTW)  # Mass flow rate of water in kg/s

print(f"a) Required water mass flow rate: {m_dotW:.5f} kg/s")

# b) Exhaust gas mass flow rate
T01A = T0A - T1A
T02A = T0A - T2A
T12A = T1A - T2A
cp12A = - (T01A * cp01A / T12A) + (T02A * cp02A / T12A) # Specific heat capacity in kJ/(kg K)

print(f"cp12A: {cp12A:.5f} kJ/(kg*K)")

m_dot_gas = Q12A / (cp12A * T12A)  # Mass flow rate of exhaust gas in kg/s

print(f"b) Exhaust gas mass flow rate: {m_dot_gas:.5f} kg/s")
