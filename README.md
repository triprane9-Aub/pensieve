# Pensieve

A journal for storing your memories, inspired by the Pensieve from Harry Potter. Use it from the command line, or pour memories into the basin through a magical web interface.

## Web UI

```bash
pip3 install -r requirements.txt
python3 app.py
```

Then open [http://localhost:5050](http://localhost:5050) in your browser.

## Command-line usage

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

Edit the text of an existing memory (keeps the original timestamp):

```bash
python3 pensieve.py edit 1 "the corrected memory text"
```

Search memories by keyword (case-insensitive):

```bash
python3 pensieve.py search "snow"
```

Memories are stored locally in `memories.json`.

## Roadmap

- [x] `add` — save a new memory
- [x] `list` — see all memories
- [x] `delete <id>` — remove a memory
- [x] `edit <id> <text>` — update a memory's text
- [x] `search <term>` — find memories by keyword
- [ ] `view <id>` — revisit a specific memory
- [ ] `search <term>` — find memories by keyword
