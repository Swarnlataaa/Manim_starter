from manim import *

class TweeningInterpolationExample(Scene):
    def construct(self):
        # Create a square
        square = Square()

        # Move the square using interpolation
        self.play(
            square.animate.shift(2 * UP).interpolate(
                square.animate.shift(2 * RIGHT), 0.5, smooth
            )
        )
        self.wait(1)
