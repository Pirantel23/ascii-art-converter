import tkinter as tk

class TextViewer:
    def __init__(self, master, text="", font_size=12):
        self.font_size = font_size
        self.master = master
        self.scrollbarX = tk.Scrollbar(self.master, orient=tk.HORIZONTAL)
        self.scrollbarY = tk.Scrollbar(self.master, orient=tk.VERTICAL)
        self.textArea = tk.Text(self.master, xscrollcommand=self.scrollbarX.set, yscrollcommand=self.scrollbarY.set, wrap=tk.NONE)
        self.scrollbarX.config(command=self.textArea.xview)
        self.scrollbarY.config(command=self.textArea.yview)
        self.scrollbarX.pack(side=tk.BOTTOM, fill=tk.X)
        self.scrollbarY.pack(side=tk.RIGHT, fill=tk.Y)
        self.textArea.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.textArea.bind("<Button-1>", lambda _: self.set_font_size(self.font_size + 1))
        self.textArea.bind("<Button-3>", lambda _: self.set_font_size(max(1, self.font_size - 1)))

        self.set_font_size(font_size)
        self.set_text(text)

    def set_text(self, text):
        self.textArea.config(state="normal")
        self.textArea.delete("1.0", tk.END)
        self.textArea.insert(tk.END, text)
        self.textArea.config(state="disabled")

    def set_font_size(self, new_size):
        self.font_size = new_size
        self.textArea.configure(font=("Courier", new_size))
        