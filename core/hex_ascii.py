def hex_to_ascii(hex_str: str) -> str:
    try:
        # Remove hex prefixes/spaces
        cleaned = hex_str.replace(" ", "").replace("\\x", "").replace("0x", "")
        bytes_obj = bytes.fromhex(cleaned)
        return bytes_obj.decode(errors="replace")
    except ValueError:
        return "[!] Invalid hex input."

def run():
    hex_str = input("Enter hex string:\n> ")
    ascii_output = hex_to_ascii(hex_str)
    print("ASCII Output:", ascii_output)
