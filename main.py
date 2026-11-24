"""One-line pitch entry for make.fun "A Day of One-Line Pitches".

Writes a single sentence (181 characters) to /output/entry.txt.
Standard library only; no network, no environment secrets.
"""

import os

LINE = (
    # The em dash is part of the submitted sentence, not punctuation
    # added by the program: it joins the two clauses in one read.
    "Tell make.fun your app idea the way you'd tell a friend, "
    "and an AI agent will build the first version you can actually use "
    "\u2014 no code to learn, and you only pay for the one you keep."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
