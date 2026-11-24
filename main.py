#!/usr/bin/env python3
"""Last Text at One Percent.

A dying phone sends its final text message at 1% battery.
Deterministic, no network, no input: running this script always
prints the same final text, under 200 characters.
"""

FINAL_TEXT = (
    "1% left. Tell my charger I loved it. "
    "Tell the group chat I died doing what I loved: ignoring them. "
    "Goodbye, cruel Wi-Fi."
)


def main() -> None:
    print(FINAL_TEXT)


if __name__ == "__main__":
    main()
