from manim import *

class GroupingExample(Scene):
    def construct(self):
        # Create squares
        square1 = Square()
        square2 = Square()
        square2.shift(RIGHT * 2)

        # Group the squares
        squares_group = VGroup(square1, square2)

        # Display the group
        self.play(Create(squares_group))
        self.wait(1)
