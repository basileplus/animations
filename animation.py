from manim import *
import numpy as np

# Load precomputed trajectory and energy data
trajectory_full = np.load('trajectory_full.npy')
energy_full = np.load('energy_full.npy')

# Define parameters for rendering
dt = 0.05          # Time step used in the simulation
steps = trajectory_full.shape[0] - 1
n = trajectory_full.shape[1]

class FullModelScene(ThreeDScene):
    """Manim scene to animate particles moving on a sphere."""
    def construct(self):
        # Set background color to white
        self.camera.background_color = WHITE

        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Create a translucent sphere
        sphere = Sphere(radius=2, color=BLACK, fill_opacity=0.01)
        self.add(sphere)

        # Initialize particles at their starting positions
        particles = VGroup(*[
            Dot3D(point=2 * trajectory_full[0][i], color=PURPLE)
            for i in range(n)
        ])
        self.add(particles)

        # Create and position legend
        legend = VGroup(
            Tex("Tokens \\tiny modeled as particles", color=PURPLE),
            Tex("Normalized Space $\\mathbb{S}^{d-1}$", color=GREY),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR)
        self.add_fixed_in_frame_mobjects(legend)

        # Create a ValueTracker for time progression
        time_tracker = ValueTracker(0)

        # Add updater to animate particles
        def update_particles(mob):
            t = time_tracker.get_value()
            index = int(t / dt)
            if index < len(trajectory_full):
                for i in range(n):
                    mob[i].move_to(2 * trajectory_full[index][i])

        particles.add_updater(update_particles)

        # Animate particles over time
        self.play(
            time_tracker.animate.set_value(steps * dt),
            run_time=10,
            rate_func=linear,
        )
        particles.remove_updater(update_particles)

class EnergyGraphScene(Scene):
    """Manim scene to animate the evolution of interaction energy."""
    def construct(self):
        # Set background color to white
        self.camera.background_color = WHITE

        # Create axes for the energy plot
        axes = Axes(
            x_range=[0, steps * dt, steps * dt / 10],
            y_range=[min(energy_full) * 0.95, max(energy_full) * 1.05],
            x_length=10,
            y_length=6,
            tips=False,
            axis_config={"include_ticks": False, "color": BLACK},
        )
        axes.to_edge(DOWN)

        # Create labels for the axes
        x_label = axes.get_x_axis_label(Tex("Time $t$ \\\\ \\tiny Image of progression through layers", color=BLACK))
        y_label = axes.get_y_axis_label(Tex("Interaction Energy $\\mathrm{E}_\\beta$", color=BLACK))

        # Create a ValueTracker for time progression
        time_tracker = ValueTracker(0)

        # Redraw the energy graph as time progresses
        energy_full_graph = always_redraw(lambda: axes.plot_line_graph(
            x_values=np.arange(0, time_tracker.get_value() + dt, dt),
            y_values=energy_full[:int(time_tracker.get_value() / dt) + 1],
            add_vertex_dots=False,
            line_color=PURPLE,
        ))

        # Add axes, labels, and the energy graph to the scene
        self.add(axes, x_label, y_label, energy_full_graph)

        # Animate the energy graph over time
        self.play(
            time_tracker.animate.set_value(steps * dt),
            run_time=10,
            rate_func=linear,
        )


