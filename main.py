import tkinter as tk
from tkinter import filedialog, messagebox
import binascii
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

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

            key_bytes_test = binascii.unhexlify(key_hex)
            iv_bytes_test = binascii.unhexlify(iv_hex)
            if len(key_bytes_test) != 16:  # Should be caught by len(key_hex) != 32 but good to double check bytes
                messagebox.showerror("Error", "Key after hex conversion is not 16 bytes.")
                return
            if len(iv_bytes_test) != 8:  # Should be caught by len(iv_hex) != 16
                messagebox.showerror("Error", "IV after hex conversion is not 8 bytes.")
                return
        except binascii.Error as e:
            messagebox.showerror("Error", f"Invalid hex string for Key or IV: {e}")
            return
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error validating Key/IV: {e}")
            return

        try:
            with open(infile, 'rb') as f:
                data = f.read()

            result = self.triple_des_cbc(data, key_hex, iv_hex, encrypt=(action == "encrypt"))

            outfile = infile + ('.enc' if action == 'encrypt' else '.dec')
            # Ensure the decrypted file doesn't overwrite original if names collide by bad luck
            if action == 'decrypt' and infile.endswith('.enc') and outfile == infile:
                outfile = infile[:-4] + '.dec'  # e.g. file.enc.dec
                if outfile == infile:  # if original was file.enc.dec already
                    outfile = infile + ".decrypted"

            with open(outfile, 'wb') as f:
                f.write(result)
            messagebox.showinfo("Success", f"Output written to:\n{outfile}")
        except FileNotFoundError:
            messagebox.showerror("Error", f"Input file not found:\n{infile}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def triple_des_cbc(self, data: bytes, key_hex: str, iv_hex: str, encrypt: bool) -> bytes:
        key = binascii.unhexlify(key_hex)
        iv = binascii.unhexlify(iv_hex)
        key = DES3.adjust_key_parity(key)
        cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)
        if encrypt:
            return cipher.encrypt(pad(data, DES3.block_size))
        else:
            decrypted_data = cipher.decrypt(data)
            try:
                return unpad(decrypted_data, DES3.block_size)
            except ValueError as e:
                raise ValueError(f"Decryption failed. Incorrect key, IV, or data corruption? (Padding error: {e})")


if __name__ == '__main__':
    app = TripleDESApp()
    app.mainloop()