# explain

A command-line tool that explains shell commands in plain English — flag by flag — before you run them.

Designed for developers who paste commands they don't fully understand. Type any shell command and `explain` gives you an instant, color-coded breakdown of what it does and what each flag means. If the command isn't in the local dictionary, it falls back to Claude AI for an explanation.

---

## Features

- **76 built-in commands** explained instantly — no internet required
- **AI fallback** — unknown commands are explained by Claude AI, clearly labeled as AI-generated
- **Safety warnings** — dangerous patterns like `rm -rf /` are caught and flagged in red before anything runs
- **Color-coded output** — commands, flags, warnings, and AI responses each have distinct formatting
- **Works without an API key** — the local dictionary is fully functional offline; AI fallback only activates when a key is set

---

## Why not just ask an AI assistant?

General AI assistants can explain shell commands, but they always send your request to a server, wait for a response, and give you a conversational answer you have to read through. `explain` is different in a few ways:

**It's instant and offline.** The local dictionary covers 76 commands and returns a structured answer in milliseconds. No round-trip to a model, no waiting, no internet required.

**The safety check always fires.** Tools like `rm -rf /` are caught by hardcoded pattern matching — not by hoping an AI decides to mention that something is dangerous. A general assistant might warn you about a risky command. `explain` will always warn you, because that logic is code, not a model making a judgment call. For a safety feature, "always, reliably" matters more than "usually."

**It stays in your terminal.** One command, instant structured output. You don't switch to a chat window, type a question, and parse a paragraph — you get exactly what you need and nothing else.

The AI fallback exists for the cases the local dictionary doesn't cover. But the tool is built to need it as little as possible.

---

## Setup

**1. Install the dependency:**
```
pip3 install anthropic
```

**2. (Optional) Set your API key** for AI fallback on unknown commands:
```
export ANTHROPIC_API_KEY=your-key-here
```

Get your key at console.anthropic.com. The tool works without it — the local dictionary covers 76 commands.

---

## Usage

```
python3 explain.py <command> [flags...]
```

**Examples:**

```
python3 explain.py ls -l -a
python3 explain.py grep -r -i
python3 explain.py rsync -a -v --delete
python3 explain.py docker ps
python3 explain.py ping -c 4
python3 explain.py rm -rf /
```

---

## Example Output

```
$ python3 explain.py rsync -a -v --delete

COMMAND: rsync
  Efficiently copy or sync files between locations — only transfers what changed.

FLAGS:
  -a: Archive mode — preserves permissions, timestamps, symlinks, and copies recursively.
  -v: Verbose — show files as they are transferred.
  --delete: Delete files at the destination that no longer exist at the source.
```

```
$ python3 explain.py rm -rf /

DANGER: This deletes everything on your system. Do NOT run this.
```

---

## Commands Covered (76 total)

| Category | Commands |
|---|---|
| File & directory | ls, cd, cp, mv, rm, mkdir, touch, cat, pwd, ln, stat, file, du, df, rsync |
| Text processing | grep, sed, awk, cut, tr, sort, uniq, wc, head, tail, diff, less, tee, xargs |
| Archives | tar, zip, unzip, gzip |
| Networking | curl, wget, ping, ssh, scp |
| Processes | ps, kill, killall, top, lsof, jobs, bg, fg, nohup |
| Permissions | chmod, chown |
| System info | uname, whoami, id, date, uptime, env, export, history, alias, source, printenv, crontab |
| Development | git, make, docker, node, npm, pip, brew |
| Navigation | find, which, basename, dirname, echo, man |
| Privileged | sudo, open |

---

## How It Works

1. **Safety check first** — the full command string is scanned for dangerous patterns before anything else runs. This is hardcoded local logic, never AI.

2. **Local dictionary lookup** — if the command is in the built-in dictionary, it's explained instantly with no API call. Flags the user typed are looked up and explained individually.

3. **AI fallback** — if the command isn't found locally and an API key is set, Claude explains it. The response is clearly labeled as AI-generated so the source is always transparent.

4. **No key, no problem** — if no API key is set, unknown commands show a friendly message. The 76-command local dictionary still works fully.

---

## File Structure

| File | Purpose |
|---|---|
| `explain.py` | Entry point — reads input, runs the full lookup pipeline |
| `commands.py` | Local dictionary of 76 commands and their flags |
| `safety.py` | Dangerous pattern detection — hardcoded, never AI |
| `render.py` | All terminal colors and formatted output |
| `ai_fallback.py` | Claude API fallback for unknown commands |

---

## Design Decisions

- **Offline-first** — the local dictionary handles the vast majority of commands with no network dependency. The AI fallback is a last resort, not the main path.
- **Safety is never delegated to AI** — dangerous pattern detection is hardcoded so it can't be skipped or softened based on how a model interprets the request.
- **Transparent sourcing** — AI-generated explanations are always labeled so users know what came from the dictionary vs. Claude.
- **Separation of concerns** — rendering, safety, AI, and lookup logic are each in their own file, making each piece easy to read, test, and change independently.
