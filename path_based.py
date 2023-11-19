from manim import *

class CustomShapePathAnimation(Scene):
    def construct(self):
        # Create a custom star shape
        star = Polygon(
            ORIGIN, UP, RIGHT, LEFT, DOWN, color=YELLOW, fill_opacity=1
        )

        # Create a path for animation
        path = Line(LEFT, RIGHT, color=WHITE)

        # Animate the star along the path
        self.play(MoveAlongPath(star, path))
        self.wait(1)
