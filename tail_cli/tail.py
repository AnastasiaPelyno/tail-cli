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

@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('-n', '--lines', default=10, type=int, help='Кількість рядків для показу.')
@click.option('-c', '--bytes', default=None, type=int, help='Кількість байтів для показу.')
@click.option('-f', '--follow', is_flag=True, help='Слідкувати за змінами файлу (як tail -f).')
@click.option('-q', '--quiet', '--silent', is_flag=True, help='Не показувати заголовки файлів.')
@click.option('-v', '--verbose', is_flag=True, help='Показувати більше інформації при виконанні.')
@click.option('-C', '--color', is_flag=True, help='Кольоровий вивід.')
@click.option('-r', '--reverse', is_flag=True, help='Виводити у зворотному порядку.')
@click.option('-s', '--skip-empty', is_flag=True, help='Пропускати порожні рядки.')
@click.option('-H', '--header', is_flag=True, help='Показувати назву файлу перед рядками.')
@click.version_option('1.0.2', prog_name='Tail CLI')
def tail(file, lines, bytes, follow, quiet, verbose, color, reverse, skip_empty, header):
    """Програма tail — виводить останні рядки або байти файлу."""
    try:
        if verbose:
            click.echo(f"Файл: {file}")
            click.echo(f"Опції: lines={lines}, bytes={bytes}, follow={follow}, reverse={reverse}")

        lines_data = read_last_lines(file, num_lines=lines, num_bytes=bytes)

        if skip_empty:
            lines_data = [l for l in lines_data if l.strip()]

        if reverse:
            lines_data = lines_data[::-1]

        if header and not quiet:
            click.echo(f"==> {file} <==")

        for line in lines_data:
            if isinstance(line, (bytes, bytearray)):
                text = line.decode(errors='ignore')
            else:
                text = str(line)
            if color:
                print(Fore.CYAN + text + Style.RESET_ALL)
            else:
                print(text)

        if follow:
            if verbose:
                click.echo("Режим слідкування (follow mode)...")
            with open(file, 'r') as f:
                f.seek(0, os.SEEK_END)
                while True:
                    line = f.readline()
                    if not line:
                        continue
                    if skip_empty and not line.strip():
                        continue
                    if color:
                        print(Fore.GREEN + line.strip() + Style.RESET_ALL)
                    else:
                        print(line.strip())

    except KeyboardInterrupt:
        click.echo("\nВихід з tail...")
        sys.exit(0)
    except Exception as e:
        click.echo(f"Помилка: {e}")

if __name__ == "__main__":
    tail()