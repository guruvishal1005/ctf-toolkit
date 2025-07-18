from datetime import datetime
from utils.color import Color

def info(message: str):
    print(f"[{Color.colorize('INFO', Color.OKBLUE)}] {timestamp()} - {message}")

def success(message: str):
    print(f"[{Color.colorize('SUCCESS', Color.OKGREEN)}] {timestamp()} - {message}")

def warn(message: str):
    print(f"[{Color.colorize('WARNING', Color.WARNING)}] {timestamp()} - {message}")

def error(message: str):
    print(f"[{Color.colorize('ERROR', Color.FAIL)}] {timestamp()} - {message}")

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
