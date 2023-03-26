import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Define the differential equation for the pendulum motion
def pendulum(t, y, L):
    theta, omega = y
    dydt = [omega, -(9.81/L)*np.sin(theta)]
    return dydt

# initial conditions are here!
theta0 = np.deg2rad(30)
omega0 = 0 
y0 = [theta0, omega0]

# set the length
L = 2

# time range
t_span = [0, 20]
t_eval = np.linspace(0, 20, 500)

# Solve the differentail equation
sol = solve_ivp(pendulum, t_span, y0, args=(L,), t_eval=t_eval)

# Extract the solution data
theta = sol.y[0]

# Convert the angle to x-y coordinates for plotting
x = L*np.sin(theta)
y = -L*np.cos(theta)

# Define the animation function
def animate(i):
    # Plot the pendulum
    plt.cla()
    plt.plot([0, x[i]], [0, y[i]], lw=2, color='blue')
    plt.plot(x[i], y[i], 'o', color='blue', markersize=10)
    plt.xlim(-1.1*L, 1.1*L)
    plt.ylim(-1.1*L, 0)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Pendulum Motion')

# Create the animation
anim = FuncAnimation(plt.gcf(), animate, frames=len(t_eval), interval=50)

# Display the animation
# plt.show()
