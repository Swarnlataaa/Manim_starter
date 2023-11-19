from manim import *

class TextAndLatexExample(Scene):
    def construct(self):
        # Adding plain text
        text = Text("Hello, ManimCE!")
        self.play(Create(text))
        self.wait(1)

        # Adding a LaTeX expression
        latex_expression = MathTex(r"\frac{1}{2} \cdot \sqrt{x^2 + 1}")
        self.play(Create(latex_expression))
        self.wait(1)
