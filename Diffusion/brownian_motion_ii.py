import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # Use Tkinter instead of Qt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

#Generate swiss roll distribution
length_phi = 15   #length of swiss roll in angular direction
sigma = 0.03  #noise strength
m = 300    #number of samples

#create the dataset
phi = length_phi * np.random.rand(m)
phi = length_phi * np.linspace(0, 1, m)
xi = np.random.rand(m)
X = 1./6*(phi + sigma*xi)*np.sin(phi)
Y = 1./6*(phi + sigma*xi)*np.cos(phi)
swiss_roll = np.array([X, Y]).transpose()
# now display
plt.scatter(X, Y, marker=".", c = phi, cmap = "viridis")
plt.show()



#Times
x = np.linspace(0, 1, 100)
ts = 0.1 * x**2

#Position over time
positions = []
positions.append(swiss_roll)

#Initial definition
current_time = ts[0]
current_positions = swiss_roll
#Step through time
for i in range(1, len(ts)):
    #New state time
    new_time = ts[i]
    time_delta = new_time - current_time
    #Randomly sample from the zero mean gaussian to get a position step,
    #variance is scaled by time delta. Do this for the number of samples within
    #swiss_roll
    #position_step = random.gauss(0, np.sqrt(time_delta))
    position_steps = np.random.normal(0, np.sqrt(time_delta), size=swiss_roll.shape)
    #Using the sampled position step, move the particle forward
    new_positions = current_positions + position_steps
    positions.append(new_positions)
    #Update current state
    current_positions = new_positions
    current_time = new_time

# Animation
fig, ax = plt.subplots()    
sc = ax.scatter([], [], cmap='viridis', marker='.')

#Plot limits
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_title("Brownian Motion of Swiss Roll")
def update(frame):
    new_positions = positions[frame]
    sc.set_offsets(positions[frame])
    sc.set_array(phi)
    return sc,


ani = animation.FuncAnimation(fig, update, frames=len(positions),
                              interval=100)

ani.save('brownian_motion_swiss_roll.gif', writer='pillow', fps=10)
plt.show()


