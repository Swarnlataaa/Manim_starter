from manim import *

class CombinedAnimationExample(Scene):
    def construct(self):
        # Create objects
        square = Square()
        circle = Circle()

        # Display the square and circle simultaneously
        self.play(Create(square), Create(circle))
        self.wait(1)

        # Animate the square and circle sequentially
        self.play(
            square.animate.shift(UP),
            circle.animate.shift(DOWN),
        )
        self.wait(1)
