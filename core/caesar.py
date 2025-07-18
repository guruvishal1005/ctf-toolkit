from utils.logger import info
from utils.color import Color

def rotate_char(c, shift):
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base + shift) % 26 + base)
    else:
        return c

def decrypt_caesar(text: str) -> list:
    results = []
    for shift in range(1, 26):
        decrypted = ''.join([rotate_char(c, shift) for c in text])
        results.append((shift, decrypted))
    return results

def run():
    text = input("Enter ciphertext:\n> ")
    results = decrypt_caesar(text)
    info("Decryption Attempts:")
    for shift, result in results:
        print(Color.colorize(f"[Shift {shift:2}] {result}", Color.CYAN))
