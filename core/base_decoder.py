import base64
from utils.logger import info, warn
from utils.color import Color

def try_decode(method, encoded_str):
    try:
        decoded_bytes = method(encoded_str.encode())
        return decoded_bytes.decode(errors='replace')
    except:
        return None

def auto_base_decode(encoded_str: str) -> dict:
    encoded_str = encoded_str.strip()
    results = {}

    result = try_decode(base64.b64decode, encoded_str)
    if result: results['base64'] = result

    result = try_decode(base64.b32decode, encoded_str.upper())
    if result: results['base32'] = result

    result = try_decode(base64.b16decode, encoded_str.upper())
    if result: results['base16'] = result

    result = try_decode(base64.b85decode, encoded_str)
    if result: results['base85'] = result

    return results

def run():
    encoded_str = input("Enter the encoded string:\n> ")
    decoded = auto_base_decode(encoded_str)

    if not decoded:
        warn("Unable to decode with base16, base32, base64, or base85.")
    else:
        info("Decoding Results:")
        for base, value in decoded.items():
            print(Color.colorize(f"[{base.upper()}] {value}", Color.CYAN))
