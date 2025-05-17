import tkinter as tk
from tkinter import filedialog

class TripleDESApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("3DES-2KEY CBC Encrypt/Decrypt")
        self.geometry("450x150") 
        self._build_widgets()

    def _build_widgets(self):
        tk.Label(self, text="Input File:").pack(anchor='w', padx=10, pady=(10, 0))
        frame = tk.Frame(self)
        frame.pack(fill='x', padx=10)
        self.file_entry = tk.Entry(frame)
        self.file_entry.pack(side='left', fill='x', expand=True)
        tk.Button(frame, text="Browse", command=self.browse_file).pack(side='left', padx=(5, 0))

    def browse_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, path)
            print(f"Selected file: {path}")

if __name__ == '__main__':
    app = TripleDESApp()
    app.mainloop()
