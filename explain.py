
import sys
from commands import COMMANDS
from safety import check_safety
import render
import ai_fallback

def main():
    # Safety check FIRST — before trying to read sys.argv[1]
    if len(sys.argv) < 2:
        print("Usage: python explain.py <command> [flags...]")
        return

    # Join all arguments into one string so safety can check the full command
    full_command = " ".join(sys.argv[1:])

    # Check for dangerous patterns before doing anything else
    warning = check_safety(full_command)
    if warning:
        render.print_danger(warning)
        return

    command_name = sys.argv[1]

    # Check if the command exists in the COMMANDS dictionary
    if command_name not in COMMANDS:
        result = ai_fallback.ask_claude(full_command)
        if result:
            render.print_ai_response(command_name, result)
        else:
            render.print_unknown_command(command_name)
        return

    command_info = COMMANDS[command_name]

    # Print the command description
    render.print_command(command_name, command_info["description"])

    # Collect any flags the user typed (everything after the command name)
    user_flags = sys.argv[2:]

    # Only print the FLAGS section if the user actually typed some flags
    if user_flags:
        print("\nFLAGS:")
        for flag in user_flags:
            if flag in command_info["flags"]:
                render.print_flag(flag, command_info["flags"][flag])
            else:
                render.print_unknown_flag(flag)

# This line actually RUNS the function
main()
