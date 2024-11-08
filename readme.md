# Particle Dynamics Simulation and Animation

This project simulates the dynamics of particles on a sphere and visualizes their movement and interaction energy over time using Manim.

## Project Structure

- `simulation.py`: Contains the code to simulate the particle dynamics and compute the trajectory and energy of the system.
- `animation.py`: Contains the code to animate the particle movement on a sphere and the evolution of interaction energy using Manim.
- `trajectory_full.npy`: Numpy file storing the computed trajectory of particles.
- `energy_full.npy`: Numpy file storing the computed interaction energy over time.
- `simulation_params.txt`: Text file storing the simulation parameters.
- `energy_evolution.png`: Plot of the energy evolution over time.

## Requirements

- Python 3.x
- Numpy
- Matplotlib
- Manim

## Installation

1. Clone the repository:# Particle Dynamics Simulation and Animation

This project simulates the dynamics of particles on a sphere and visualizes their movement and interaction energy over time using Manim.

## Project Structure

- `simulation.py`: Contains the code to simulate the particle dynamics and compute the trajectory and energy of the system.
- `animation.py`: Contains the code to animate the particle movement on a sphere and the evolution of interaction energy using Manim.
- `trajectory_full.npy`: Numpy file storing the computed trajectory of particles.
- `energy_full.npy`: Numpy file storing the computed interaction energy over time.
- `simulation_params.txt`: Text file storing the simulation parameters.
- `energy_evolution.png`: Plot of the energy evolution over time.

## Requirements

- Python 3.x
- Numpy
- Matplotlib
- Manim

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install numpy matplotlib manim
    ```

## Running the Simulation

To run the simulation and generate the trajectory and energy data, execute:
```sh
python simulation.py