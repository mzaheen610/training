import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        self.result_var = tk.StringVar()
        self.create_ui()

    def create_ui(self):
        # Entry field for displaying the expression and result
        entry = tk.Entry(self.root, textvariable=self.result_var, font=("Helvetica", 20), justify="right")
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row, col = 1, 0
        for button in buttons:
            tk.Button(self.root, text=button, font=("Helvetica", 15), command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif button == "C":
            self.expression = ""
        else:
            self.expression += button
        self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
