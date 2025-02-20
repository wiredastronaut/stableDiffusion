import matplotlib.pyplot as plt
import numpy as np
import random

# Number of plots to generate
num_plots = 6

# Define the x values and parameters for the Gaussian distributions
x = np.linspace(-4, 4, 400)
mu_initial, sigma0 = 0, 1
mean_shifts = np.zeros(num_plots)

# Initialize the mean for the first distribution
mean_shifts[0] = mu_initial

# Create the figure with multiple subplots
fig, axes = plt.subplots(num_plots, 1, figsize=(8, 12))

# Loop through each plot
for i, ax in enumerate(axes):
    ax.set_title(f'Timestep t = {i}')
    if i > 0:
        # Randomly sample a value from the previous distribution
        mean_shifts[i] = random.gauss(mean_shifts[i - 1], sigma0)

    # Calculate the Gaussian distribution
    if i == 0:
        y = (1 / (np.sqrt(2 * np.pi) * sigma0)) * np.exp(-0.5 * ((x - mu_initial) / sigma0)**2)
    else:
        y = (1 / (np.sqrt(2 * np.pi) * sigma0)) * np.exp(-0.5 * ((x - mean_shifts[i-1]) / sigma0)**2)


    # Plot the Gaussian distribution
    ax.plot(x, y, color='orange')

    # Plot the initial mean line
    if i == 0:
        ax.axvline(mu_initial, color='k', linestyle='--')
    else:
        ax.axvline(mean_shifts[i-1], color='k', linestyle='--')

    # Plot the sampled line
    sampled_line_position = mean_shifts[i]
    ax.axvline(sampled_line_position, color='red', linestyle='-', linewidth=2)

    # Grid and labels
    ax.set_xlabel('x')
    ax.set_ylabel('Density')
    ax.grid(True)

# Adjust layout and display the plot
plt.tight_layout()
plt.savefig('multiple_gaussian_plots.png')
plt.show()
