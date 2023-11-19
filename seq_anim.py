from manim import *

class SequentialAnimationExample(Scene):
    def construct(self):
        # Create objects
        square = Square()
        circle = Circle()

        # Display the square first
        self.play(Create(square))
        self.wait(1)

        # Then display the circle
        self.play(Create(circle))
        self.wait(1)
