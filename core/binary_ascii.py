from utils.logger import info, warn
from utils.color import Color

def binary_to_ascii(binary_str):
    try:
        if ' ' in binary_str:
            binaries = binary_str.strip().split()
        else:
            binaries = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]

        ascii_text = ''.join([chr(int(b, 2)) for b in binaries])
        return ascii_text
    except ValueError:
        return None

def run():
    binary_str = input("Enter binary:\n> ")
    result = binary_to_ascii(binary_str)
    if result:
        info("ASCII Output:")
        print(Color.colorize(result, Color.CYAN))
    else:
        warn("Invalid binary input")
