import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Samriddhi's Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.display = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 14), padding=10)
        style.configure('TEntry', font=('Helvetica', 24))

        display_frame = ttk.Frame(self.root, padding="10")
        display_frame.pack(side=tk.TOP, fill=tk.BOTH)

        display_entry = ttk.Entry(display_frame, textvariable=self.display, font=("Helvetica", 24), justify='right', state='readonly', style='TEntry')
        display_entry.pack(expand=True, fill='both')

        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(expand=True, fill='both', padx=10, pady=10)

        buttons = [
            ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2, 1, 2),
        ]

        for (text, row, col, rowspan, colspan) in [(*button, 1, 1) if len(button) == 3 else button for button in buttons]:
            button = ttk.Button(buttons_frame, text=text, command=lambda t=text: self.on_button_click(t), style='TButton')
            button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        for i in range(6):
            buttons_frame.rowconfigure(i, weight=1)
            buttons_frame.columnconfigure(i % 4, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.display.set('')
        elif char == '=':
            try:
                result = eval(self.display.get())
                self.display.set(result)
            except Exception as e:
                self.display.set('Error')
        else:
            current_text = self.display.get()
            new_text = current_text + char
            self.display.set(new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
