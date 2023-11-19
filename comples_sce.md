In Manim Community Edition (ManimCE), you can create complex scenes by combining multiple objects and animations. Sequential and parallel animations allow you to orchestrate the order and timing of these elements. Let's explore these concepts with code examples:

**Sequential Animations:**

Sequential animations are used to animate objects one after the other. You can use the `play()` method to add animations in sequence.

Here's an example of animating multiple objects sequentially:

```python
from manim import *

class SequentialAnimationExample(Scene):
    def construct(self):
        # Create objects
        square = Square()
        circle = Circle()

        # Display the square first
        self.play(Create(square))
        self.wait(1)

        # Then display the circle
        self.play(Create(circle))
        self.wait(1)
```

In this code, we create a square and a circle and animate them sequentially.

**Parallel Animations:**

Parallel animations allow you to animate objects simultaneously. You can use the `play()` method with multiple animations to achieve this.

Here's an example of animating multiple objects in parallel:

```python
from manim import *

class ParallelAnimationExample(Scene):
    def construct(self):
        # Create objects
        square = Square()
        circle = Circle()

        # Display the square and circle simultaneously
        self.play(Create(square), Create(circle))
        self.wait(1)
```

In this code, we create a square and a circle and animate them in parallel.

**Combining Sequential and Parallel Animations:**

You can combine sequential and parallel animations to create more complex scenes. Here's an example of doing this:

```python
from manim import *

class CombinedAnimationExample(Scene):
    def construct(self):
        # Create objects
        square = Square()
        circle = Circle()

        # Display the square and circle simultaneously
        self.play(Create(square), Create(circle))
        self.wait(1)

        # Animate the square and circle sequentially
        self.play(
            square.animate.shift(UP),
            circle.animate.shift(DOWN),
        )
        self.wait(1)
```

In this code, we first display the square and circle in parallel, and then we animate them sequentially by shifting them in different directions.

These examples illustrate how to build complex scenes by combining multiple objects and animations in ManimCE. You can use sequential and parallel animations to create a wide range of visual effects and storytelling in your animations.
