import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # Use Tkinter instead of Qt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random



#Times
ts = np.linspace(0, 100, 50)
starting_position = 0
#Position over time
positions = []
positions.append(starting_position)
#Probability density over time
densities = []
densities.append(1)

#Initial definition
current_time = ts[0]
current_position = starting_position
#Step through time
for i in range(1, len(ts)):
    #New state time
    new_time = ts[i]
    time_delta = new_time - current_time
    #Randomly sample from the zero mean gaussian to get a position step,
    #variance is scaled by time delta
    position_step = random.gauss(0, np.sqrt(time_delta))
    #Using the sampled position step, move the particle forward
    new_position = current_position + position_step
    #Identify the probability associated with that step using transition probability
    transition_density = ( 
        1/(np.sqrt(2 * np.pi * (time_delta))) * 
        np.exp(-((new_position - current_position)**2)/(2 * (time_delta)))
    )
    #Store
    positions.append(new_position)
    #Probability of observing x given y equals p(y) * p(x|y)
    densities.append(densities[-1] * transition_density)
    #Update current state
    current_position = new_position
    current_time = new_time

#Plot
plt.figure(figsize=(12, 5))
plt.plot(ts, positions, label="Particle Path")
plt.title("Brownian Motion Path")
plt.xlabel("Time")
plt.ylabel("Position")
plt.legend()
plt.grid(True, linestyle='-', linewidth=0.3, color='gray', alpha=0.5)
plt.show()

# Plot likelihood evolution
plt.figure(figsize=(12, 5))
plt.plot(ts, densities, label="Cumulative Likelihood")
plt.title("Trajectory Likelihood Over Time")
plt.xlabel("Time")
plt.ylabel("Likelihood")
plt.yscale("log")  # Log scale for better visualization of decreasing likelihood
plt.legend()
plt.grid(True, linestyle='-', linewidth=0.3, color='gray', alpha=0.5)
plt.show()



