import click
import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

def read_last_lines(file_path, num_lines=None, num_bytes=None):
    if num_bytes:
        with open(file_path, 'rb') as f:
            f.seek(0, os.SEEK_END)
            file_size = f.tell()
            read_size = min(file_size, num_bytes)
            f.seek(-read_size, os.SEEK_END)
            data = f.read(read_size)
        return data.splitlines()
    elif num_lines:
        with open(file_path, 'rb') as f:
            f.seek(0, os.SEEK_END)
            file_size = f.tell()
            block_size = 1024
            data = b''
            lines = []
            while len(lines) <= num_lines and file_size > 0:
                read_size = min(block_size, file_size)
                file_size -= read_size
                f.seek(file_size)
                data = f.read(read_size) + data
                lines = data.splitlines()
            return lines[-num_lines:]
    else:
        raise ValueError("Вкажіть num_lines або num_bytes")
