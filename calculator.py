import tkinter as tk
from math import *

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("540x550")
        self.resizable(False, False)
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
        self.display.grid(row=0, column=0, columnspan=6, pady=20, sticky="we")

        btns = [
            ('7', '8', '9', '/', 'sqrt', 'C'),
            ('4', '5', '6', '*', 'pow', '('),
            ('1', '2', '3', '-', 'log', ')'),
            ('0', '.', '+', '=', 'sin', 'cos'),
            ('tan', 'exp', 'pi', 'e', 'abs', 'fact')
        ]

        for r, row in enumerate(btns, 1):
            for c, btn in enumerate(row):
                action = lambda x=btn: self.on_click(x)
                tk.Button(self, text=btn, width=6, height=2, font=("Arial", 16),
                          command=action).grid(row=r, column=c, padx=2, pady=2)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = self.safe_eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        elif char == 'sqrt':
            self.expression += "sqrt("
            self.display.insert(tk.END, "sqrt(")
        elif char == 'pow':
            self.expression += "**"
            self.display.insert(tk.END, "^")
        elif char == 'log':
            self.expression += "log("
            self.display.insert(tk.END, "log(")
        elif char == 'sin':
            self.expression += "sin("
            self.display.insert(tk.END, "sin(")
        elif char == 'cos':
            self.expression += "cos("
            self.display.insert(tk.END, "cos(")
        elif char == 'tan':
            self.expression += "tan("
            self.display.insert(tk.END, "tan(")
        elif char == 'exp':
            self.expression += "exp("
            self.display.insert(tk.END, "exp(")
        elif char == 'pi':
            self.expression += "pi"
            self.display.insert(tk.END, "π")
        elif char == 'e':
            self.expression += "e"
            self.display.insert(tk.END, "e")
        elif char == 'abs':
            self.expression += "abs("
            self.display.insert(tk.END, "abs(")
        elif char == 'fact':
            self.expression += "factorial("
            self.display.insert(tk.END, "fact(")
        else:
            self.expression += str(char)
            self.display.insert(tk.END, str(char))

    def safe_eval(self, expr):
        allowed_names = {k: v for k, v in globals().items() if k in [
            'sin', 'cos', 'tan', 'sqrt', 'log', 'exp', 'pi', 'e', 'abs', 'factorial', 'pow']}
        allowed_names.update({'__builtins__': None})
        return eval(expr, allowed_names, {})

if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()