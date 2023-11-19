from manim import *

class EasingFunctionExample(Scene):
    def construct(self):
        # Create a square
        square = Square()

        # Move the square with an easing function
        self.play(square.animate.shift(2 * RIGHT).shift(2 * UP).shift(2 * LEFT).shift(2 * DOWN).shift(2 * RIGHT), run_time=2, rate_func=there_and_back)
        self.wait(1)
