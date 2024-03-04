import tkinter as tk

class FancyCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Fancy Calculator")
        master.geometry("400x600")  # Set initial window size

        # Entry widget for user input
        self.entry = tk.Entry(master, font=('Helvetica', 16), bg='#D0A9E6')  # Purple color
        self.entry.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Buttons for digits 0-9
        buttons_frame = tk.Frame(master)
        buttons_frame.pack()

        for i in range(3):
            for j in range(3):
                digit = i * 3 + j + 1
                self.create_button(buttons_frame, str(digit), row=i, column=j, command=lambda digit=digit: self.entry.insert(tk.END, str(digit)), bg='#FAC8F7')  # Pink color

        # Special buttons: 0, ., =
        self.create_button(buttons_frame, "0", row=3, column=0, command=lambda: self.entry.insert(tk.END, "0"), bg='#FAC8F7')  # Pink color
        self.create_button(buttons_frame, ".", row=3, column=1, command=lambda: self.entry.insert(tk.END, "."), bg='#FAC8F7')  # Pink color

        equals_btn = self.create_button(buttons_frame, "=", row=3, column=2, command=self.calculate, bg='#D0A9E6')  # Purple color

        # Operator buttons: +, -, *, /
        operators_frame = tk.Frame(master)
        operators_frame.pack()

        operators = ['+', '-', '*', '/']
        for i, operator in enumerate(operators):
            self.create_button(operators_frame, operator, row=i, column=0, command=lambda operator=operator: self.entry.insert(tk.END, operator), bg='#D0A9E6')  # Purple color

        # Button to clear the entry widget
        clear_btn = self.create_button(operators_frame, "Clear", row=len(operators), column=0, command=lambda: self.entry.delete(0, tk.END), bg='#D0A9E6')  # Purple color

        # Text widget to display the result
        self.result_text = tk.Text(master, height=2, font=('Helvetica', 16), bg='#FAC8F7')  # Pink color
        self.result_text.pack(pady=10)

    def create_button(self, frame, text, row, column, command=None, bg=None):
        btn = tk.Button(frame, text=text, padx=20, pady=10, font=('Helvetica', 12), command=command, bg=bg)
        btn.grid(row=row, column=column, padx=5, pady=5)
        return btn

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.result_text.config(state=tk.NORMAL)  # Allow modification
            self.result_text.delete(1.0, tk.END)  # Clear previous content
            self.result_text.insert(tk.END, str(result))
        except Exception as e:
            error_message = f"Error: {e}"
            self.result_text.config(state=tk.NORMAL)  # Allow modification
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, error_message)
        finally:
            self.result_text.config(state=tk.DISABLED)  # Disable modification

def run_calculator():
    root = tk.Tk()
    app = FancyCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    run_calculator()
