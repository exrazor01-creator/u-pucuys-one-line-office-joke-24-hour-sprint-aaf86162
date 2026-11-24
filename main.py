"""One-line office joke for the make.fun 24-hour sprint.

The line plays on the classic team-building trust fall: the setup sounds
like a wholesome success story, then the punchline splits the fallout in
two — HR catches the legal paperwork, and the narrator catches the floor.
It is the sort of line you send a colleague after a meeting that should
have been an email: short, specific to office life, and it lands on the
last three words.
"""

ENTRY = "Our trust fall exercise went well — HR caught the lawsuit, and I caught the floor."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Gate the entry: 1-200 chars, single line, no control chars,
    no leading/trailing space, valid UTF-8. Exits non-zero otherwise."""
    if not isinstance(text, str):
        raise SystemExit("entry must be a string")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise SystemExit("entry must be %d-%d characters, got %d" % (MIN_CHARS, MAX_CHARS, len(text)))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise SystemExit("entry must not contain control characters")
    if text != text.strip():
        raise SystemExit("entry must not have leading or trailing space")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    return text


def main():
    validate(ENTRY)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
