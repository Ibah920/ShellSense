# render.py
# Handles all color and formatted terminal output

# ANSI color codes - special strings the terminal reads as color instructions
RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"   # turns off all formatting

def print_danger(message):
    print(f"{RED}{BOLD}DANGER: {message}{RESET}")

def print_command(name, description):
    print(f"\n{BOLD}{CYAN}COMMAND:{RESET} {name}")
    print(f"  {description}")

def print_flag(flag, explanation):
    print(f"  {GREEN}{flag}{RESET}: {explanation}")

def print_unknown_flag(flag):
    print(f"  {YELLOW}{flag}{RESET}: (not recognized in local dictionary)")

def print_unknown_command(name):
    print(f"{YELLOW}Sorry, I don't recognize '{name}' yet — and no API key is set.{RESET}")

def print_ai_response(command, text):
    print(f"\n{BOLD}{CYAN}COMMAND:{RESET} {command}")
    print(f"  {YELLOW}(AI-generated explanation){RESET}")
    print(f"\n{text}")
