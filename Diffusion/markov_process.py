import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # Use Tkinter instead of Qt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

steps = 50
extent = 2
starting_position = np.array([0,0])
current_state = starting_position
path = np.zeros((steps+1, 2))
for s in range(steps):
    #sample off the motion's probabilistic distribution
    motion_vector = np.random.randint(int(-extent/2), int(extent/2)+1, size=(1, 2))
    #Update the current state
    path[s, :] = current_state
    current_state = motion_vector + current_state
path[steps,:] = current_state


# Set up figure
fig, ax = plt.subplots(figsize=(8, 8))
#Set the limits of the plot
ax.set_xlim(path[:, 0].min() - 1, path[:, 0].max() + 1)
ax.set_ylim(path[:, 1].min() - 1, path[:, 1].max() + 1)
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")
ax.set_title("2D Random Walk Animation")
ax.grid(True, linestyle='-', linewidth=0.3, color='gray', alpha=0.5)

# Color range for smooth transition

cmap = plt.get_cmap("viridis")
norm = plt.Normalize(vmin=0, vmax=steps)
colors = cmap(norm(np.arange(steps + 1)))  

#fig = plt.figure(figsize=(10,10))
#plt.scatter(path[:,0], path[:,1], cmap='viridis', c=color, marker='o', edgecolors='black')
#plt.plot(path[:, 0], path[:,1], cmap='viridis', c=color)
#plt.show()
# Empty plotting elements that will get updated
scatter = ax.scatter([], [], marker='o')
line, = ax.plot([], [], linestyle='-', color='gray', alpha=0.5, linewidth=1)



def update(frame):
    line.set_data(path[0:frame+1, 0], path[0:frame+1, 1])    
    scatter.set_offsets(path[0:frame+1])
    scatter.set_facecolors(colors[0:frame+1])
    return scatter


ani = animation.FuncAnimation(fig, update, frames=steps + 1, interval=100, blit=False)
ani.save("random_walk.gif", writer=animation.PillowWriter(fps=20))

plt.show()




