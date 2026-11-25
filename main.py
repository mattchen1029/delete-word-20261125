import os

WORD = "literally"

MIN_CHARS = 1
MAX_CHARS = 77
OUTPUT_NAME = "entry.txt"


def validate_word(word):
    if not (MIN_CHARS <= len(word) <= MAX_CHARS):
        raise ValueError("word must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(word)))
    if not word.strip():
        raise ValueError("word must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word, got %d" % len(word.split()))


def write_entry(word, out_dir):
    validate_word(word)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_NAME), "w", encoding="utf-8") as f:
        f.write(word)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(WORD, out_dir)


if __name__ == "__main__":
    main()
