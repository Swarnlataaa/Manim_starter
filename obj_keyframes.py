from manim import *

class CameraKeyframeExample(Scene):
    def construct(self):
        # Create a square
        square = Square()

        # Start the animation with the square at the center
        self.play(Create(square))

        # Define a camera keyframe at 1 second to zoom in on the square
        self.wait(1)
        self.camera.frame.animate.move_to(square.get_center()).set(width=2.5)
        self.play(self.camera.frame.animate.shift(UP))

        # Define another camera keyframe at 2 seconds to zoom out
        self.wait(1)
        self.camera.frame.animate.set(width=12)
        self.play(self.camera.frame.animate.shift(DOWN))

        # Continue animating to the end
        self.wait(1)
        self.play(FadeOut(square))
