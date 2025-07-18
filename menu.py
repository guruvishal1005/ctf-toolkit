from core import (
    binary_ascii_run,
    hex_ascii_run,
    caesar_run,
    base_decoder_run,
    xor_brute_run
)

def show_menu():
    tools = {
        "1": ("Binary to ASCII", binary_ascii_run),
        "2": ("Hex to ASCII", hex_ascii_run),
        "3": ("Caesar Cipher Decoder", caesar_run),
        "4": ("Base Decoder", base_decoder_run),
        "5": ("XOR Brute Force", xor_brute_run),
        "0": ("Exit", exit)
    }

    while True:
        print("\n=== CTF TOOLKIT MENU ===")
        for key, (name, _) in tools.items():
            print(f"{key}. {name}")

        choice = input("Select a tool:\n> ").strip()
        if choice in tools:
            print(f"\n[+] Running {tools[choice][0]}\n")
            tools[choice][1]()
        else:
            print("[!] Invalid choice. Try again.")
