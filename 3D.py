from manim import *

class ThreeDExample(ThreeDScene):
    def construct(self):
        # Create a 3D cube
        cube = Cube()
        cube.set_fill(BLUE, opacity=0.5)

        # Display the cube in the 3D scene
        self.play(Create(cube))
        self.wait(1)
