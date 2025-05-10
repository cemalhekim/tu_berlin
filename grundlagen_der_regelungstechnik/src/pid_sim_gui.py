import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Define the system dynamics
def system_dynamics(y, u, a=1.0, b=1.0):
    """Simple first-order system: dy/dt + ay = bu."""
    return -a * y + b * u

# PID Controller
class PIDController:
    def __init__(self, kp=1.0, ki=0.5, kd=0.1, setpoint=1.0):
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

# GUI Setup
root = tk.Tk()
root.title("PID Controller Simulation")

# Variables
kp_var = tk.DoubleVar(value=1.0)
ki_var = tk.DoubleVar(value=0.5)
kd_var = tk.DoubleVar(value=0.1)
setpoint_var = tk.DoubleVar(value=1.0)
time_var = tk.DoubleVar(value=10.0)
dt_var = tk.DoubleVar(value=0.01)

kp_var.trace_add("write", lambda *args: run_simulation())
ki_var.trace_add("write", lambda *args: run_simulation())
kd_var.trace_add("write", lambda *args: run_simulation())
setpoint_var.trace_add("write", lambda *args: run_simulation())
time_var.trace_add("write", lambda *args: run_simulation())
dt_var.trace_add("write", lambda *args: run_simulation())

# Run Simulation
def run_simulation():
    # Simulation Parameters
    kp = kp_var.get()
    ki = ki_var.get()
    kd = kd_var.get()
    setpoint = setpoint_var.get()
    sim_time = time_var.get()
    dt = dt_var.get()

    time = np.arange(0, sim_time, dt)
    pid = PIDController(kp, ki, kd, setpoint)
    y = 0  # Initial state
    output = []

    for t in time:
        u = pid.compute(y, dt)
        y = y + system_dynamics(y, u) * dt
        output.append(y)

    # Plot the results
    ax.clear()
    ax.plot(time, output, label="PID Controlled Output")
    ax.axhline(setpoint, color='r', linestyle='--', label="Setpoint")
    ax.set_title("PID Controller Simulation")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Output")
    ax.legend()
    ax.grid()
    canvas.draw()

# GUI Layout
frame = tk.Frame(root)
frame.pack(side=tk.LEFT, padx=10, pady=10)

# PID Gains
tk.Label(frame, text="Kp").grid(row=0, column=0)
tk.Scale(frame, from_=0.0, to=5.0, resolution=0.1, orient=tk.HORIZONTAL, variable=kp_var).grid(row=0, column=1)
tk.Entry(frame, textvariable=kp_var).grid(row=0, column=2)

tk.Label(frame, text="Ki").grid(row=1, column=0)
tk.Scale(frame, from_=0.0, to=5.0, resolution=0.1, orient=tk.HORIZONTAL, variable=ki_var).grid(row=1, column=1)
tk.Entry(frame, textvariable=ki_var).grid(row=1, column=2)

tk.Label(frame, text="Kd").grid(row=2, column=0)
tk.Scale(frame, from_=0.0, to=5.0, resolution=0.1, orient=tk.HORIZONTAL, variable=kd_var).grid(row=2, column=1)
tk.Entry(frame, textvariable=kd_var).grid(row=2, column=2)

# Setpoint
tk.Label(frame, text="Setpoint").grid(row=3, column=0)
tk.Entry(frame, textvariable=setpoint_var).grid(row=3, column=1)

# Simulation Time and Step Size
tk.Label(frame, text="Simulation Time (s)").grid(row=4, column=0)
tk.Entry(frame, textvariable=time_var).grid(row=4, column=1)

tk.Label(frame, text="Time Step (dt)").grid(row=5, column=0)
tk.Entry(frame, textvariable=dt_var).grid(row=5, column=1)

# Run Button
tk.Button(frame, text="Run", command=run_simulation).grid(row=6, column=0, columnspan=3, pady=10)

# Plot Area
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.RIGHT, padx=10, pady=10)

root.bind('<Return>', lambda event: run_simulation())

# Start the GUI
root.mainloop()
