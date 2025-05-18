import tkinter as tk
from tkinter import filedialog, messagebox
import binascii
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

class TripleDESApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("3DES-2KEY CBC Encrypt/Decrypt")
        self.geometry("450x350")
        self._build_widgets()

    def _build_widgets(self):
        tk.Label(self, text="Input File:").pack(anchor='w', padx=10, pady=(10, 0))
        file_frame = tk.Frame(self)
        file_frame.pack(fill='x', padx=10)
        self.file_entry = tk.Entry(file_frame)
        self.file_entry.pack(side='left', fill='x', expand=True)
        tk.Button(file_frame, text="Browse", command=self.browse_file).pack(side='left', padx=(5, 0))


        tk.Label(self, text="Key (32 hex chars):").pack(anchor='w', padx=10, pady=(10, 0))
        key_frame = tk.Frame(self)
        key_frame.pack(fill='x', padx=10)
        self.key_entry = tk.Entry(key_frame)
        self.key_entry.pack(side='left', fill='x', expand=True)
        tk.Button(key_frame, text="Generate Key", command=self.generate_key).pack(side='left', padx=(5, 0))

        tk.Label(self, text="IV (16 hex chars):").pack(anchor='w', padx=10, pady=(10, 0))
        iv_frame = tk.Frame(self)
        iv_frame.pack(fill='x', padx=10)
        self.iv_entry = tk.Entry(iv_frame)
        self.iv_entry.pack(side='left', fill='x', expand=True)
        tk.Button(iv_frame, text="Generate IV", command=self.generate_iv).pack(side='left', padx=(5, 0))


        self.action = tk.StringVar(value="encrypt")
        tk.Radiobutton(self, text="Encrypt", variable=self.action, value="encrypt").pack(anchor='w', padx=10, pady=(10, 0))
        tk.Radiobutton(self, text="Decrypt", variable=self.action, value="decrypt").pack(anchor='w', padx=10)


        tk.Button(self, text="Run", command=self.run_action).pack(pady=20)

    def browse_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, path)

    def generate_key(self):
        raw = get_random_bytes(16)
        key_bytes_with_parity = DES3.adjust_key_parity(raw)
        key_hex = binascii.hexlify(key_bytes_with_parity).upper().decode()
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, key_hex)

    def generate_iv(self):
        raw = get_random_bytes(8)
        iv_hex = binascii.hexlify(raw).upper().decode()
        self.iv_entry.delete(0, tk.END)
        self.iv_entry.insert(0, iv_hex)

    def run_action(self):
        infile = self.file_entry.get()
        key_hex = self.key_entry.get().strip()
        iv_hex = self.iv_entry.get().strip()
        action = self.action.get()

        if not infile or not key_hex or not iv_hex:
            messagebox.showerror("Error", "All fields are required.")
            return
        if len(key_hex) != 32:
            messagebox.showerror("Error", "Key must be 32 hex chars (16 bytes).")
            return
        if len(iv_hex) != 16:
            messagebox.showerror("Error", "IV must be 16 hex chars (8 bytes).")
            return

        try:
            binascii.unhexlify(key_hex)
            binascii.unhexlify(iv_hex)
        except binascii.Error as e:
            messagebox.showerror("Error", f"Invalid hex string for Key or IV: {e}")
            return
        except Exception as e:
            messagebox.showerror("Error", f"Error processing Key/IV: {e}")
            return

        messagebox.showinfo("Action", f"Action: {action}\nFile: {infile}\nKey: {key_hex[:8]}...\nIV: {iv_hex[:8]}...\n\n(Crypto operation not yet implemented)")



    def triple_des_cbc(self, data: bytes, key_hex: str, iv_hex: str, encrypt: bool) -> bytes:
        print(f"Placeholder: triple_des_cbc called. Encrypt: {encrypt}")
        print(f"Data length: {len(data)}, Key: {key_hex}, IV: {iv_hex}")
        if encrypt:
            return b"encrypted_placeholder_data"
        else:
            return b"decrypted_placeholder_data"

if __name__ == '__main__':
    app = TripleDESApp()
    app.mainloop()