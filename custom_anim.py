from manim import *

class CustomAnimationStyleExample(Scene):
    def construct(self):
        # Create a square
        square = Square()

        # Move the square with a custom style
        self.play(
            square.animate.shift(2 * UP).interpolate(
                square.animate.shift(2 * RIGHT), 0.5, smooth
            ).interpolate(
                square.animate.shift(2 * UP), 0.5, linear
            ).interpolate(
                square.animate.shift(2 * RIGHT), 0.5, there_and_back
            ).interpolate(
                square.animate.shift(2 * UP), 0.5, there_and_back
            ),
            run_time=4,
        )
        self.wait(1)
