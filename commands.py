# commands.py
# A local dictionary of common shell commands and their flags.
# The explain tool checks here first before calling the AI.

COMMANDS = {
    "ls": {
        "description": "List the contents of a directory.",
        "flags": {
            "-l": "Long format — shows permissions, owner, size, and date for each file.",
            "-a": "Show all files, including hidden ones (names starting with a dot).",
            "-h": "Human-readable file sizes (e.g. 4K instead of 4096 bytes).",
            "-r": "Reverse the sort order.",
            "-t": "Sort by time modified, newest first.",
        }
    },
    "cd": {
        "description": "Change the current working directory.",
        "flags": {
            "cd ..": "Move up one directory level.",
            "cd -": "Switch to the previous directory.",
            "cd ~": "Change to the home directory.",
        }
    },
    "cp": {
        "description": "Copy files or directories from one location to another.",
        "flags": {
            "-r": "Copy directories recursively — copies the folder and everything inside it.",
            "-i": "Interactive — ask before overwriting an existing file.",
            "-v": "Verbose — print each file name as it is copied.",
        }
    },
    "mv": {
        "description": "Move or rename files and directories.",
        "flags": {
            "-i": "Interactive — ask before overwriting an existing file.",
            "-v": "Verbose — print each file name as it is moved.",
            "-n": "No-clobber — never overwrite an existing file.",
        }
    },
    "rm": {
        "description": "Remove (delete) files or directories.",
        "flags": {
            "-r": "Recursive — delete a directory and everything inside it.",
            "-f": "Force — delete without asking, even if files are write-protected.",
            "-i": "Interactive — ask before deleting each file.",
            "-v": "Verbose — print each file name as it is deleted.",
        }
    },
    "grep": {
        "description": "Search for a pattern (text or regex) inside files.",
        "flags": {
            "-r": "Recursive — search through all files in a directory and subdirectories.",
            "-i": "Case-insensitive — match regardless of upper or lower case.",
            "-n": "Show line numbers next to each matching line.",
            "-v": "Invert — show lines that do NOT match the pattern.",
            "-l": "List only the names of files that contain a match.",
        }
    },
    "tar": {
        "description": "Archive (bundle) or extract files from a .tar file.",
        "flags": {
            "-x": "Extract — unpack files from an archive.",
            "-c": "Create — make a new archive.",
            "-z": "Use gzip compression (for .tar.gz files).",
            "-v": "Verbose — list each file as it is archived or extracted.",
            "-f": "File — specifies the name of the archive file (always followed by the filename).",
        }
    },
    "find": {
        "description": "Search for files and directories matching given criteria.",
        "flags": {
            "-name": "Search by file name (e.g. -name '*.txt' finds all .txt files).",
            "-type": "Filter by type: 'f' for files, 'd' for directories.",
            "-mtime": "Filter by modification time in days (e.g. -mtime -7 means last 7 days).",
            "-size": "Filter by file size (e.g. -size +1M means larger than 1 megabyte).",
        }
    },
    "chmod": {
        "description": "Change the permissions (who can read, write, or execute) of a file.",
        "flags": {
            "-R": "Recursive — apply the permission change to a directory and all its contents.",
            "+x": "Add execute permission — make a file runnable as a program.",
            "777": "Give read, write, and execute permission to everyone (use with caution).",
            "644": "Owner can read and write; everyone else can only read (common for files).",
            "755": "Owner can do everything; everyone else can read and execute (common for directories).",
        }
    },
    "git": {
        "description": "Version control — track changes to code over time.",
        "flags": {
            "status": "Show which files have been changed or staged.",
            "add": "Stage files to be included in the next commit.",
            "commit": "Save a snapshot of staged changes with a message.",
            "push": "Upload local commits to a remote repository.",
            "pull": "Download and merge changes from a remote repository.",
            "clone": "Copy a remote repository to your local machine.",
            "log": "Show the history of commits.",
            "diff": "Show the exact lines that changed since the last commit.",
        }
    },
    "mkdir": {
        "description": "Create a new directory (folder).",
        "flags": {
            "-p": "Create parent directories as needed — no error if the directory already exists.",
            "-v": "Verbose — print a message for each directory that is created.",
            "-m": "Set permissions at creation time (e.g. -m 755).",
        }
    },
    "touch": {
        "description": "Create an empty file, or update the timestamp of an existing file.",
        "flags": {
            "-a": "Change only the access time of the file.",
            "-m": "Change only the modification time of the file.",
            "-t": "Set a specific timestamp instead of the current time (format: YYYYMMDDHHMM).",
            "-c": "Do not create the file if it does not already exist.",
        }
    },
    "cat": {
        "description": "Display the contents of a file in the terminal.",
        "flags": {
            "-n": "Number all output lines.",
            "-b": "Number only non-blank lines.",
            "-A": "Show hidden characters like tabs and line endings (useful for debugging).",
            "-s": "Squeeze multiple blank lines into one.",
            "-v": "Show non-printing characters visibly.",
        }
    },
    "pwd": {
        "description": "Print the full path of the current working directory — shows where you are.",
        "flags": {
            "-L": "Print the logical path, following symlinks as-is (default behavior).",
            "-P": "Print the physical path, resolving all symlinks to their real location.",
        }
    },
    "echo": {
        "description": "Print text or the value of a variable to the terminal.",
        "flags": {
            "-n": "Do not print a newline at the end of the output.",
            "-e": "Enable interpretation of special characters like \\n (newline) and \\t (tab).",
            "-E": "Disable interpretation of special characters (default behavior).",
        }
    },
    "man": {
        "description": "Display the manual (help page) for a command.",
        "flags": {
            "-k": "Search all manual pages for a keyword.",
            "-f": "Show a short description of a command (same as the whatis command).",
            "-a": "Show all manual pages for a command, not just the first one.",
            "-P": "Use a specific pager program to display the output.",
        }
    },
    "sudo": {
        "description": "Run a command with superuser (administrator) privileges.",
        "flags": {
            "-u": "Run the command as a different user instead of root.",
            "-i": "Start an interactive login shell as root.",
            "-s": "Start a shell as root without a full login.",
            "-l": "List the commands the current user is allowed to run with sudo.",
            "-k": "Invalidate the cached password — next sudo will prompt for password again.",
        }
    },
    "curl": {
        "description": "Transfer data to or from a URL — commonly used to download files or call APIs.",
        "flags": {
            "-o": "Save output to a specific file name (e.g. -o file.html).",
            "-O": "Save output using the filename from the URL.",
            "-L": "Follow redirects if the URL points somewhere else.",
            "-s": "Silent mode — hide progress and error messages.",
            "-I": "Fetch only the HTTP headers, not the full response body.",
            "-X": "Specify the HTTP method (e.g. -X POST, -X DELETE).",
            "-H": "Add a custom HTTP header (e.g. -H 'Authorization: Bearer token').",
            "-d": "Send data in the request body (used with POST requests).",
            "--user": "Pass a username and password for authentication (e.g. --user name:pass).",
        }
    },
    "pip": {
        "description": "Install and manage Python packages from the Python Package Index (PyPI).",
        "flags": {
            "install": "Install a package (e.g. pip install requests).",
            "uninstall": "Remove an installed package.",
            "list": "Show all installed packages and their versions.",
            "show": "Display details about a specific installed package.",
            "freeze": "Output installed packages in a format suitable for requirements.txt.",
            "install -r": "Install all packages listed in a requirements.txt file.",
            "install --upgrade": "Upgrade a package to its latest version.",
            "search": "Search PyPI for a package by name or keyword.",
        }
    },
    "ping": {
        "description": "Send test packets to a host to check if it's reachable and measure response time.",
        "flags": {
            "-c": "Count — stop after sending this many packets (e.g. -c 4).",
            "-i": "Interval — wait this many seconds between packets (default is 1).",
            "-t": "Timeout — stop waiting for a response after this many seconds.",
            "-s": "Set the size of the packet in bytes.",
        }
    },
    "ssh": {
        "description": "Securely connect to a remote machine over the network.",
        "flags": {
            "-i": "Identity file — use a specific private key for authentication (e.g. -i ~/.ssh/id_rsa).",
            "-p": "Port — connect on a specific port instead of the default (22).",
            "-L": "Local port forwarding — tunnel a remote port to your local machine.",
            "-v": "Verbose — show detailed connection info, useful for debugging.",
            "-N": "Do not execute a remote command — useful for port forwarding only.",
        }
    },
    "scp": {
        "description": "Securely copy files between your local machine and a remote server.",
        "flags": {
            "-r": "Recursive — copy an entire directory.",
            "-P": "Port — connect on a specific port (capital P, unlike ssh which uses lowercase).",
            "-i": "Identity file — use a specific private key.",
            "-v": "Verbose — show progress and connection details.",
        }
    },
    "wget": {
        "description": "Download files from the internet via a URL.",
        "flags": {
            "-O": "Output — save the file with a specific name (e.g. -O file.zip).",
            "-q": "Quiet — suppress output, download silently.",
            "-r": "Recursive — download an entire website or directory.",
            "-c": "Continue — resume a partially downloaded file.",
            "--no-check-certificate": "Skip SSL certificate verification (use with caution).",
        }
    },
    "ps": {
        "description": "Show a snapshot of currently running processes.",
        "flags": {
            "aux": "Show all processes for all users in a detailed format (commonly used as ps aux).",
            "-e": "Show every process running on the system.",
            "-f": "Full format — show more columns including parent process ID.",
            "-u": "Show processes for a specific user (e.g. -u ibrahim).",
        }
    },
    "kill": {
        "description": "Send a signal to a process — most commonly used to stop it.",
        "flags": {
            "-9": "Force kill — immediately terminate the process with no cleanup (SIGKILL).",
            "-15": "Graceful stop — ask the process to shut down cleanly (SIGTERM, the default).",
            "-l": "List all available signal names.",
        }
    },
    "killall": {
        "description": "Kill all processes with a given name instead of using a process ID.",
        "flags": {
            "-9": "Force kill all matching processes immediately.",
            "-i": "Interactive — ask for confirmation before killing each process.",
            "-v": "Verbose — print a message for each process that is killed.",
        }
    },
    "top": {
        "description": "Show a live, updating view of running processes and system resource usage.",
        "flags": {
            "-u": "Filter by user — show only processes owned by a specific user.",
            "-n": "Number — exit after this many refreshes (e.g. -n 5).",
            "-d": "Delay — set the refresh interval in seconds.",
        }
    },
    "which": {
        "description": "Show the full path of a command — tells you where a program is installed.",
        "flags": {
            "-a": "Show all matching locations, not just the first one found.",
        }
    },
    "wc": {
        "description": "Count lines, words, and characters in a file or input.",
        "flags": {
            "-l": "Count lines only.",
            "-w": "Count words only.",
            "-c": "Count bytes (characters) only.",
            "-m": "Count characters (handles multi-byte characters correctly).",
        }
    },
    "head": {
        "description": "Show the first lines of a file (default: first 10 lines).",
        "flags": {
            "-n": "Number — show this many lines instead of the default 10 (e.g. -n 20).",
            "-c": "Show this many bytes instead of lines.",
        }
    },
    "tail": {
        "description": "Show the last lines of a file (default: last 10 lines).",
        "flags": {
            "-n": "Number — show this many lines from the end (e.g. -n 20).",
            "-f": "Follow — keep watching the file and print new lines as they are added (great for logs).",
            "-c": "Show this many bytes from the end instead of lines.",
        }
    },
    "sort": {
        "description": "Sort lines of text alphabetically or numerically.",
        "flags": {
            "-r": "Reverse — sort in descending order.",
            "-n": "Numeric — sort by number value instead of alphabetically.",
            "-u": "Unique — remove duplicate lines from the output.",
            "-k": "Key — sort by a specific column (e.g. -k 2 sorts by the second word).",
            "-f": "Fold case — treat uppercase and lowercase as equal.",
        }
    },
    "uniq": {
        "description": "Remove or report duplicate lines (works best after sorting).",
        "flags": {
            "-c": "Count — prefix each line with the number of times it appears.",
            "-d": "Duplicates only — only print lines that appear more than once.",
            "-u": "Unique only — only print lines that appear exactly once.",
            "-i": "Case-insensitive — treat uppercase and lowercase as the same.",
        }
    },
    "cut": {
        "description": "Extract specific columns or characters from each line of a file.",
        "flags": {
            "-d": "Delimiter — specify the character that separates columns (e.g. -d ',').",
            "-f": "Fields — which columns to extract (e.g. -f 1,3 gets the first and third columns).",
            "-c": "Characters — extract specific character positions (e.g. -c 1-5).",
        }
    },
    "sed": {
        "description": "Stream editor — find and replace text, or transform lines in a file.",
        "flags": {
            "-i": "In-place — edit the file directly instead of printing to the terminal.",
            "-n": "Silent — suppress automatic printing (use with /p to print only matches).",
            "-e": "Expression — lets you chain multiple sed commands together.",
            "s/old/new/": "Substitute — replace first occurrence of 'old' with 'new' on each line.",
            "s/old/new/g": "Global substitute — replace all occurrences on each line.",
        }
    },
    "awk": {
        "description": "A powerful text processing tool — great for working with columns and structured data.",
        "flags": {
            "-F": "Field separator — set the character that separates columns (e.g. -F ':').",
            "-v": "Variable — pass a value into the awk program (e.g. -v name=Ibrahim).",
            "'{print $1}'": "Print the first column of each line ($2 for second, $NF for last).",
            "'{print NR, $0}'": "Print line numbers alongside each line.",
        }
    },
    "diff": {
        "description": "Compare two files line by line and show what is different.",
        "flags": {
            "-u": "Unified format — shows a few lines of context around each change (most readable).",
            "-i": "Ignore case — treat uppercase and lowercase as the same.",
            "-r": "Recursive — compare two directories and all their contents.",
            "-q": "Quiet — only report whether files differ, not what changed.",
        }
    },
    "less": {
        "description": "View a file one page at a time — use arrow keys to scroll, Q to quit.",
        "flags": {
            "-N": "Show line numbers.",
            "-S": "Chop long lines instead of wrapping them.",
            "-i": "Case-insensitive search when using the / search feature.",
            "+F": "Follow mode — like tail -f, keep reading as the file grows.",
        }
    },
    "du": {
        "description": "Show disk usage — how much space files and directories are taking up.",
        "flags": {
            "-h": "Human-readable — show sizes in KB, MB, GB instead of bytes.",
            "-s": "Summary — show only the total for each argument, not every subfolder.",
            "-a": "All — show sizes for individual files, not just directories.",
            "--max-depth": "Limit how many folder levels deep to show (e.g. --max-depth=1).",
        }
    },
    "df": {
        "description": "Show available and used disk space on all mounted drives.",
        "flags": {
            "-h": "Human-readable — show sizes in KB, MB, GB.",
            "-T": "Show the filesystem type (e.g. ext4, APFS).",
            "-i": "Show inode usage instead of disk space.",
        }
    },
    "ln": {
        "description": "Create a link to a file — either a hard link or a symbolic (shortcut) link.",
        "flags": {
            "-s": "Symbolic — create a symlink (a shortcut that points to the original file).",
            "-f": "Force — overwrite an existing link with the same name.",
            "-v": "Verbose — print a message for each link created.",
        }
    },
    "stat": {
        "description": "Show detailed information about a file — size, permissions, timestamps, and more.",
        "flags": {
            "-f": "On macOS, use a specific output format.",
            "-c": "On Linux, use a specific output format string.",
        }
    },
    "file": {
        "description": "Identify the type of a file based on its contents, not just its extension.",
        "flags": {
            "-b": "Brief — don't print the filename, just the type.",
            "-i": "MIME type — show the file type in MIME format (e.g. text/plain).",
            "-z": "Try to look inside compressed files.",
        }
    },
    "xargs": {
        "description": "Take input from a pipe and pass it as arguments to another command.",
        "flags": {
            "-n": "Max args — pass at most this many arguments per command run.",
            "-I": "Replace string — use a placeholder for where the input goes (e.g. -I {} cp {} /backup/).",
            "-p": "Prompt — ask for confirmation before running each command.",
            "-0": "Null delimiter — use with find -print0 to handle filenames with spaces.",
        }
    },
    "tee": {
        "description": "Read from input and write to both a file and the terminal at the same time.",
        "flags": {
            "-a": "Append — add to the file instead of overwriting it.",
        }
    },
    "env": {
        "description": "Show all environment variables, or run a command with a modified environment.",
        "flags": {
            "-i": "Ignore — start with an empty environment instead of the current one.",
            "-u": "Unset — remove a specific variable from the environment.",
        }
    },
    "export": {
        "description": "Set an environment variable so it's available to child processes and commands you run.",
        "flags": {
            "-n": "Remove the export attribute from a variable (it still exists, just not exported).",
            "-p": "Print all exported variables.",
        }
    },
    "history": {
        "description": "Show a list of previously run commands in this terminal session.",
        "flags": {
            "-c": "Clear — delete all history.",
            "-d": "Delete a specific entry by line number (e.g. history -d 42).",
            "-w": "Write — save current history to the history file immediately.",
        }
    },
    "alias": {
        "description": "Create a shortcut name for a longer command.",
        "flags": {
            "-p": "Print all currently defined aliases.",
        }
    },
    "source": {
        "description": "Run a script file in the current shell — changes made inside it affect your current session.",
        "flags": {
            "-n": "Read the file but don't execute it — useful for syntax checking.",
        }
    },
    "uname": {
        "description": "Show information about the operating system and hardware.",
        "flags": {
            "-a": "All — print all available system information.",
            "-s": "Kernel name (e.g. Darwin, Linux).",
            "-r": "Kernel release version.",
            "-m": "Machine hardware type (e.g. arm64, x86_64).",
        }
    },
    "whoami": {
        "description": "Print the username of the currently logged-in user.",
        "flags": {}
    },
    "id": {
        "description": "Show the user ID, group ID, and group memberships of the current user.",
        "flags": {
            "-u": "Print only the user ID.",
            "-g": "Print only the primary group ID.",
            "-n": "Print names instead of numbers.",
        }
    },
    "date": {
        "description": "Display or set the current date and time.",
        "flags": {
            "+%Y-%m-%d": "Format the date as YYYY-MM-DD.",
            "+%H:%M:%S": "Format the time as HH:MM:SS.",
            "-u": "Show the time in UTC instead of local time.",
            "-r": "Show the last modification time of a file instead of the current time.",
        }
    },
    "uptime": {
        "description": "Show how long the system has been running, and the current load averages.",
        "flags": {
            "-p": "Pretty — show uptime in a human-readable format.",
            "-s": "Since — show the date and time the system was last booted.",
        }
    },
    "chown": {
        "description": "Change the owner (and optionally the group) of a file or directory.",
        "flags": {
            "-R": "Recursive — apply the ownership change to a directory and all its contents.",
            "-v": "Verbose — print a message for each file changed.",
            "user:group": "Set both owner and group at once (e.g. chown ibrahim:staff file.txt).",
        }
    },
    "rsync": {
        "description": "Efficiently copy or sync files between locations — only transfers what changed.",
        "flags": {
            "-a": "Archive mode — preserves permissions, timestamps, symlinks, and copies recursively.",
            "-v": "Verbose — show files as they are transferred.",
            "-z": "Compress data during transfer.",
            "--delete": "Delete files at the destination that no longer exist at the source.",
            "--dry-run": "Simulate the transfer without actually copying anything.",
            "-P": "Show progress and keep partial files if the transfer is interrupted.",
        }
    },
    "zip": {
        "description": "Compress files into a .zip archive.",
        "flags": {
            "-r": "Recursive — include a directory and all its contents.",
            "-e": "Encrypt — password-protect the zip file.",
            "-9": "Maximum compression (slower but smallest file size).",
            "-d": "Delete a file from an existing zip archive.",
        }
    },
    "unzip": {
        "description": "Extract files from a .zip archive.",
        "flags": {
            "-d": "Destination — extract to a specific directory (e.g. -d /tmp/output).",
            "-l": "List — show the contents of the zip without extracting.",
            "-o": "Overwrite existing files without prompting.",
            "-q": "Quiet — suppress output.",
        }
    },
    "gzip": {
        "description": "Compress a file into .gz format (replaces the original by default).",
        "flags": {
            "-d": "Decompress — unzip a .gz file (same as gunzip).",
            "-k": "Keep — don't delete the original file after compressing.",
            "-r": "Recursive — compress all files in a directory.",
            "-9": "Maximum compression.",
            "-l": "List compression info for a .gz file.",
        }
    },
    "lsof": {
        "description": "List open files — shows which files and network connections are in use by which processes.",
        "flags": {
            "-i": "Internet — show network connections (e.g. -i :8080 shows what's using port 8080).",
            "-u": "User — show files opened by a specific user.",
            "-p": "Process — show files opened by a specific process ID.",
            "+D": "Directory — show all open files inside a directory.",
        }
    },
    "crontab": {
        "description": "Schedule commands to run automatically at set times.",
        "flags": {
            "-e": "Edit — open your crontab schedule in a text editor.",
            "-l": "List — show your current scheduled jobs.",
            "-r": "Remove — delete your entire crontab.",
            "-u": "User — manage the crontab for a specific user (requires sudo).",
        }
    },
    "docker": {
        "description": "Build, run, and manage containers — isolated environments for applications.",
        "flags": {
            "ps": "List running containers.",
            "ps -a": "List all containers, including stopped ones.",
            "run": "Create and start a new container from an image.",
            "build": "Build an image from a Dockerfile.",
            "pull": "Download an image from Docker Hub.",
            "stop": "Gracefully stop a running container.",
            "rm": "Remove a stopped container.",
            "rmi": "Remove an image.",
            "logs": "Show the output logs of a container.",
            "exec -it": "Run a command inside a running container interactively.",
        }
    },
    "npm": {
        "description": "Node Package Manager — install and manage JavaScript packages.",
        "flags": {
            "install": "Install all packages listed in package.json.",
            "install <pkg>": "Install a specific package (e.g. npm install express).",
            "install -g": "Install a package globally so it's available as a command.",
            "uninstall": "Remove a package.",
            "run": "Run a script defined in package.json (e.g. npm run start).",
            "init": "Create a new package.json file interactively.",
            "list": "Show installed packages.",
            "update": "Update packages to their latest allowed versions.",
            "audit": "Check for known security vulnerabilities in installed packages.",
        }
    },
    "node": {
        "description": "Run JavaScript files or start an interactive JavaScript console.",
        "flags": {
            "-e": "Evaluate — run a string of JavaScript directly (e.g. node -e 'console.log(1+1)').",
            "-v": "Print the installed Node.js version.",
            "--inspect": "Start in debug mode so you can connect a debugger.",
        }
    },
    "brew": {
        "description": "Homebrew — the package manager for macOS. Install and manage software.",
        "flags": {
            "install": "Install a package (e.g. brew install git).",
            "uninstall": "Remove an installed package.",
            "update": "Update Homebrew itself.",
            "upgrade": "Upgrade all installed packages to their latest versions.",
            "list": "Show all installed packages.",
            "search": "Search for a package by name.",
            "info": "Show details about a package.",
            "doctor": "Check your Homebrew setup for problems.",
        }
    },
    "make": {
        "description": "Build tool — runs instructions from a Makefile to compile or automate tasks.",
        "flags": {
            "-f": "File — use a specific Makefile instead of the default.",
            "-j": "Jobs — run this many tasks in parallel to speed up the build.",
            "-n": "Dry run — show what would be run without actually running it.",
            "-C": "Change directory — run make in a specific directory.",
            "clean": "Run the 'clean' target, which usually deletes compiled files.",
        }
    },
    "open": {
        "description": "Open a file, folder, or URL with the default application (macOS only).",
        "flags": {
            "-a": "Application — open with a specific app (e.g. open -a TextEdit file.txt).",
            "-e": "Edit — open the file in TextEdit.",
            "-R": "Reveal — show the file in Finder without opening it.",
            "-n": "New instance — open a new instance of the application.",
        }
    },
    "printenv": {
        "description": "Print the value of one or all environment variables.",
        "flags": {}
    },
    "tr": {
        "description": "Translate or delete characters — replace one character with another across input.",
        "flags": {
            "-d": "Delete — remove all occurrences of specified characters.",
            "-s": "Squeeze — replace repeated characters with a single one.",
            "-c": "Complement — operate on all characters NOT in the given set.",
        }
    },
    "basename": {
        "description": "Strip the directory path from a filename — returns just the file name.",
        "flags": {
            "-s": "Suffix — also strip a specific file extension (e.g. -s .txt).",
        }
    },
    "dirname": {
        "description": "Return the directory portion of a path — the opposite of basename.",
        "flags": {}
    },
    "nohup": {
        "description": "Run a command that keeps running even after you close the terminal.",
        "flags": {
            "&": "Run in the background (typically added at the end: nohup command &).",
        }
    },
    "jobs": {
        "description": "List background and suspended jobs in the current terminal session.",
        "flags": {
            "-l": "Long format — also show the process ID of each job.",
            "-p": "Print only the process IDs.",
        }
    },
    "bg": {
        "description": "Resume a suspended job and run it in the background.",
        "flags": {}
    },
    "fg": {
        "description": "Bring a background or suspended job to the foreground.",
        "flags": {}
    },
}
