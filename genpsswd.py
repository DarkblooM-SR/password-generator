import click
from secrets import randbelow

def rand(min: int, max: int) -> int:
    while True:
        n = randbelow(max + 1)
        if n >= min:
            return n

@click.command()
@click.option("--length", "-l", help="Number of characters to be included in password (default: 16)", default=16, required=False)
@click.option("--count", "-c", help="Number of passwords to generate (default: 1)", default=1, required=False)
def generate(length: int, count: int) -> None:
    '''
    Generates one or multiple random password(s)
    '''
    for _ in range(count):
        word = ""
        for _ in range(length):
            word = word + chr(rand(33, 126))
        print(word)
