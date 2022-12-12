import click
from secrets import randbelow

def rand(min: int, max: int) -> int:
    diff = max - min
    return min + randbelow(diff + 1)

def psswd(length: int, exclude: str | None) -> str:
    word = ""
    while len(word) < length:
        char = chr(rand(33, 126))
        if exclude == None or char not in exclude:
            word = word + char
    return word

@click.command()
@click.option("--length", "-l", help="Number of characters to be included in password (default: 16).", default=16, required=False)
@click.option("--count", "-c", help="Number of passwords to generate (default: 1).", default=1, required=False)
@click.option("--exclude", "-e", help="String representing a list of characters not to include in the password.", required=False)
def generate(length: int, count: int, exclude: str | None) -> None:
    '''
    Generates one or multiple random password(s).
    '''
    for _ in range(count):
        print(psswd(length, exclude))
