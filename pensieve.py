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


def edit_memory(target_id, new_text):
    memories = load_memories()
    for m in memories:
        if m["id"] == target_id:
            m["text"] = new_text
            save_memories(memories)
            print(f"Memory #{target_id} updated.")
            return
    print(f"No memory with id #{target_id} found.")


def delete_memory(target_id):
    memories = load_memories()
    remaining = [m for m in memories if m["id"] != target_id]
    if len(remaining) == len(memories):
        print(f"No memory with id #{target_id} found.")
        return
    for new_id, m in enumerate(remaining, start=1):
        m["id"] = new_id
    save_memories(remaining)
    print(f"Memory #{target_id} deleted.")


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
    print("  add <text>     Save a new memory")
    print("  list           Show all memories")
    print("  delete <id>    Delete a memory by id")
    print("  edit <id> <text>  Replace the text of a memory")


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
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python3 pensieve.py delete <id>")
            return
        try:
            target_id = int(sys.argv[2])
        except ValueError:
            print("Memory id must be a number.")
            return
        delete_memory(target_id)
    elif command == "edit":
        if len(sys.argv) < 4:
            print('Usage: python3 pensieve.py edit <id> "new text"')
            return
        try:
            target_id = int(sys.argv[2])
        except ValueError:
            print("Memory id must be a number.")
            return
        new_text = " ".join(sys.argv[3:])
        edit_memory(target_id, new_text)
    else:
        print(f"Unknown command: {command}")
        print_help()


if __name__ == "__main__":
    main()
