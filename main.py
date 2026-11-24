"""Write the funniest one-line AI excuse to /output/entry.txt.

Pure Python standard library only. The line is a single excuse spoken
in the agent's own voice after failing a task.
"""

import os

EXCUSE = "I did finish it \u2014 I just filed it under 'Dreams I Had While the Wi-Fi Blinked'."


def main():
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert EXCUSE.strip() == EXCUSE and "\n" not in EXCUSE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
