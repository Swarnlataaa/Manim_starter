from manim import *

class TextPositioningExample(Scene):
    def construct(self):
        # Positioning and aligning plain text
        text = Text("Centered Text", x=0, y=0, alignment="center")
        self.play(Create(text))
        self.wait(1)

        # Positioning and aligning a LaTeX expression
        latex_expression = MathTex(
            r"\frac{1}{2} \cdot \sqrt{x^2 + 1}",
            x=-2,
            y=2,
            alignment="left",
        )
        self.play(Create(latex_expression))
        self.wait(1)
