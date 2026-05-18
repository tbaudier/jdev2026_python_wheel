import numpy as np

from helpers import (
    break_rsa_with_primes,
    display_gui,
    rsa_decrypt,
    rsa_decrypt_text,
    rsa_encrypt,
    rsa_encrypt_text,
    show_text_gui,
)

# public key (n, e)
n = 1067333190347  # 1292063 * 826069
e = 17

# If message is an integer
# message = 123
# c = rsa_encrypt(message, n, e)
# encrypted message
# c = 641618116209
# plaintext = rsa_decrypt(c, d, n)
# print("Decrypted message:", plaintext)

# Get the message to encrypt and encrypt it
message = "Hello"
message = display_gui(message)
c = rsa_encrypt_text(message, n, e)
show_text_gui(str(c), title="Encrypted message", label="Encrypted message:")

# Load the list of primes and break RSA to find d
primes = np.load("primes.npz").tolist()
d = break_rsa_with_primes(n, e, primes)

# Decrypting the message
decrypted_message = rsa_decrypt_text(c, d, n)
show_text_gui(
    str(decrypted_message), title="Decrypted message", label="Decrypted message:"
)
