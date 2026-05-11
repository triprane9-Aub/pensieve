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

Memories are stored locally in `memories.json`.

## Roadmap

- [x] `add` — save a new memory
- [x] `list` — see all memories
- [ ] `view <id>` — revisit a specific memory
- [ ] `search <term>` — find memories by keyword
