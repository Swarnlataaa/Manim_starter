from manim import *

class FirstScene(Scene):
    def construct(self):
        text = Text("This is the first scene")
        self.play(Create(text))
        self.wait(1)

class SecondScene(Scene):
    def construct(self):
        text = Text("This is the second scene")
        self.play(Create(text))
        self.wait(1)

if __name__ == "__main__":
    my_scenes = [FirstScene, SecondScene]
    for i in range(len(my_scenes) - 1):
        scene1 = my_scenes[i]()
        scene2 = my_scenes[i + 1]()
        scene1.play(FadeOut(scene1, shift=UP))
        scene1.play(scene1.animate.shift(DOWN))
        scene1.wait(1)
