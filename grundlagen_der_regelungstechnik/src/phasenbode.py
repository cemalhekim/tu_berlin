import numpy as np
import matplotlib.pyplot as plt

# Data from your table
frequency = np.array([50, 250, 1000, 3000, 6000, 18000, 72000, 360000])  # Hz
phase_highpass_unloaded = np.array([97.2, 76.5, 72, 51.84, 28.08, 9.72, 3.11, 1.55])  # Degrees

# New phase data
phase_new_data = np.array([0.917921459323272, 4.58021854050815, 17.7676644579948, 43.8704117010005,
                           62.5204184386838, 80.1643187351204, 87.5181909889923, 89.5033399712733])

# Plot Bode Phase Diagram
plt.figure(figsize=(8, 6))
plt.semilogx(frequency, phase_highpass_unloaded, marker='o', linestyle='-', color='b', label="gemessen")
plt.semilogx(frequency, phase_new_data, marker='x', linestyle='--', color='r', label="theoretisch")

# Set x-axis limits between 10^0 and 10^6
plt.xlim(10**0, 10**6)

# Labels and title
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (Degrees)")
plt.title("Hochpass Unbelastet")
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.legend()

# Show the plot
plt.show()
