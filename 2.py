from manim import *

class TransformExample(Scene):
    def construct(self):
        # Create a circle
        circle = Circle()
        circle.set_fill(RED, opacity=0.5)

        # Display the circle
        self.play(Create(circle))

        # Move the circle to a new position
        self.play(circle.animate.shift(2 * UP + 3 * RIGHT))
        self.wait(1)
