import tkinter as tk
from tkinter import filedialog
import binascii
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

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

        tk.Label(self, text="Key (32 hex chars):").pack(anchor='w', padx=10, pady=(10,0))
        key_frame = tk.Frame(self)
        key_frame.pack(fill='x', padx=10)
        self.key_entery = tk.Entry(key_frame)
        self.key_entery.pack(side='left', fill='x', expand=True)
        tk.Button(key_frame, text="Generate Key", command=self.generate_key).pack(side='left', padx=(5,0))

        tk.Label(self, text="IV (16 hex chars):").pack(anchor='w', padx=10, pady=(10,0))
        iv_frame = tk.Frame(self)
        iv_frame.pack(fill='x', padx=10)
        self.iv_entery = tk.Entry(iv_frame)
        self.iv_entery.pack(side='left', fill='x', expand=True)
        tk.Button(iv_frame, text="Generate IV", command=self.generate_iv).pack(side='left', padx=(5,0))

    def browse_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, path)
            print(f"Selected file: {path}")
    def generate_key(self):
        raw = get_random_bytes(16)
        key_bytes_with_parity = DES3.adjust_key_parity(raw)
        key_hex = binascii.hexlify(key_bytes_with_parity).upper().decode()
        self.key_entery.delete(0, tk.END)
        self.key_entery.insert(0, key_hex)

    def generate_iv(self):
        raw = get_random_bytes(8)
        iv_hex = binascii.hexlify(raw).upper().decode()
        self.iv_entery.delete(0, tk.END)
        self.iv_entery.insert(0, iv_hex)

if __name__ == '__main__':
    app = TripleDESApp()
    app.mainloop()
