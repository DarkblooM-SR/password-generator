# Password Generator
Simple random password generator written in Python

Made for Linux. Windows users, use [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install).

## Installation
```
git clone https://github.com/DarkblooM-SR/password-generator.git
cd password-generator
./install.sh
```

## Usage
```
$ genpsswd --help         
Usage: genpsswd [OPTIONS]

  Generates one or multiple random password(s).

Options:
  -l, --length INTEGER  Number of characters to be included in password
                        (default: 16).
  -c, --count INTEGER   Number of passwords to generate (default: 1).
  -e, --exclude TEXT    String representing a list of characters not to
                        include in the password.
  --help                Show this message and exit.
```
