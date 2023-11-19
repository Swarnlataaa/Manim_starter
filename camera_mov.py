from manim import *

class CameraMovementExample(Scene):
    def construct(self):
        # Create a square and a circle
        square = Square()
        circle = Circle()

        # Display the square and circle
        self.play(Create(square), Create(circle))
        self.wait(1)

        # Move the camera to focus on the circle
        self.camera.frame.animate.shift(2 * RIGHT)
        self.wait(1)

        # Move the camera back to the original position
        self.camera.frame.animate.shift(2 * LEFT)
        self.wait(1)
