"""Pensieve — a simple journal for storing memories."""

import sys


def main():
    if len(sys.argv) < 2:
        print("Pensieve — your personal memory store")
        print("Usage: python3 pensieve.py <command>")
        print("Commands: (none yet — coming soon)")
        return

    command = sys.argv[1]
    print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
