import numpy as np
import matplotlib.pyplot as plt

# Define the system dynamics
def system_dynamics(y, u, a=1.0, b=1.0):
    """Simple first-order system: dy/dt + ay = bu."""
    return -a * y + b * u

# PID Controller
class PIDController:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.integral = 0
        self.prev_error = 0

    def compute(self, y, dt):
        """Compute PID output."""
        error = self.setpoint - y
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative

# Simulation parameters
dt = 0.01  # Time step
time = np.arange(0, 10.0, dt)  # Simulation time
setpoint = 1  # Desired value
kp, ki, kd = 1.0, 1.0, 0.5  # PID gains

# Initialize
pid = PIDController(kp, ki, kd, setpoint)
y = 0  # Initial system state
u = 0  # Initial control input
output = []  # To store system output

y_uncontrolled = 0  # Initial state for the uncontrolled system
uncontrolled_output = []  # To store the uncontrolled system output

for t in time:
    u = pid.compute(y, dt)  # PID control
    y = y + system_dynamics(y, u) * dt  # Update controlled system state
    y_uncontrolled = y_uncontrolled + system_dynamics(y_uncontrolled, 0) * dt  # Uncontrolled system
    output.append(y)
    uncontrolled_output.append(y_uncontrolled)

plt.figure(figsize=(10, 5))
plt.plot(time, output, label="PID Controlled Output")
plt.plot(time, uncontrolled_output, label="Uncontrolled Output", linestyle='--')
plt.axhline(setpoint, color='r', linestyle='--', label="Setpoint")
plt.title("PID Controller Simulation with Uncontrolled System")
plt.xlabel("Time (s)")
plt.ylabel("Output")
plt.legend()
plt.grid()
plt.show()

