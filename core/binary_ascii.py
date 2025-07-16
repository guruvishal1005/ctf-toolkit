def binary_to_ascii(binary_str):
    try:
        # Split by space or split every 8 bits
        if ' ' in binary_str:
            binaries = binary_str.strip().split()
        else:
            binaries = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]

        ascii_text = ''.join([chr(int(b, 2)) for b in binaries])
        return ascii_text
    except ValueError:
        return "[!] Invalid binary input"

def run():
    binary_str = input("Enter binary:\n> ")
    result = binary_to_ascii(binary_str)
    print("ASCII Output:", result)
