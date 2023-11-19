from manim import *

class CoordinateSystemsExample(Scene):
    def construct(self):
        # Create a Cartesian coordinate system
        cartesian_axes = Axes(
            x_range=[-2, 2],
            y_range=[-1, 1],
            axis_config={"color": BLUE},
        )

        # Create a polar coordinate system
        polar_axes = PolarAxes(
            azimuthal_angle_range=[0, TAU],
            radius_range=[0, 1],
            axis_config={"color": GREEN},
        )

        self.play(Create(cartesian_axes), Create(polar_axes))
        self.wait(1)
