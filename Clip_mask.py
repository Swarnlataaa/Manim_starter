from manim import *

class ClippingMaskingExample(Scene):
    def construct(self):
        # Create a square and a circle
        square = Square()
        circle = Circle()

        # Use the circle as a mask for the square
        square.set_fill(BLUE, opacity=1)
        square.set_stroke(width=0)
        square.save_state()
        square.set_fill(opacity=0)
        square.next_to(circle, RIGHT)
        self.play(Restore(square))
        self.wait(1)
