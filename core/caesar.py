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
    text = input("Enter ciphertext: ")
    results = decrypt_caesar(text)
    for shift, result in results:
        print(f"[Shift {shift}]: {result}")
