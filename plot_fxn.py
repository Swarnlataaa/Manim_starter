from manim import *

class PlottingExample(Scene):
    def construct(self):
        # Create a Cartesian coordinate system
        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1, 1],
            axis_config={"color": BLUE},
        )

        # Plot a sine wave
        sine_graph = axes.plot(lambda x: np.sin(x), color=RED)

        # Define data points
        data_points = [(PI/2, 0), (PI, 1), (3*PI/2, 0), (2*PI, -1)]

        # Plot data points
        data_graph = axes.plot_points(data_points, color=GREEN, marker="o", radius=0.08)

        self.play(Create(axes), Create(sine_graph), Create(data_graph))
        self.wait(1)
