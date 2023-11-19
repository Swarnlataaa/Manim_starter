from manim import *

class KeyframeExample(Scene):
    def construct(self):
        # Create an object
        square = Square()

        # Start the animation with the square at the center
        self.play(Create(square))

        # Define a keyframe at 1 second with a new position and color
        self.wait(1)
        self.play(
            square.animate
            .shift(2 * RIGHT)
            .set_color(RED)
        )

        # Another keyframe at 2 seconds with different properties
        self.wait(1)
        self.play(
            square.animate
            .rotate(90 * DEGREES)
            .scale(0.5)
        )

        # Continue animating to the end
        self.wait(1)
        self.play(FadeOut(square))
