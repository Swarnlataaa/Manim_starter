from manim import *

class ShapesExample(Scene):
    def construct(self):
        # Create a square
        square = Square()
        square.set_fill(RED, opacity=0.5)

        # Create a circle
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)

        # Display shapes
        self.play(Create(square))
        self.wait(1)
        self.play(Create(circle))
        self.wait(1)
