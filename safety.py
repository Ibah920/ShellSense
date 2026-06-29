# safety.py
# Detects dangerous shell command patterns.
# This is LOCAL logic only - never relies on AI

DANGEROUS_PATTERNS = [
    ("rm -rf /", "This deletes everything on your system. Do NOT run this."),
    ("rm -rf ~", "This deletes your entire home folder. Do NOT run this."),
    ("rm -rf *", "This deletes everything in the current directory."),
    ("curl | bash", "This downloads and immediately runs unknown code. Very risky."),
    ("wget | bash", "This downloads and immediately runs unknown code. Very risky."),
    ("mkfs", "mkfs formats a disk — this will erase all data on it."),
    (":(){:|:&};:", "This is a fork bomb — it will crash your system."),
]

def check_safety(command):
    # Convert to lowercase so we catch "RM -RF /" the same as "rm -rf /"
    command_lower = command.lower()

    for pattern, warning in DANGEROUS_PATTERNS:
        if pattern.lower() in command_lower:
            return warning

    return None
