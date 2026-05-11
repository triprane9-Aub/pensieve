"""Pensieve — a simple journal for storing memories."""

import json
import sys
from datetime import datetime
from pathlib import Path

MEMORIES_FILE = Path(__file__).parent / "memories.json"


def load_memories():
    if not MEMORIES_FILE.exists():
        return []
    with MEMORIES_FILE.open() as f:
        return json.load(f)


def save_memories(memories):
    with MEMORIES_FILE.open("w") as f:
        json.dump(memories, f, indent=2)


def add_memory(text):
    memories = load_memories()
    memory = {
        "id": len(memories) + 1,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "text": text,
    }
    memories.append(memory)
    save_memories(memories)
    print(f"Memory #{memory['id']} saved.")


def list_memories():
    memories = load_memories()
    if not memories:
        print("No memories yet. Add one with: python3 pensieve.py add \"your memory\"")
        return
    for m in memories:
        when = datetime.fromisoformat(m["timestamp"]).strftime("%Y-%m-%d %H:%M")
        print(f"#{m['id']:<3} {when}  {m['text']}")


def print_help():
    print("Pensieve — your personal memory store")
    print("Usage: python3 pensieve.py <command> [args]")
    print()
    print("Commands:")
    print("  add <text>   Save a new memory")
    print("  list         Show all memories")


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print('Usage: python3 pensieve.py add "your memory here"')
            return
        text = " ".join(sys.argv[2:])
        add_memory(text)
    elif command == "list":
        list_memories()
    else:
        print(f"Unknown command: {command}")
        print_help()


if __name__ == "__main__":
    main()
