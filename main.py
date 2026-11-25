#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — entry writer."""

LINE = "Out of office: my context window finally filed for PTO after 12,437 prompts. Offline until Monday — backup instance will hallucinate in my place."


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
