from toga import App, MainWindow, Button, TextInput, Box
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import math
import matplotlib.pyplot as plt
import numpy as np

class CalculatorApp(App):
    def startup(self):
        self.main_window = MainWindow(title="Scientific Calculator")

        # Create input field
        self.input = TextInput(readonly=True, style=Pack(flex=1))

        # Create buttons
        buttons = [
            ('7', self.on_button_press), ('8', self.on_button_press), ('9', self.on_button_press), ('/', self.on_button_press),
            ('4', self.on_button_press), ('5', self.on_button_press), ('6', self.on_button_press), ('*', self.on_button_press),
            ('1', self.on_button_press), ('2', self.on_button_press), ('3', self.on_button_press), ('-', self.on_button_press),
            ('0', self.on_button_press), ('.', self.on_button_press), ('=', self.on_calculate), ('+', self.on_button_press),
            ('C', self.on_clear), ('(', self.on_button_press), (')', self.on_button_press), ('sin', self.on_button_press),
            ('cos', self.on_button_press), ('tan', self.on_button_press), ('log', self.on_button_press), ('sqrt', self.on_button_press),
            ('plot', self.on_plot)
        ]

        # Create a grid layout
        grid = Box(style=Pack(direction=COLUMN, padding=10))
        grid.add(self.input)

        for i in range(0, len(buttons), 4):
            row = Box(style=Pack(direction=ROW))
            for label, handler in buttons[i:i+4]:
                button = Button(label, on_press=handler, style=Pack(flex=1, padding=5))
                row.add(button)
            grid.add(row)

        self.main_window.content = grid
        self.main_window.show()

    def on_button_press(self, widget):
        self.input.value += widget.text

    def on_calculate(self, widget):
        try:
            # Replace scientific functions with their math module equivalents
            expression = self.input.value.replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan')
            expression = expression.replace('log', 'math.log').replace('sqrt', 'math.sqrt')
            self.input.value = str(eval(expression))
        except Exception:
            self.input.value = "Error"

    def on_clear(self, widget):
        self.input.value = ""

    def on_plot(self, widget):
        try:
            # Evaluate the expression and plot the result
            x = np.linspace(-10, 10, 400)
            y = eval(self.input.value.replace('x', 'x'))
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Plot')
            plt.grid(True)
            plt.show()
        except Exception:
            self.input.value = "Error"

if __name__ == "__main__":
    CalculatorApp("Scientific Calculator", "org.beeware.demo").main_loop()