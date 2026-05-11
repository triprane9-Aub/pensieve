# Pensieve

A simple command-line journal for storing your memories, inspired by the Pensieve from Harry Potter.

## Usage

Save a new memory:

```bash
python3 pensieve.py add "The first snow of the year fell today"
```

See all your memories:

```bash
python3 pensieve.py list
```

Delete a memory by id (remaining memories are renumbered):

```bash
python3 pensieve.py delete 3
```

Memories are stored locally in `memories.json`.

## Roadmap

- [x] `add` — save a new memory
- [x] `list` — see all memories
- [x] `delete <id>` — remove a memory
- [ ] `view <id>` — revisit a specific memory
- [ ] `search <term>` — find memories by keyword
