import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.animation as animation

# Number of frames for the animation
num_frames = 20

# Define the x values and parameters for the Gaussian distributions
x = np.linspace(-4, 4, 400)
mu_initial, sigma0 = 0, 1
mean_shifts_anim = np.linspace(0, 3, num_frames)

# Create a figure for the animation
fig, ax = plt.subplots(figsize=(8, 6))

# Initialize the plot elements we will update
line, = ax.plot([], [], color='orange')
mean_line = ax.axvline(0, color='k', linestyle='--')
sample_line = ax.axvline(0, color='red', linestyle='-', linewidth=2)
prev_mean_line = ax.axvline(0, color='blue', linestyle='--', linewidth=1)
time_text = ax.text(3, 0.3, '', fontsize=12, fontweight='bold')

# Set plot limits and labels
ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.45)
ax.set_xlabel('x')
ax.set_ylabel('Density')
ax.grid(True)

# Initialization function for the animation
def init():
    line.set_data([], [])
    mean_line.set_xdata([0])
    sample_line.set_xdata([0])
    prev_mean_line.set_xdata([0])
    time_text.set_text('')
    return line, mean_line, sample_line, prev_mean_line, time_text

# Update function for each frame
def update(frame):
    # Randomly sample a value from the current distribution
    #current_mean = mu_initial + mean_shifts_anim[frame]
    if frame > 0:
      current_mean = mean_shifts_anim[frame-1]
    else:
      current_mean = mu_initial
      
    sampled_value = random.gauss(current_mean, sigma0)
    # Calculate the Gaussian distribution
    y = (1 / (np.sqrt(2 * np.pi) * sigma0)) * np.exp(-0.5 * ((x - current_mean) / sigma0)**2)

    # Update plot elements
    line.set_data(x, y)
    mean_line.set_xdata([current_mean])
    sample_line.set_xdata([sampled_value])
    mean_shifts_anim[frame] = sampled_value
  
    
    prev_mean_line.set_xdata([mu_initial])
    time_text.set_text(f'$t = {frame}$')
    
    return line, mean_line, sample_line, prev_mean_line, time_text

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True)

# Save the animation as a .gif
gif_path = 'gaussian_diffusion_process_random.gif'
ani.save(gif_path, writer='pillow', fps=1)

print(f'Animation saved as {gif_path}')