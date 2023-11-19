from manim import *

class TextAndLatexFormattingExample(Scene):
    def construct(self):
        # Formatting plain text
        text = Text("Hello, ManimCE!", color=BLUE, size=0.6)
        self.play(Create(text))
        self.wait(1)

        # Formatting a LaTeX expression
        latex_expression = MathTex(
            r"\frac{1}{2} \cdot \sqrt{x^2 + 1}",
            color=YELLOW,
            size=0.8,
        )
        self.play(Create(latex_expression))
        self.wait(1)
