import tkinter as tk
from tkinter import messagebox


def factor_with_primes(n, primes):
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return p, n // p
    return None


def break_rsa_with_primes(n, e, primes):
    factors = factor_with_primes(n, primes)
    if not factors:
        raise ValueError("No small prime factor found")

    p, q = factors
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return d


def read_primes_from_file(filename):
    primes = []

    with open(filename, "r") as f:
        for line in f:
            # Split by whitespace
            for token in line.split():
                # Keep only numbers
                if token.isdigit():
                    primes.append(int(token))

    return primes


def rsa_encrypt(m, n, e):
    if m >= n:
        raise ValueError("Message " + str(m) + " is too large for modulus " + str(n))
    return pow(m, e, n)


def rsa_encrypt_text(message, n, e):
    # Convert text to integer
    m = int.from_bytes(message.encode("utf-8"), byteorder="big")
    return rsa_encrypt(m, n, e)


def rsa_decrypt(c, d, n):
    return pow(c, d, n)


def rsa_decrypt_text(c, d, n):
    m = rsa_decrypt(c, d, n)

    # Convert integer back to bytes
    length = (m.bit_length() + 7) // 8
    return m.to_bytes(length, byteorder="big").decode("utf-8")


def display_gui(default_text="Hello"):
    result = {"value": None}  # mutable container

    def submit():
        result["value"] = entry.get()
        root.destroy()

    root = tk.Tk()
    root.title("RSA Message Encryption")
    root.geometry("350x150")
    root.resizable(False, False)

    lbl = tk.Label(root, text="Message to encrypt")
    lbl.pack(pady=10)

    entry = tk.Entry(root, width=40)
    entry.pack(pady=5)
    entry.insert(0, default_text)
    entry.focus()

    btn = tk.Button(root, text="OK", command=submit)
    btn.pack(pady=10)

    root.mainloop()
    return result["value"]


def show_text_gui(message, title="Result", label="Encrypted message:"):
    root = tk.Tk()
    root.title(title)
    root.geometry("400x200")
    root.resizable(False, False)

    lbl = tk.Label(root, text=label)
    lbl.pack(pady=10)

    text_box = tk.Text(root, height=4, width=45, wrap="word")
    text_box.pack(pady=5)
    text_box.insert("1.0", str(message))
    text_box.config(state="disabled")  # read‑only

    btn = tk.Button(root, text="OK", command=root.destroy)
    btn.pack(pady=10)

    root.mainloop()
