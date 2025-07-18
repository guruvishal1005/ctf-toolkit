from utils.logger import info, warn
from utils.color import Color

def hex_to_ascii(hex_str: str) -> str:
    try:
        cleaned = hex_str.replace(" ", "").replace("\\x", "").replace("0x", "")
        bytes_obj = bytes.fromhex(cleaned)
        return bytes_obj.decode(errors="replace")
    except ValueError:
        return None

def run():
    hex_str = input("Enter hex string:\n> ")
    ascii_output = hex_to_ascii(hex_str)
    if ascii_output:
        info("ASCII Output:")
        print(Color.colorize(ascii_output, Color.CYAN))
    else:
        warn("Invalid hex input.")
