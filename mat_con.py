from manim import *

class AnimationExample(Scene):
    def construct(self):
        # Create a Cartesian coordinate system
        axes = Axes(
            x_range=[-2, 2],
            y_range=[-1, 1],
            axis_config={"color": BLUE},
        )

        # Plot a sine wave
        sine_graph = axes.plot(lambda x: np.sin(x), color=RED)

        # Animate the sine wave
        self.play(Create(axes), Create(sine_graph))
        self.wait(1)

        # Transform the sine wave to a cosine wave
        self.play(Transform(sine_graph, axes.plot(lambda x: np.cos(x), color=GREEN)))
        self.wait(1)
