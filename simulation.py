import numpy as np
import matplotlib.pyplot as plt


# Helper functions for dynamics
def project_onto_tangent(x, y):
    """Project vector y onto the tangent space at point x on S^2."""
    return y - np.dot(x, y) * x

def compute_Z(x_i, x, beta):
    """Compute the partition function Z for particle x_i."""
    return np.sum(np.exp(beta * np.dot(x_i, x.T)))

def compute_dynamics(x, beta):
    """Compute dynamics with normalization (full continuity equation)."""
    n = x.shape[0]
    x_dot = np.zeros_like(x)
    for i in range(n):
        Z = compute_Z(x[i], x, beta)
        # Vectorized computation of sum_interactions
        interaction_terms = np.exp(beta * np.dot(x[i], x.T))[:, np.newaxis] * x
        sum_interactions = np.sum(interaction_terms, axis=0)
        force = project_onto_tangent(x[i], sum_interactions / Z)
        x_dot[i] = force
    return x_dot

def compute_energy(x, beta):
    """Compute the interaction energy of the particle system."""
    n = x.shape[0]
    inner_products = np.dot(x, x.T)
    energy = np.sum(np.exp(beta * inner_products))
    return energy / (2 * beta * n**2)

def track_energy(trajectory, beta):
    """Track energy over time for a given trajectory."""
    energies = [compute_energy(x, beta) for x in trajectory]
    return energies

def integrate(x, beta, dt, steps, dynamics_func):
    """Perform numerical integration to compute the trajectory."""
    trajectory = [x.copy()]
    for _ in range(steps):
        x_dot = dynamics_func(x, beta)
        x += dt * x_dot
        # Normalize to stay on S^2
        x /= np.linalg.norm(x, axis=1, keepdims=True)
        trajectory.append(x.copy())
    return trajectory

# Simulation parameters
n = 20            # Number of particles
d = 3             # Dimensions (for S^2, use d=3)
beta = 10         # Inverse temperature
dt = 0.05         # Time step
steps = 700       # Number of integration steps

# Initial condition: Randomly distributed particles on S^2
x_initial = np.random.normal(size=(n, d))
x_initial /= np.linalg.norm(x_initial, axis=1, keepdims=True)

# Run simulation
trajectory_full = integrate(x_initial.copy(), beta, dt, steps, compute_dynamics)
energy_full = track_energy(trajectory_full, beta)

# Save the trajectory and energy data to files
np.save('trajectory_full.npy', trajectory_full)

# Save simulation parameters to a file (optional)
with open('simulation_params.txt', 'w') as f:
    f.write(f"dt={dt}\n")

# Plot energy evolution
plt.figure()
plt.plot(energy_full)
plt.xlabel('Time step')
plt.ylabel('Energy')
plt.title('Energy Evolution Over Time')
plt.grid(True)
plt.savefig('energy_evolution.png')
plt.show()
np.save('energy_full.npy', energy_full)
