from manim import *

class MyFirstScene(Scene):
    def construct(self):
        # Create objects in the first scene
        square = Square()
        square.set_fill(RED, opacity=0.5)
        self.play(Create(square))
        self.wait(1)

class MySecondScene(Scene):
    def construct(self):
        # Create objects in the second scene
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        self.play(Create(circle))
        self.wait(1)

if __name__ == "__main__":
    my_scenes = [MyFirstScene, MySecondScene]
    for scene in my_scenes:
        scene = scene()
        scene.render()
