import os

class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def print_header(title: str):
    """Print a formatted header."""
    clear_screen()
    print(Colors.BOLD + Colors.OKBLUE + "=" * 50 + Colors.ENDC)
    print(Colors.BOLD + f"{title.center(50)}" + Colors.ENDC)
    print(Colors.BOLD + Colors.OKBLUE + "=" * 50 + Colors.ENDC)

def ask_float(prompt: str):
    """Ask user for a float with validation."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Colors.WARNING + "Ogiltigt värde, försök igen." + Colors.ENDC)
