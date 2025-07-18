from utils.logger import info, warn
from utils.color import Color
import string

def is_printable(s: str, threshold: float = 0.9) -> bool:
    printable = set(string.printable)
    return sum(c in printable for c in s) / len(s) >= threshold

def xor_brute(hex_str: str) -> list:
    try:
        data = bytes.fromhex(hex_str.replace(" ", "").replace("\\x", "").replace("0x", ""))
    except ValueError:
        return None

    results = []
    for key in range(256):
        decrypted = bytes([b ^ key for b in data])
        try:
            text = decrypted.decode("utf-8")
        except UnicodeDecodeError:
            continue
        if is_printable(text):
            results.append(f"[KEY: {key:02X}] {text}")
    return results

def run():
    hex_input = input("Enter XORed hex string:\n> ")
    output = xor_brute(hex_input)
    if output:
        info("Brute Force Results:")
        for line in output:
            print(Color.colorize(line, Color.CYAN))
    else:
        warn("No readable output found or invalid hex.")
