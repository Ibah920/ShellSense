import os
import anthropic

def ask_claude(command):
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    if not api_key:
        return None

    client = anthropic.Anthropic(api_key=api_key)

    try:
        message = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=300,
            messages=[
                {
                    "role": "user",
                    "content": f"Explain this shell command in plain English, flag by flag, in 3-5 sentences. Be beginner-friendly. Command: {command}"
                }
            ]
        )
        return message.content[0].text
    except Exception:
        return None
