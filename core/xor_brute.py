def xor_brute(hex_str: str) -> str:
    try:
        data = bytes.fromhex(hex_str.replace(" ", "").replace("\\x", "").replace("0x", ""))
    except ValueError:
        return "[!] Invalid hex input."

    results = []
    for key in range(256):
        decrypted = bytes([b ^ key for b in data])
        try:
            text = decrypted.decode("utf-8")
        except UnicodeDecodeError:
            continue

        if is_printable(text):
            results.append(f"[KEY: {key:02X}] {text}")

    return "\n".join(results) if results else "[!] No readable output found."


def is_printable(s: str, threshold: float = 0.9) -> bool:
    import string
    printable = set(string.printable)
    return sum(c in printable for c in s) / len(s) >= threshold


def run():
    hex_input = input("Enter XORed hex string:\n> ")
    output = xor_brute(hex_input)
    print("Brute Force Results:\n", output)
