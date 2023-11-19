from manim import *

class ParallelAnimationExample(Scene):
    def construct(self):
        # Create objects
        square = Square()
        circle = Circle()

        # Display the square and circle simultaneously
        self.play(Create(square), Create(circle))
        self.wait(1)
